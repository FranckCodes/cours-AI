def check_number(number):
    if number > 0 : 
        if number % 2 == 0 :
            return "the number is positive and even."
        else:
            return "the number is positive and odd."
    else:
        return "The number is not positive"
    
    
#check number even or odd

number_to_check = int(input("Enter a number: ") )

    

def print_result (n):
    result = check_number(n)
    print(f"The number {n} is {result}")
    
    
print_result(number_to_check)