def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num, odd_sum):
    # Duplicate the loop1 function using recursion
    if num <= 20:
        if (num % 2) == 1:
            odd_sum += num
        num += 1
        return loop1Rec(num, odd_sum)
    else:
        return odd_sum

def loop2Rec(num, even_sum):
    # Duplicate the loop2 function using recursion
    if num < 20:
        if (num % 2) == 0:
            even_sum += num
        num += 1
        return loop2Rec(num, even_sum)
    else:
        return even_sum


print(f"Sum of odds between 1 and 20 using 'for' loop = {loop1()}")
print(f"Sum of odds between 1 and 20 using recursion = {loop1Rec(0, 0)}")
print(f"Sum of evens between 1 and 20 using 'while' loop = {loop2()}")
print(f"Sum of evens between 1 and 20 using recursion = {loop2Rec(0, 0)}")
