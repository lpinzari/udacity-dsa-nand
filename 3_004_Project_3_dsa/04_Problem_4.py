def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    Note:

    """

    if input_list is None or len(input_list) <= 1:
        return input_list

    # positional indices
    low = 0 # store next position of smaller element from beginning
    mid = 0 # position of the element to be compared
    high = len(input_list) - 1 # store next position of greater element from end

    # iterate till all elements are sorted
    while mid <= high:
        if input_list[mid] == 0 and input_list[low] in [0, 1, 2]:
            # temp = input_list[low]
            # input_list[low] = input_list[mid]
            # input_list[mid] = temp : Swap optimized below Pythonic way :)
            if input_list[low] != 0:
                input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        elif input_list[mid] == 2 and input_list[high] in [0, 1, 2]:
            # temp = input_list[mid]
            # input_list[mid] = input_list[high]
            # input_list[high] = temp : Swap optimized below Pythonic way :)
            if input_list[high] != 2:
                input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1
        else: # element in the array out of the range [0, 1, 2]
            return input_list

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case[0])
    solution = test_case[1]
    if sorted_array == solution:
        return "Pass"
    else:
        return "Fail"

# Udacity supported test
print("------- \t Udacity supported test \t -------")
arr = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

arr = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# sorted
arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# Arbitray input
print("------- \t Arbitrary test \t -------")
# all zeros
arr = [0, 0, 0, 0, 0, 0]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# all ones
arr = [1, 1, 1, 1, 1, 1]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# all twos
arr = [2, 2, 2, 2, 2, 2]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# descending
arr = [2, 2, 1, 1, 0, 0]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# single element
arr = [0]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# two elements
arr = [2,1]
sol = sorted(arr)
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

print("------- \t Not valid input \t -------")

# None
arr = None
sol = None
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# empty
arr = []
sol = []
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))

# partially sorted
arr = [2, 0, 1, 4, 0, 6, 2, 1, 2]
sol = [0, 1, 1, 4, 0, 6, 2, 2, 2]
test = test_function([arr, sol])
print('{} \t {}'.format(sol, test))
