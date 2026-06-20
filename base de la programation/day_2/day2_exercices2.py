def add( a, b):
    return a + b

def multiply( a, b):
    return a * b

def divide( a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

def subtract( a, b):
    return a - b


while True : 
    print ("\nMenu:")
    print ("1. Add")
    print ("2. Multiply")
    print ("3. Divide")
    print ("4. Subtract")
    print ("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "5":
        print("Exiting the calculator.")
        break
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", multiply(num1, num2))
    elif choice == "3":
        print("Result:", divide(num1, num2))
    elif choice == "4":
        print("Result:", subtract(num1, num2))
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")