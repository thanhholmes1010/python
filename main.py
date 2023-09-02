# atcoder 308
def check():
    array = [125, 175, 250, 300, 400, 525, 600, 650]
    for i in range(0, 7):
        if (array[i] <= array[i + 1]) and (array[i] >= 100) and (array[i] <= 650) and (array[i] % 25 == 0):
            pass
        else:
            print("No")
            return
    print("Yes")
check()
