def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    last = prev_digit
    rest = num
    if rest < 10:
        return rest == prev_digit
    return int(prev_digit == rest % 10 or rest % 10 == ((rest // 10) % 10)) + neighbor_digits(rest // 10, rest % 10)


