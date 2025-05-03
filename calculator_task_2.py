print("Welcome to the Simple Calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose an operation please:")
print("Add (+)")
print("Subtract (-)")
print("Multiply (*)")
print("Divide (/)")
choice = input("Enter the number of the operation (1/2/3/4): ")
if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error")
else:
    print("Invalid")
