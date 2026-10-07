#import packages
import os

from random import randint

#initialize
num1=0
num2=0
add=0
subs=0
mult=0
div=0
opt=0

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

if opt==1:
    print(f"\nAddition is: {num1+num2}")
elif opt==2:
    print(f"Subtraction is: {num1-num2}")
elif opt==3:
    print(f"Multiplication is: {num1*num2}")
elif opt==4:
    print(f"Division is: {num1/num2}")
elif opt==5:
    print(f"\nADD: {num1+num2}\nSUBS: {num1-num2}\nMULT is: {num1*num2}\nDIV is: {num1/num2}")
else:
    print("Try again. Invalid option")
