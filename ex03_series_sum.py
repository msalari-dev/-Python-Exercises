n = int(input("Enter number[0 < number < 10]: "))
if 0 < n < 10:
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += 1 / fact
    print(total)
else:
    print("invalid number!")

