a = float(input("Enter your a: "))

if a != 0:
    b = float(input("Enter your b: "))
    c = float(input("Enter your c: "))
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + delta ** 0.5) / (2*a)
        root2 = (-b - delta ** 0.5) / (2*a)
        print("root1: ", root1, "root2: ", root2)
    elif delta == 0:
        root0 = -b / (2 * a)
        print("root: ", root0)
    else:
        print("It has no real roots.")
else:
    print("a cannot be zero.")
