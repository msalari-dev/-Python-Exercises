def max_of_three(a, b, c):
    m = a
    if m < b:
        m = b
    if m < c:
        m = c

    return m


a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))

print("\nmax number is: ", max_of_three(a, b, c))
