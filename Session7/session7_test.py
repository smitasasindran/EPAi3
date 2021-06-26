import pytest

from .session7 import find_docstring, get_fibonacci, count_function, fn_count, count_function_with_dict


def test_docstring_greater():
    def testfn():
        "This is a test function with docstring greater than 50 chars"
        return True

    assert find_docstring(testfn)() == True

def test_docstring_lesser():
    def testfn():
        "Greetings, Earthlings!"
        return True

    assert find_docstring(testfn)() == False

def test_docstring_none():
    def testfn():
        return True

    assert find_docstring(testfn)() == False

def test_docstring_nonfunction():
    assert find_docstring("abcde")() == False
    assert find_docstring(1)() == False
    assert find_docstring(True)() == False

def test_docstring_builtin_function():
    assert find_docstring(open)() == True
    assert find_docstring(print)() == True


def test_fibonacci_first():
    testfn = get_fibonacci()
    assert testfn() == 0

def test_fibonacci_sequence():
    testfn = get_fibonacci()
    assert testfn() == 0
    assert testfn() == 1
    assert testfn() == 1
    assert testfn() == 2
    assert testfn() == 3
    assert testfn() == 5
    assert testfn() == 8


def mult(a, b, c):
    return a * b * c

def add(a, b):
    return a + b

def div(a, b):
    return a / b

def test_only_add():
    counted_add = count_function(add)
    assert fn_count.get('add', None) == None
    counted_add(1, 2)
    assert fn_count['add'] == 1

def test_only_mult():
    counted_mult = count_function(mult)
    assert fn_count.get('mult', None) == None
    counted_mult(1, 2, 3)
    assert fn_count.get('mult', 0) == 1
    assert fn_count.get('add', 0) == 1

def test_only_div():
    counted_div = count_function(div)
    assert fn_count.get('div', None) == None
    counted_div(4, 2)
    assert fn_count.get('div', 0) == 1
    assert fn_count.get('mult', 0) == 1
    assert fn_count.get('add', 0) == 1

def test_all_counts():
    print("in test before:", fn_count)
    # fn_count still retains old values from prev tests, but gets overwritten.. no nice way of clearing it
    counted_add = count_function(add)
    counted_mult = count_function(mult)
    counted_div = count_function(div)
    counted_add(1, 2)
    counted_add(1, 3)
    # counted_mult(3, 4, 5)
    counted_div(4, 2)
    counted_div(4, 2)
    counted_div(4, 2)

    print("in test after:", fn_count)
    assert fn_count.get('div', 0) == 3
    assert fn_count.get('mult', 0) == 1
    assert fn_count.get('add', 0) == 2


def test_only_add_dict_empty():
    counted_add, fn_count = count_function_with_dict(add, {})
    assert fn_count.get('add', None) == None
    counted_add(1, 2)
    assert fn_count['add'] == 1

def test_only_add_dict_nonempty():
    counted_add, fn_count = count_function_with_dict(add, {'add': 3})
    assert fn_count.get('add', None) == 3
    counted_add(1, 2)
    assert fn_count['add'] == 4

def test_only_mult_dict_empty():
    counted_mult, fn_count = count_function_with_dict(mult, {})
    assert fn_count.get('mult', None) == None
    assert fn_count.get('add', None) == None
    counted_mult(3, 4, 5)
    assert fn_count.get('add', None) == None
    assert fn_count['mult'] == 1
    counted_mult(3, 4, 5)
    counted_mult(3, 4, 5)
    assert fn_count['mult'] == 3

def test_only_mult_dict_nonempty():
    counted_mult, fn_count = count_function_with_dict(mult, {'mult': 5})
    assert fn_count.get('mult', None) == 5
    assert fn_count.get('add', None) == None
    counted_mult(3, 4, 5)
    assert fn_count.get('add', None) == None
    assert fn_count['mult'] == 6
    counted_mult(3, 4, 5)
    counted_mult(3, 4, 5)
    assert fn_count['mult'] == 8

def test_only_mult_dict_nonempty2():
    counted_mult, fn_count = count_function_with_dict(mult, {'mult': 3, 'add': 2})
    assert fn_count.get('mult', None) == 3
    assert fn_count.get('add', None) == 2
    counted_mult(3, 4, 5)
    assert fn_count.get('add', None) == 2
    assert fn_count['mult'] == 4


def test_all_dict_empty():
    counted_add, fn_count_add = count_function_with_dict(add, {})
    counted_mult, fn_count_mult = count_function_with_dict(mult, {})
    counted_div, fn_count_div = count_function_with_dict(div, {})

    counted_mult(3, 4, 5)
    counted_mult(3, 4, 5)
    counted_add(1, 2)
    counted_div(4, 2)

    assert fn_count_add['add'] == 1
    assert fn_count_mult['mult'] == 2
    assert fn_count_div['div'] == 1

    assert fn_count_add.get('mult', None) == None
    assert fn_count_add.get('div', None) == None
    assert fn_count_mult.get('add', None) == None
    assert fn_count_mult.get('div', None) == None
    assert fn_count_div.get('add', None) == None
    assert fn_count_div.get('mult', None) == None


def test_all_dict_empty_common():
    common_dict = {}
    counted_add, common_dict = count_function_with_dict(add, common_dict)
    counted_mult, common_dict = count_function_with_dict(mult, common_dict)
    counted_div, common_dict = count_function_with_dict(div, common_dict)

    counted_mult(3, 4, 5)
    counted_mult(3, 4, 5)
    counted_add(1, 2)
    counted_div(4, 2)

    assert common_dict['add'] == 1
    assert common_dict['mult'] == 2
    assert common_dict['div'] == 1

def test_all_dict_nonempty_common():
    common_dict = {'add': 3, 'div': 1, 'dalek': 0}
    counted_add, common_dict = count_function_with_dict(add, common_dict)
    counted_mult, common_dict = count_function_with_dict(mult, common_dict)
    counted_div, common_dict = count_function_with_dict(div, common_dict)

    counted_mult(3, 4, 5)
    counted_mult(3, 4, 5)
    counted_add(1, 2)
    counted_div(4, 2)

    assert common_dict['add'] == 4
    assert common_dict['mult'] == 2
    assert common_dict['div'] == 2
    assert common_dict['dalek'] == 0

