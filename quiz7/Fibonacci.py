def Fibonacci(n):
    if n == 1:
        return 1  # F_1 = 1
    if n == 2:
        return 1  # F_2 = 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)  # F_n = F_(n-1) + F_(n-2) when n >= 3


for i in range(1, 11):
    print(Fibonacci(i))
