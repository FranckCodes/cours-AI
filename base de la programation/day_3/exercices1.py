def factorial (n): 
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    


def print_factorial (n):
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
    
    
number_to_find_factoriel  = int(input("Enter a number to find its factorial: "))    
print_factorial(number_to_find_factoriel)