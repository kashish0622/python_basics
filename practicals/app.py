from flask import Flask, render_template, request
import random
app = Flask(__name__)
print("Number guessing game")
user = str(input("Enter your name: "))
print("Hello", user)
num = 96
guess = int(input("Enter number: "))
while guess != num:
    if guess > num:
       print('''You entered a higher number.
    Try again!!''')
    else:
       print('''You entered a lower number.
          Try again!!''')
    guess = int(input("Enter the number again: "))
    print("Congratulation!Your guess is correct this time.")