# Problem Statement
# Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.
#
# For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].

def nth_row_pascal(n):
    if n == 0:
        return [1]
    current_row = [1]
    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            next_number = previous_row[j] + previous_row[j - 1]
            current_row.append(next_number)
        current_row.append(1)
    return current_row

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")

n = 0
solution = [1]


test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)
