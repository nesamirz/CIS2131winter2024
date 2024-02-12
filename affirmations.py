import random
import math

def affirmation_generator():
    """
    Generates a random value between 1 and 5 and prints a corresponding affirmation.
    """
    random_value = random.randint(1, 5)
    if random_value == 1:
        print("You are enough!")
    elif random_value == 2:
        print("Become the best version of yourself!")
    elif random_value == 3:
        print("The only person you need to believe in you is you!")
    elif random_value == 4:
        print("You've got this!")
    else:
        print("With hardship there is ease!")

def quadratic_equation_intercept_finder(a, b, c):
    """
    Finds the x intercepts of a quadratic equation of the form ax^2 + bx + c = 0.
    Returns the x intercepts or a message saying they don't exist.
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No intercepts found."
    else:
        first_x_intercept = (-b + math.sqrt(discriminant)) / (2*a)
        second_x_intercept = (-b - math.sqrt(discriminant)) / (2*a)
        return (first_x_intercept, second_x_intercept)

# Example usage
print("Affirmation:")
affirmation_generator()

print("\nQuadratic Equation Intercept Finder:")
print(quadratic_equation_intercept_finder(1, -3, 2))
print(quadratic_equation_intercept_finder(1, -2, 5))