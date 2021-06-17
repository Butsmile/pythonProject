def star():
    for x in range(-30, 30, 1):
        for y in range(-30, 30, 1):
            if x * 2 + y == 6:
                print('+', end='')
            else:
                print('-', end='')
        print()

#run field
star()


