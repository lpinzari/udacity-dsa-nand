# Problem Statement
# You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.
#
# Example 1:
#
# input = [1, 2, 3]
# output = [1, 2, 4]
# Example 2:
#
# input = [9, 9, 9]
# output = [1, 0, 0, 0]

def list_to_string(input_list: list) -> str:
    string = str()
    for i in input_list:
        string += str(i)
    return string


def string_add_one(string: str) -> str:
    number = int(string)
    number += 1
    return str(number)


def string_to_list(string: str) -> list:
    return [int(char) for char in string]


def add_one(input_list: list) -> list:
    return string_to_list(string_add_one(list_to_string(input_list)))

#%% Test zone

a = [1,1,2,3]
test = add_one(a)
print(test)
