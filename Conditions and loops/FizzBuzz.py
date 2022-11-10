print("Welcome to fizzbuzz game!")
num = int(input("Enter custom number from 1 to 100:"))

for var in range (1, num + 1):
    if var % 3 == 0 and var % 5 == 0:
        print("fizzbuzz")
    elif var % 3 == 0:
        print("fizz")
    elif var % 5 == 0:
        print("buzz")
    else:
        print(var)
