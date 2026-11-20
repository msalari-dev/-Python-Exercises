total = 0
n = int(input("Enter your number: "))

while n != 0:
    total += n ** 3
    n = int(input("Enter your number: "))

print("Sum of cubes: ", total)
