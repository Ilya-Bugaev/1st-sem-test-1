from src.bin_search import bin_search


def test_middle():
    assert bin_search([1, 2, 3, 4, 5], 3) == 2


def test_start():
    assert bin_search([1, 2, 3, 4], 1) == 0
    assert bin_search([1, 2, 3, 4], 2) == 1


def test_end():
    assert bin_search([1, 2, 3, 4, 5], 5) == 4
    assert bin_search([1, 2, 3, 4], 4) == 3


def test_not_in_list():
    assert bin_search([1, 2, 3, 4], 5) == -1
    assert bin_search([1, 2, 3, 4], 0) == -1
    assert bin_search([1, 2, 3, 4], 6) == -1
