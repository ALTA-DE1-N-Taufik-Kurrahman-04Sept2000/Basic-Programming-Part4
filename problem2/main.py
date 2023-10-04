def draw_xyz(N):
    pattern = ""
    count = 1

    for i in range(1, N + 1):
        line = ""
        for j in range(1, N + 1):
            if count % 3 == 0:
                line += " X"
            elif count % 2 == 0:
                line += " Z"
            elif count % 2 == 1:
                line += " Y"
            count += 1
        pattern += line.strip() + " \n"

    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """