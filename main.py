#quadratic function calculator
import math
def quadratic_function():
    a = input("a = ")
    a = float(a)
    b = input("b = ")
    b = float(b)
    c = input("c = ")
    c = float(c)

    check_real_intercept = pow(b, 2) - 4 * a * c / 2 * a
    if check_real_intercept <0:
        print("No real intercept")
    else:
        x_1 = -1 * b + math.sqrt(pow(b,2) - (4 * a * c))
        x_1 = x_1 / 2 * a
        print("x = " + str(x_1))
        x_2 = -1 * b - math.sqrt(pow(b, 2) - (4 * a * c))
        x_2 = x_2 / 2 * a
        print("x = " + str(x_2))



quadratic_function()


#affirmation generator
import random

def affirmation_generator():
    value = random.randint(1,5)
    if value == 1:
        print("You are loved")
    if value == 2:
        print("You are special")
    if value == 3:
        print("You can do anything")
    if value == 4:
         print("I believe in you")
    if value == 5:
        print("You are capable")

affirmation_generator()