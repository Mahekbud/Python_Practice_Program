dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def present(key):
    if key in dict.keys():
        return True
    else:
        return False

print(present(5))
print(present(9))