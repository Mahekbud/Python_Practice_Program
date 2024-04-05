num = 5
factorial = 1
if num < 0:
    print("Factorial is not ")
elif num == 0:
    print(" factorial ")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("factorial : " ,factorial)