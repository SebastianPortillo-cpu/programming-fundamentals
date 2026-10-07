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
    add=num1+num2
    print(f"Addition is: {add}")

if opt==2:
    subs=num1-num2
    print(f"Substraction is: {subs}")
   
if opt==3:
    mult=num1*num2
    print(f"Multiplication is: {mult}")

if opt==4:
    div=num1/num2
    print(f"Division is: {div}")

if opt==5:
    add=num1+num2
    subs=num1-num2
    mult=num1*num2
    div=num1/num2 
    print(f"\nAddition is: {add}\nSubstraction is: {subs}\nMultiplication is: {mult}\nDision is: {div}\n")    

if opt<1 or opt>5:
    print(f"Invalid option.Try again")
