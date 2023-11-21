# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function Return the remainder of two number when dividing
def modules(x, y):
    return x % y


def exponential(x, y):
    return x ** y

print("Select Calculation To Perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modules")
print("6. Exponential")

while True:
    # take input from the user
    choice = input("Enter choice : ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(a, "+", b, "=", add(a, b))

        elif choice == '2':
            print(a, "-", b, "=", subtract(a, b))

        elif choice == '3':
            print(a, "*", b, "=", multiply(a, b))

        elif choice == '4':
            print(a, "/", b, "=", divide(a, b))

        elif choice == '5':
            print(a, "%", b, "=", modules(a, b))

        elif choice == '6':
            print(a, "^", b, "=", exponential(a, b))

        print("\t")
        next_calculation = input("Did You want to Continue ?? Say (yes/no): ")
        print("\t")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")