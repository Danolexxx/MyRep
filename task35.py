fib1 = 1
fib2 = 1
n = input()
i = 0
while i < (int(n) - 2):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
print(fib2)