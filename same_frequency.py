def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_sorted = sorted(str(num1))
    num2_sorted = sorted(str(num2))

    if len(num1_sorted) != len(num2_sorted):
        return False

    for i in range(len(num1_sorted)):
        if num1_sorted[i] != num2_sorted[i]:
            return False

    return True