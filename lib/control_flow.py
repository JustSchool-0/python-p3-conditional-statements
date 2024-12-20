#!/usr/bin/env python3

def admin_login(username, password):
    if (username.lower() == "admin" and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if (temperature < 40):
        return "It's brisk out there!"
    elif (temperature < 66):
        return "It's a little chilly out there!"
    elif (temperature > 85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    of3 = num % 3 == 0
    of5 = num % 5 == 0
    if (of3 and of5):
        return "FizzBuzz"
    elif (of3):
        return "Fizz"
    elif (of5):
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    if (operation == "+"):
        return num1 + num2
    elif (operation == "-"):
        return num1 - num2
    elif (operation == "*"):
        return num1 * num2
    elif (operation == "/"):
        return num1 / num2
    else:
        print("Invalid operation!")
        return None