def Add(n):
    Sum = 0
    for digit in str(n):
        Sum += int(digit)
    return Sum