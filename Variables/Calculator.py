x = int(input("Number 1: "))
operator = input("(+, -, *, /): ")
y = int(input("Number 2: "))



if operator == "*":
    print(x * y)

elif operator == "/":
    print(x / y)

elif operator == "+":
    print(x + y)

elif operator == "-":
    print(x - y)

else:

    print("the calculator does not support this function")


