from math import ceil
from typing import Any, List


def chunk(full_list: List[Any], chunks: int, chunk_index: int) -> range:
    chunk_size = ceil(len(full_list) / chunks)

    return range(chunk_size)
