n = int(raw_input("Type an integer n (<= 100):"))

last3 = 1
for i in range(1, n + 1):
    last3 *= i
    while (last3 % 10 == 0):
        last3 /= 10
    last3 %= 1000
last1 = last3 % 10

print last1
