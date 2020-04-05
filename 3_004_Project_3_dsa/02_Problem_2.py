
def rotated_array_pivot(array):
    """
    Find the pivot index in a rotated array sorted in ascending order. The pivot index is the position of the smallest value in the array.

    Args:
       array(array): Input array
    Returns:
       int: the index of the pivot, if found, in the arr
       -1: if the pivot is not found (for testing)
    """
    pivot_index = -1

    first_index = 0
    last_index = len(array) - 1

    while first_index <= last_index:

        mid_index = (first_index + last_index) // 2
        first_item = array[first_index]
        last_item = array[last_index]
        mid_item = array[mid_index]

        if first_item <= last_item: # array or subarray sorted
            pivot_index = first_index
            break
        elif first_item <= mid_item: # first half sorted
            first_index = mid_index + 1 # pivot is in the other half of the array
        elif mid_item <= last_item: # second half sorted
            last_index = mid_index # pivot is in the first half of the array
        else: # index not found
            break

    return pivot_index

def binary_search(array, target):
    '''
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    first_index = 0
    last_index = len(array) - 1

    while first_index <= last_index:

        mid_index = (first_index + last_index) // 2
        mid_item = array[mid_index]

        if target == mid_item: # we have found the element
            return mid_index

        if target < mid_item: # we will only search in the left half
            last_index = mid_index - 1
        else: # we will only search in the right half
            first_index = mid_index + 1

    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated array sorted in ascending order at some pivot unknow beforehand. Assume there are no duplicates in the list.

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Null input
    if input_list is None or number is None:
        return -1
    # Empty list
    if input_list == []:
        return -1

    first_item = input_list[0]
    last_item = input_list[len(input_list)-1]

    # get the position and value of the pivot to partition the input list
    pivot_index = rotated_array_pivot(input_list)
    pivot_item = input_list[pivot_index]


    # the position of the input number is the pivot position
    if number == pivot_item:
        return pivot_index

    # search number index in the first half of the list
    number_index = binary_search(input_list[0: pivot_index], number)
    if number_index != -1:
        return number_index

    # search number index in the second half of the list
    number_index = binary_search(input_list[pivot_index: len(input_list)],number)
    if number_index != -1:
        return pivot_index + number_index

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        #print("Pass")
        return "Pass"
    else:
        # print("Fail")
        return "Fail"

# Udacity supported test
print("------- \t Udacity supported test \t -------")
arr = [6, 7, 8, 9, 10, 1, 2, 3, 4]
number = 6
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

arr = [6, 7, 8, 1, 2, 3, 4]
number = 8
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

number = 1
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

number = 10
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

# Full cycle rotated array
print("------- \t Full cycle rotated test \t -------")

arr = [1, 2, 3, 4]
number = 1
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

arr = [4, 1, 2, 3]
number = 1
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

arr = [3, 4, 1, 2]
number = 1
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

arr = [2, 3, 4, 1]
number = 1
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

# Negative numbers
print("------- \t Negative numbers test \t -------")
arr = [-3, -2, -1, 0, 1]
number = 0
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

# EDGE CASES
print("------- \t Edge cases \t -------")
arr = [1]
number = 1
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

arr = [1]
number = 0
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))

# No valid input
print("------- \t No valid input \t -------")
arr = []
number = []
index = rotated_array_search(arr, number)
test = test_function([arr, number])
print('rotated_array_search({}, {}) index: {} \t {}'.format(arr,number,index, test))
