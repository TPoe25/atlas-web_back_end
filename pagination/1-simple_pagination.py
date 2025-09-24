#!/usr/bin/env python3
"""
simple pagination example
"""

import csv
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple of the start and end indicies for given page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> list:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                import csv
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> list:
        """
        Returns a page of the dataset (list of rows).

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            list: requested page.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
