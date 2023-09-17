
def is_even(number):
    """
    This function tells if a given number is odd or even
    Input-any valid integer
    output-odd/even
    Created By-Zain
    Last edited-10 july 2023
    
    """
    if type(number)== int:
        if number%2 ==0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Not allow"