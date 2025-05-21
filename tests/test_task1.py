from tasks.task1 import sum_nums


ERROR_DATA = 'Функция должна возвращать сумму двух чисел'

def test_sum_nums():
    assert sum_nums(1, 2) == 3, ERROR_DATA
    assert sum_nums(-1, 5) == 4, ERROR_DATA
