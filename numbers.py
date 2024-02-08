def promptNum():
    print("\nEnter any number [666 to exit]:\t")
    return int(input())

num = promptNum()
while num != 666:
    if num > 0:
        print("Positive")
        num = promptNum()
        if num == 666:
            break
    elif num < 0:
        print("Negative")
        num = promptNum()
        if num == 666:
            break
    else:
        print("Zero")
        num = promptNum()
        if num == 666:
            break