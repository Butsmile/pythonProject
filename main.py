def star():
    for y in range(20, -20, -1):
        for x in range(-20, 20, 1):
            if x ** 2 + (y ** 2) * 4.14 <= 49:
                print('*', end='')
            else:
                print(' ', end='')
        print()

#run field
star()


