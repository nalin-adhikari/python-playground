def find_factorial(num):

    if num == 1:
        return num
    else:
        return num * find_factorial(num-1)

print(find_factorial(998))