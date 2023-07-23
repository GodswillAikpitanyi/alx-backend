#!/usr/bin/env python3

def index_range(page, page_size):

    """ Calculate the start index based on the given page number & page size"""
    start_index = (page - 1) * page_size

    """ Calculate the end index by adding the page size to the start index """
    end_index = start_index + page_size

    return (start_index, end_index)
