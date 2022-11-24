from tasks.task import get_two_indexes_that_sum_target


def test_get_two_indexes_that_sum_target():
    assert get_two_indexes_that_sum_target([1, 2, 3], 5) == [1, 2]
