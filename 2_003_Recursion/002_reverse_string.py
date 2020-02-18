def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    # TODO: Write your recursive string reverser solution here

    if len(input) <= 1:
        return input
    else:
        return reverse_string(input[1:]) + input[0]

print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
