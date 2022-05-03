from typing import List

from pytest import fixture

from tdd_showcase.showcase import chunk


@fixture
def full_list() -> List[int]:
    return [1, 2, 3, 4, 5]


def test_chunking_should_give_full_range_when_asking_for_one_chunk(
    full_list: List[int],
) -> None:
    assert chunk(full_list, chunks=1, chunk_index=0) == range(0, 5)


def test_chunking_should_give_first_half_when_asking_for_two_chunks_and_first_index(
    full_list: List[int],
) -> None:
    assert chunk(full_list, chunks=2, chunk_index=0) == range(0, 3)
