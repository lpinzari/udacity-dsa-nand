import math

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Null input
    if number is None:
        return None

    # Negative input
    if number < 0:
        return -1

    # Base cases:
    if (number == 0 or number == 1):
        return number

    # Do Binary search for floor(sqrt(number))
    lower_bound = 0
    upper_bound = number // 2

    while lower_bound <= upper_bound:

        middle = (lower_bound + upper_bound) // 2
        middle_squared = middle * middle

        # if num is a perfect square (we have found the element)
        if middle_squared == number:
            return middle

        # since we are rounding below we need to update middle
        # when middle_squared is smaller than number move closer to sqrt(num) from left
        if middle_squared < number:
            lower_bound = middle + 1
            guess = middle
        else: # middle_squared is greater than number move closer to sqrt(num) from right
            upper_bound = middle -1

    return guess


# Test Exception cases: Not valid input
print("----------- \t Exception cases: Not valid input \t -------")
print ('sqrt(None): {} Pass'.format(sqrt(None)) if  (None == sqrt(None)) else "Fail")
print ('sqrt(-10): {} \t Pass'.format(sqrt(-10)) if  (-1 == sqrt(-10)) else "Fail")


# Test Base cases
print("----------- \t Base cases \t -------")
print ('  sqrt(0):  {} \t Pass'.format(sqrt(0)) if  (0 == sqrt(0)) else "Fail")
print ('  sqrt(1):  {} \t Pass'.format(sqrt(1)) if  (1 == sqrt(1)) else "Fail")

# Test arbitrary perfect square numbers
print("----------- \t Arbitrary perfect square numbers \t -------")
print ('  sqrt(9):  {} \t Pass'.format(sqrt(9)) if  (3 == sqrt(9)) else "Fail")
print (' sqrt(16):  {} \t Pass'.format(sqrt(16)) if  (4 == sqrt(16)) else "Fail")

# Test arbitrary no perfect square numbers
print("----------- \t Arbitrary No perfect square numbers \t -------")
print (' sqrt(14):  {} \t Pass'.format(sqrt(14)) if  (math.floor(math.sqrt(14)) == sqrt(14)) else "Fail")
print (' sqrt(18):  {} \t Pass'.format(sqrt(18)) if  (math.floor(math.sqrt(18)) == sqrt(18)) else "Fail")
# Test  arbitray Large perfect square numbers
print("----------- \t Arbitrary Large perfect square numbers \t -------")
print (' sqrt(10000000000):  {} \t Pass'.format(sqrt(10000000000)) if  (100000 == sqrt(10000000000)) else "Fail")
# Test  arbitrary Large No perfect square numbers
print("----------- \t Arbitrary Large No perfect square numbers \t -------")
print (' sqrt(10995599679):  {} \t Pass'.format(sqrt(10995599679)) if  (math.floor(math.sqrt(10995599679)) == sqrt(10995599679)) else "Fail")
