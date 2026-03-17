import random 


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']


def password_generator(length,use_digits,use_symbols):
    characters = []
    characters = letters.copy()
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password


print("----PASSWORD GENERATOR---")
length = int(input("Enter length of password:"))
use_digits = input("Do you want digits:(y/n)").lower() == "y"
use_symbols = input("Do you want symbols:(y/n)").lower() == "y"
passw = password_generator(length,use_digits,use_symbols)
print("password generated :", passw)

