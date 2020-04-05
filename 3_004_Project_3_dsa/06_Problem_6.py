# importing the required modules
import random
import timeit

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # Null and empty array check
    if ints is None or len(ints) < 1:
        return None

    # the array has at least one element
    min = ints[0]
    max = ints[0]

    # find the minimum and maximum in the remaining values
    for i in range(1, len(ints)):
        if ints[i] < min:
            min = ints[i]
        if ints[i] > max:
            max = ints[i]
    return min, max

# compute Python's min max time
def min_max_time():
    SETUP_CODE = '''
from __main__ import get_min_max
import random'''

    TEST_CODE = '''
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
result = (min(l), max(l))
    '''
    TEST_CODE_1 = '''
l = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(l)
result = (min(l), max(l))
    '''
    TEST_CODE_2 = '''
l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)
result = (min(l), max(l))
    '''
    TEST_CODE_3 = '''
l = [i for i in range(0, 10000)]  # a list containing 0 - 9999
random.shuffle(l)
result = (min(l), max(l))
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 1000)

    print('min_max iterations: {}'.format(1000))

    # priniting minimum exec. time
    print('input size: {}  \t time: {}  s'.format(10,round(min(times),4)))

    # timeit.repeat statement
    times_2 = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE_1,
                          repeat = 3,
                          number = 1000)

    # priniting minimum exec. time
    print('input size: {}  \t time: {} s'.format(100,round(min(times_2),4)))

    # timeit.repeat statement
    times_3 = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE_2,
                          repeat = 3,
                          number = 1000)

    # priniting minimum exec. time
    print('input size: {}  \t time: {} s'.format(1000,round(min(times_3),4)))

    # timeit.repeat statement
    times_4 = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE_3,
                          repeat = 3,
                          number = 1000)

    # priniting minimum exec. time
    print('input size: {}  \t time: {} s'.format(10000,round(min(times_4),4)))

def get_min_max_time():
    ## code adapted from https://www.geeksforgeeks.org/timeit-python-examples/
    SETUP_CODE = '''
from __main__ import get_min_max
import random'''

    TEST_CODE = '''
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
result = get_min_max(l)
    '''
    TEST_CODE_1 = '''
l = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(l)
result = get_min_max(l)
    '''
    TEST_CODE_2 = '''
l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)
result = get_min_max(l)
    '''
    TEST_CODE_3 = '''
l = [i for i in range(0, 10000)]  # a list containing 0 - 9999
random.shuffle(l)
result = get_min_max(l)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 1000)

    print('get_min_max iterations: {}'.format(1000))

    # priniting minimum exec. time
    print('input size: {}  \t time: {}  s'.format(10,round(min(times),4)))

    # timeit.repeat statement
    times_2 = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE_1,
                          repeat = 3,
                          number = 1000)

    # priniting minimum exec. time
    print('input size: {}  \t time: {} s'.format(100,round(min(times_2),4)))

    # timeit.repeat statement
    times_3 = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE_2,
                          repeat = 3,
                          number = 1000)

    # priniting minimum exec. time
    print('input size: {}  \t time: {} s'.format(1000,round(min(times_3),4)))

    # timeit.repeat statement
    times_4 = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE_3,
                          repeat = 3,
                          number = 1000)

    # priniting minimum exec. time
    print('input size: {}  \t time: {} s'.format(10000,round(min(times_4),4)))

if __name__ == "__main__":

    print("------- \t Not valid input \t -------")

    l = None
    result = None
    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('get_min_max({}): \t{} \t{}'.format(l,result,test))

    l = []
    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('get_min_max({}): \t{} \t{}'.format(l,result,test))

    print("------- \t Edge cases \t -------")


    l = [1]
    result = (min(l), max(l))

    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('get_min_max({}): \t{} \t{}'.format(l,result,test))

    l = [4,4]
    result = (min(l), max(l))
    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('get_min_max({}): \t{} \t{}'.format(l,result,test))

    print("------- \t Udacity supported test \t -------")
    ## Example Test Case of Ten Integers

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    result = (min(l), max(l))
    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('get_min_max({}): \t{} \t{}'.format(l,result,test))

    print("------- \t Testing Large input \t -------")

    l = [i for i in range(0, 100)]  # a list containing 0 - 99
    size = len(l)
    random.shuffle(l)
    result = (min(l), max(l))
    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('input size: {} \t{}'.format(size,test))

    l = [i for i in range(0, 1000)]  # a list containing 0 - 999
    size = len(l)
    random.shuffle(l)
    result = (min(l), max(l))
    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('input size: {} \t{}'.format(size,test))

    l = [i for i in range(0, 10000)]  # a list containing 0 - 9999
    size = len(l)
    random.shuffle(l)
    result = (min(l), max(l))
    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('input size: {} \t{}'.format(size,test))

    l = [i for i in range(0, 100000)]  # a list containing 0 - 99999
    size = len(l)
    random.shuffle(l)
    result = (min(l), max(l))
    test = "Pass" if (result == get_min_max(l)) else "Fail"
    print ('input size: {} \t{}'.format(size,test))

    print("------- \t Running Time Large input \t -------")
    min_max_time()
    get_min_max_time()
