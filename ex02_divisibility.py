def div(a, b):
    if b != 0:
        if a % b == 0:
            return True
        else:
            return False
    else:
        return "Error!"


n = True
while n:
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    print(div(a, b))
    q = input("Continue? [y/n]: ")
    if q == 'y':
        n = True
    else:
        n = False
