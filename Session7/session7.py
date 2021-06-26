import inspect


def find_docstring(fn):
    "Function to check if the input function's docstring is greater than 50 or not"
    max_length = 50

    def inner():
        docstring = ""
        if '__doc__' in dir(fn) and (inspect.isfunction(fn) or callable(fn)):
            docstring = fn.__doc__ if fn.__doc__ else ""

        return len(docstring) > max_length

    return inner


def get_fibonacci():
    "Function to return the next Fibonacci number in the series"
    pos = 0
    next = 0

    def inner():

        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        nonlocal pos, next
        next = fibonacci(pos)
        pos += 1
        print("Next fibonacci number: ", next)
        return next
    return inner

def get_next_fibonacci(n):
    "Function to return the next Fibonacci number in the series"
    # Use memoization to store in intermediate dict
    pass


fn_count = {}
def count_function(fn):
    "Function to count how many times input functions were called, and store it in global dict"
    count = 0

    def inner(*args, **kwargs):
        global fn_count
        nonlocal count
        count += 1
        fn_count[fn.__name__] = count
        print("fncount is:", fn_count)
        return fn(*args, **kwargs)

    return inner


def count_function_with_dict(fn, fn_count):
    "Function to count how many times input functions were called, and store it in the passed dict"
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count = fn_count.get(fn.__name__, 0)
        count += 1
        # existing = fn_count.get(fn.__name__, 0)
        fn_count[fn.__name__] = count
        print("fncount is:", fn_count)
        return fn(*args, **kwargs)

    return inner, fn_count

