def square(x):
    running_total = 0
    for i in range(x):
        running_total = running_total + x

    return running_total


num = 10
result = square(num)

print("The square root of {} is {}.".format(num, result))
