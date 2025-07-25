
import pytest

def test_stack():

    stack = []

    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

    print('Все тесты прошли успешно')


def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack
    
    print('Все тесты прошли успешно')

def test_pop_with_empty_stack():
    stack = []

    with pytest.raises (IndexError):
        stack.pop()
