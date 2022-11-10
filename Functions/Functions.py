def say_hello(name):
    return "Hello {0}!".format(name)


def main():
    hello_nina = say_hello(name="Nina")
    print(hello_nina)

    if __name__ == "__main__":
        main()


def calculate_sum(num1, num2):
    result = num1 + num2
    return result


def step_counter(distance_walked, lenght):
    steps_made = float(distance_walked / lenght)
    return steps_made


def absolute(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


def get_cube(num1, num2, num3):
    cube = float(num1*num2*num3)
    return cube


def get_cube_square(num1, num2, num3):
    square = float(num1*num2)
    cube = float(num1*num2*num3)
    return square, cube
