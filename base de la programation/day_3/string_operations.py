#count voyelles 

voyelles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def count_voyelles(string):
    count = 0
    for char in string:
        if char in voyelles:
            count += 1
    print(f"les voyelles dans {string} sont : {count}")


def reverse_string(string):
    print(f"la chaîne inversée de {string} est : {string[::-1]}")
    return string[::-1] #ça me permet d'inverser une chaine de caractères 


def check_palindromes(string): 
    result = reverse_string(string)
    print(string, result)
    if string == result:
        print(f"la chaîne {string} est-elle un palindrome ? : Oui")
    else: 
        print(f"la chaîne {string} n'est pas un palindrome.")    