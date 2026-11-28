def reverse(n):
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** (len(str(n)) - 1)) + reverse(n // 10)


n = int(input("Enter number: "))
print(reverse(n))
