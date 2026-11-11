from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

PROJECT_ROOT = Path(__file__).resolve().parents[1]
COMPOSE_FILE = PROJECT_ROOT / "infrastructure" / "surrealdb" / "compose.yaml"

SERVICE_NAME = "surrealdb"
HEALTH_URL = "http://127.0.0.1:8000/health"

DEFAULT_TIMEOUT = 90
POLL_INTERVAL = 3


class DeploymentError(RuntimeError):
    """Raised when deployment or health verification fails."""


def run_command(
    command: list[str],
    *,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    """Execute a command and capture its output."""

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    if check and result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise DeploymentError(f"Command failed: {' '.join(command)}\n{message}")

    return result


def compose_command(*args: str) -> list[str]:
    """Build a Docker Compose command."""

    return [
        "docker",
        "compose",
        "-f",
        str(COMPOSE_FILE),
        *args,
    ]


def verify_docker() -> None:
    """Verify Docker CLI and daemon availability."""

    print("[1/5] Checking Docker...")

    run_command(["docker", "--version"])
    run_command(["docker", "compose", "version"])
    run_command(["docker", "info"])

    print("      Docker is available.")


def validate_compose() -> None:
    """Validate the Compose configuration."""

    print("[2/5] Validating Compose configuration...")

    if not COMPOSE_FILE.is_file():
        raise DeploymentError(f"Compose file not found: {COMPOSE_FILE}")

    run_command(compose_command("config", "--quiet"))

    print("      Compose configuration is valid.")


def deploy_container() -> None:
    """Create or update the SurrealDB container."""

    print("[3/5] Deploying SurrealDB...")

    run_command(
        compose_command(
            "up",
            "-d",
            SERVICE_NAME,
        )
    )

    print("      Deployment command completed.")


def get_container_id() -> str | None:
    """Retrieve the container ID for the Compose service."""

    result = run_command(
        compose_command("ps", "-q", SERVICE_NAME),
        check=False,
    )

    if result.returncode != 0:
        return None

    container_id = result.stdout.strip()

    return container_id or None


def inspect_container(container_id: str) -> tuple[str, str]:
    """Retrieve container state and Docker health status."""

    result = run_command(
        [
            "docker",
            "inspect",
            "--format",
            (
                "{{.State.Status}}|"
                "{{if .State.Health}}"
                "{{.State.Health.Status}}"
                "{{else}}"
                "no-healthcheck"
                "{{end}}"
            ),
            container_id,
        ]
    )

    state, health = result.stdout.strip().split("|", maxsplit=1)

    return state, health


def check_http_health() -> bool:
    """Check the SurrealDB HTTP health endpoint."""

    try:
        with urlopen(HEALTH_URL, timeout=3) as response:
            return response.status == 200

    except URLError, TimeoutError, OSError:
        return False


def print_diagnostics() -> None:
    """Print useful diagnostics following a deployment failure."""

    print("\n--- Container status ---")

    run_command(
        compose_command("ps", "-a"),
        check=False,
    )

    result = run_command(
        compose_command("logs", "--tail", "40", SERVICE_NAME),
        check=False,
    )

    if result.stdout:
        print("\n--- Container logs ---")
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


def wait_for_healthy(timeout: int) -> None:
    """Wait until both Docker and the HTTP health check succeed."""

    print("[4/5] Waiting for SurrealDB health checks...")

    deadline = time.monotonic() + timeout

    while time.monotonic() < deadline:
        container_id = get_container_id()

        if container_id is None:
            time.sleep(POLL_INTERVAL)
            continue

        state, docker_health = inspect_container(container_id)

        if state == "exited" or state == "dead":
            raise DeploymentError(f"Container entered an unexpected state: {state}")

        http_healthy = check_http_health()

        if state == "running":
            print(
                f"      Container: {state} | "
                f"Docker health: {docker_health} | "
                f"HTTP health: {'OK' if http_healthy else 'WAITING'}"
            )

        docker_ready = docker_health in ("healthy", "no-healthcheck")

        if state == "running" and docker_ready and http_healthy:
            return

        time.sleep(POLL_INTERVAL)

    raise DeploymentError(f"SurrealDB did not become healthy within {timeout} seconds.")


def print_final_status() -> None:
    """Display the final Compose service status."""

    print("\n[5/5] Final deployment status:")

    result = run_command(compose_command("ps", SERVICE_NAME))

    print(result.stdout.strip())

    print("\nSurrealDB is running and responding to health checks.")
    print(f"Health endpoint: {HEALTH_URL}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deploy and verify the FinWorldModel SurrealDB container."
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help="Health-check timeout in seconds (default: 90).",
    )

    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")

    try:
        verify_docker()
        validate_compose()
        deploy_container()
        wait_for_healthy(args.timeout)
        print_final_status()

        return 0

    except (DeploymentError, OSError) as exc:
        print(f"\nDEPLOYMENT FAILED: {exc}", file=sys.stderr)
        print_diagnostics()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
