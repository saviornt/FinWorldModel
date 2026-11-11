from __future__ import annotations

import argparse
import os
import sys
import uuid
from pathlib import Path

import arcticdb as adb  # pyright: ignore[reportMissingTypeStubs]
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_STORAGE_PATH = PROJECT_ROOT / "data" / "arcticdb"
DEFAULT_LIBRARY = "market_data"


class ArcticDBError(RuntimeError):
    """Raised when ArcticDB initialization or verification fails."""


def initialize_storage(storage_path: Path) -> adb.Arctic:
    """Create the storage directory and initialize ArcticDB."""

    storage_path = storage_path.expanduser().resolve()

    if storage_path.exists() and not storage_path.is_dir():
        raise ArcticDBError(f"Storage path exists but is not a directory: {storage_path}")

    storage_path.mkdir(parents=True, exist_ok=True)

    uri = f"lmdb://{storage_path.as_posix()}"

    print(f"      Storage path: {storage_path}")
    print("      Initializing LMDB backend...")

    return adb.Arctic(uri)


def initialize_library(
    arctic: adb.Arctic,
    library_name: str,
):
    """Create the library if necessary and return its handle."""

    print(f"[2/4] Checking library '{library_name}'...")

    existing_libraries = arctic.list_libraries()

    if library_name not in existing_libraries:
        arctic.create_library(library_name)
        print("      Library created.")
    else:
        print("      Library already exists.")

    library = arctic[library_name]

    if library.name != library_name:
        raise ArcticDBError(f"Unexpected library returned: {library.name}")

    return library


def verify_storage(library) -> None:
    """Perform a temporary write/read/delete verification."""

    print("[3/4] Performing storage health check...")

    symbol = f"__healthcheck_{uuid.uuid4().hex}"

    original = pd.DataFrame(
        {
            "value": [1.0, 2.0, 3.0],
        },
        index=pd.date_range(
            "2026-01-01",
            periods=3,
            freq="D",
            name="timestamp",
        ),
    )

    written = False

    try:
        library.write(symbol, original)
        written = True

        result = library.read(symbol).data

        # ArcticDB does not necessarily preserve pandas frequency metadata.
        # Compare actual index values and data, not the inferred frequency.
        original.index = pd.DatetimeIndex(
            original.index.to_numpy(),
            name=original.index.name,
        )

        result.index = pd.DatetimeIndex(
            result.index.to_numpy(),
            name=result.index.name,
        )

        pd.testing.assert_frame_equal(
            original,
            result,
            check_exact=True,
        )

        print("      Write test: PASSED")
        print("      Read test:  PASSED")
        print("      Data comparison: PASSED")

    finally:
        if written:
            library.delete(symbol)

            if library.has_symbol(symbol):
                raise ArcticDBError("Temporary health-check symbol could not be deleted.")

    print("      Cleanup: PASSED")


def print_status(
    storage_path: Path,
    library_name: str,
) -> None:
    """Display the final initialization status."""

    print("\n[4/4] ArcticDB status")
    print("------------------------------")
    print("Backend:       LMDB")
    print(f"Storage:       {storage_path}")
    print(f"Library:       {library_name}")
    print("Write access:  OK")
    print("Read access:   OK")
    print("Cleanup:       OK")
    print("------------------------------")
    print("ArcticDB is initialized and healthy.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=("Initialize and verify FinWorldModel ArcticDB storage.")
    )

    parser.add_argument(
        "--path",
        type=Path,
        default=None,
        help="Override the ArcticDB storage directory.",
    )

    parser.add_argument(
        "--library",
        default=DEFAULT_LIBRARY,
        help="Library to initialize (default: market_data).",
    )

    args = parser.parse_args()

    if not args.library or args.library.strip() != args.library:
        parser.error("--library must be a non-empty name without surrounding whitespace")

    configured_path = args.path or Path(
        os.environ.get(
            "FINWORLDMODEL_ARCTICDB_PATH",
            str(DEFAULT_STORAGE_PATH),
        )
    )

    storage_path = configured_path.expanduser().resolve()

    print("FinWorldModel ArcticDB Initialization")
    print("=====================================")

    try:
        print("[1/4] Initializing storage...")

        arctic = initialize_storage(storage_path)

        library = initialize_library(
            arctic,
            args.library,
        )

        verify_storage(library)

        print_status(
            storage_path,
            args.library,
        )

        return 0

    except Exception as exc:
        print(
            f"\nARCTICDB INITIALIZATION FAILED: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )

        return 1


if __name__ == "__main__":
    raise SystemExit(main())
