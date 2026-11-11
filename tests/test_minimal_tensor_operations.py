from __future__ import annotations

import pytest
import torch


def perform_tensor_operation(device: torch.device) -> torch.Tensor:
    """Perform a minimal matrix multiplication on the requested device."""

    left = torch.tensor(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ],
        dtype=torch.float32,
        device=device,
    )

    right = torch.tensor(
        [
            [5.0, 6.0],
            [7.0, 8.0],
        ],
        dtype=torch.float32,
        device=device,
    )

    return torch.matmul(left, right)


def expected_result() -> torch.Tensor:
    """Return the expected matrix multiplication result."""

    return torch.tensor(
        [
            [19.0, 22.0],
            [43.0, 50.0],
        ],
        dtype=torch.float32,
    )


def available_gpu_device() -> torch.device | None:
    """Return a supported GPU device, if available."""

    if torch.cuda.is_available():
        return torch.device("cuda")

    return None


def test_cpu_tensor_operation() -> None:
    """Verify that basic tensor operations work on the CPU."""

    device = torch.device("cpu")

    result = perform_tensor_operation(device)

    assert result.device.type == "cpu"

    torch.testing.assert_close(
        result,
        expected_result(),
    )


@pytest.mark.gpu
def test_gpu_tensor_operation() -> None:
    """Verify that basic tensor operations work on a supported GPU."""

    device = available_gpu_device()

    if device is None:
        pytest.skip("No supported PyTorch GPU backend is available.")

    result = perform_tensor_operation(device)

    assert result.device.type == device.type

    torch.testing.assert_close(
        result.cpu(),
        expected_result(),
    )
