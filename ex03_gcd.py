def gcd(a, b):
    if a < b:
        a, b = b, a

    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


a = int(input("Enter number1: "))
b = int(input("Enter number2: "))

print(gcd(a, b))