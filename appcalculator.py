print("Welcome to the calculator app and we are gladly waiting for your request")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = input("Enter your option (1/2/3/4): ")

if option in ('1', '2', '3', '4'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if option == '1':
        print("The sum is:", num1 + num2)
    elif option == '2':
        print("The difference is:", num1 - num2)
    elif option == '3':
        print("The product is:", num1 * num2)
    elif option == '4':
        if num2 != 0:
            print("The division is:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid option selected.")
