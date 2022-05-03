from math import ceil
from typing import Any, List


def chunk(full_list: List[Any], chunks: int, chunk_index: int) -> range:
    list_length = len(full_list)
    indices = range(list_length)

    chunk_size = ceil(list_length / chunks)

    chunks = [
        indices[index : index + chunk_size]
        for index in range(0, list_length, chunk_size)
    ]

    return chunks[chunk_index]
