from math import ceil
from typing import Any, List


def chunk(full_list: List[Any], chunks: int, chunk_index: int) -> range:
    indices = range(len(full_list))

    chunk_size = ceil(len(full_list) / chunks)

    chunks = [
        indices[index : index + chunk_size]
        for index in range(0, len(full_list), chunk_size)
    ]

    return chunks[chunk_index]
