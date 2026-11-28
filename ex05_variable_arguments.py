def maximum(*numbers):
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


print(maximum(12, 5, 20, 8, 3))
print(maximum(4, 9, 15, 2))
print(maximum(100, 45, 67, 89, 12, 34))