def equilateral(sides):
    if (sides[0] == sides[1]) and (sides[0] == sides[2]):
        return True
    return False


def isosceles(sides):
    if (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]):
        return True
    return False


def scalene(sides):
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return False
    return True


if __name__ == "__main__":
    sides = [0, 0, 0]
    print(equilateral(sides))
