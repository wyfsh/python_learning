def inverse_by_math(num):
    inv = 0
    while (num > 9):
        inv = inv * 10 + num % 10
        num /= 10
    inv = inv * 10 + num % 10
    return inv


def inverse_by_string(num):
    return int(str(num)[::-1])


a, b = raw_input("Type 2 integers:").split()

sum1 = inverse_by_math(int(a)) + inverse_by_math(int(b))
print inverse_by_math(sum1)

sum2 = inverse_by_string(int(a)) + inverse_by_string(int(b))
print inverse_by_string(sum2)
