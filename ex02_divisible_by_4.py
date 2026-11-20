divisible = ""
count = 0

for i in range(10):
    n = int(input("Enter your number: "))
    if n % 4 == 0:
        if count == 0:
            divisible += str(n)
        else:
            divisible += "," + str(n)
        count += 1

print("count:", count, "divisible:", divisible)

