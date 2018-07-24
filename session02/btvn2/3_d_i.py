for row in range(1, 10):
    for col in range(1,10):
        if (row + col) % 2 == 0:
            print('{:3}'.format(1), end="")
        else:
            print('{:3}'.format(0), end="")
    print()        

    