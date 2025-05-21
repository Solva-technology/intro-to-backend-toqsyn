from tasks.task2 import is_even

def test_is_even():
    assert is_even(2) == True, (
        'При четном number, функция должна вернуть значение True'
        )
    assert is_even(3) == False, (
        'При нечетном number, функция должна вернуть значение False'
        )
