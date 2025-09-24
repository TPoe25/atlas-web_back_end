#!/usr/bin/env python3
"""
simple pagination example
"""

import math
from typing import List, Tuple, Dict

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

def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Gets the requested page from the dataset and returns a dictionary
        with the following key-value pairs:

        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary with the pagination information.
        """
        dataset = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page - 1 > 0 else None

        return {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }

Server.get_page = get_page
Server.get_hyper = get_hyper
