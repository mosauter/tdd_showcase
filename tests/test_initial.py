from __future__ import annotations

import pytest


def complex_add_and_subtract(a: int, b: int, c: int) -> int:
    return a + b - c


@pytest.mark.parametrize(
    ("input_a", "input_b", "input_c", "expected"),
    [
        pytest.param(1, 1, 1, 1),
        pytest.param(2, 1, 1, 2),
        pytest.param(3, 1, 1, 3),
        pytest.param(4, 1, 1, 4),
        pytest.param(5, 1, 1, 5),
        pytest.param(2, 1, 2, 1),
        pytest.param(3, 1, 3, 1),
        pytest.param(4, 1, 4, 1),
        pytest.param(5, 1, 5, 1),
    ],
)
def test_initial_should_do_what(
    input_a: int,
    input_b: int,
    input_c: int,
    expected: int,
) -> None:
    assert complex_add_and_subtract(input_a, input_b, input_c) == expected
