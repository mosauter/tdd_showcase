from tdd_showcase.showcase import chunk


def test_chunking_should_give_full_range_when_asking_for_one_chunk() -> None:
    full_list = [1, 2, 3, 4, 5]

    assert chunk(full_list, chunks=1, chunk_index=0) == range(0, 5)
