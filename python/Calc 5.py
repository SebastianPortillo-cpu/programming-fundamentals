#import packages
import os

from random import randint

os.system("Clear")
print("LOADING BASIC CALC V.2.0...\n")

#Get data

num1= randint (-100,100)
num2= randint (-100,100)

#Display generated number

print(f"Number 1: {num1}")
print(f"Number 2: {num2}\n")

#Display MainMenu

print("          MAIN MENU\n")
print("[1].Addition\n[2].Substrction\n[3].Multiplication\n[4].Division\n[5].All operations\n")

opt = int(input("Please,press any option [1-5]: "))

match opt:
    case 1:
        print(f"Adittion is: {num1+num2}")
    case 2:
        print(f"Substraction is: {num1-num2}")
    case 3:
        print(f"Multiplication is: {num1*num2}")
    case 4:
        print(f"Division is: {num1/num2}")
    case 5:
        print(f"\nADD is: {num1+num2}\nSUBS is: {num1-num2}\nMULT is: {num1*num2}\nDIV is: {num1/num2}")
    case _:
        print("Error")
              
