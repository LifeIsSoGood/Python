import random

print("Ok, Let's start.\n")

name = input("Please enter your name: ")
print("Hello", name + "!")

number = int(input("Please enter the number I'm thinking: "))

screct = random.randint(1,9)

while number != screct:
    if number < screct:
        print("Too small")       
    else:
        print("Too big")
    number = int(input("Please enter the number again: "))
print("Congratulations! You got it!")
print("Game over!")
