from tasks.task3 import reverse_string

def test_reverse_string():
    assert reverse_string('abc') == 'cba', (
        'При вводе строки "abc" функция должна вернуть "cba" — проверь, '
        'правильно ли переворачивается строка'
    )
    assert reverse_string('') == '', (
        'При вводе пустой строки функция должна вернуть пустую строку'
    )
