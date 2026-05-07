def is_valid_triangle(sides):
    side_one, side_two, side_three = sides

    return (
        side_one > 0 and side_two > 0 and side_three > 0 and
        side_one + side_two >= side_three and
        side_one + side_three >= side_two and
        side_two + side_three >= side_one
    )


def equilateral(sides):
    if not is_valid_triangle(sides):
        return False

    side_one, side_two, side_three = sides
    return side_one == side_two == side_three


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False

    side_one, side_two, side_three = sides
    return (
        side_one == side_two or
        side_one == side_three or
        side_two == side_three
    )


def scalene(sides):
    if not is_valid_triangle(sides):
        return False

    side_one, side_two, side_three = sides
    return (
        side_one != side_two and
        side_two != side_three and
        side_one != side_three
    )