# mon tp 

number_to_find_factoriel = int(input("Enter a number to find its factorial: "))

if number_to_find_factoriel < 1 : 
    print("Please enter a positive integer.")
else : 
    while number_to_find_factoriel > 1:
        result = number_to_find_factoriel * (number_to_find_factoriel - 1)
        print("result:", result)
        break
