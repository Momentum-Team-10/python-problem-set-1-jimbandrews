# 1. Set the variable `given_name` to the string "Addison".
given_name = "Addison"

# ------------------------------------------------------------------------------
# 2. You have 20 candies that you must divide equally among 6 people. How many candies will be left over?
# Set variables for `candies`, `people`, `left_over` to make your tests pass.
candies = 20
people = 6
left_over = candies % people

# ------------------------------------------------------------------------------
# 3. Create a function called `greeting` that returns "Hello, <name>!",
# where <name> is the name given as an argument to the function.
def greeting(name):
    return f"Hello, {name}!"

# ------------------------------------------------------------------------------
# 4. Create a function called `is_odd` that, given a number, will
# return true if the number is odd and false if it is not. An odd number is a
# number which, when divided by 2, has a remainder of 1 or -1.
def is_odd(number):
    if abs(number % 2) == 1:
        return True
    else:
        return False

# ------------------------------------------------------------------------------
# 5. Create a function called `is_even` that, given a number, will
# return true if the number is even and false if it is not. An even number is a
# number which, when divided by 2, has a remainder of 0.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# ------------------------------------------------------------------------------
# 6. Create a function called `fahrenheit_to_celsius` that takes a
# Fahrenheit temperature as an argument and returns the
# temperature in Celsius.
def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5 / 9)

# ------------------------------------------------------------------------------
# 7. Create a function called `celsius_to_fahrenheit` that takes a
# Celsius temperature as an argument and returns the
# temperature in Fahrenheit.
def celsius_to_fahrenheit(temp):
    return temp * (9 / 5) + 32

# ------------------------------------------------------------------------------
# 8. Create a function called `fahrenheit_to_kelvin` that takes a
# Fahrenheit temperature as an argument and returns the
# temperature in Kelvin. This function must use your previous
# fahrenheit_to_celsius function.
# Absolute zero (0 K) is equivalent to −273.15 C.
# 1 degree Kelvin equals 1 degree Celsius.
def fahrenheit_to_kelvin(temp):
    return fahrenheit_to_celsius(temp) + 273.15

# ------------------------------------------------------------------------------
# 9. Create a function called `lesser` that takes two numbers as
# arguments and returns the lesser of them. This function should
# use an if/else statement.
def lesser(a, b):
    if a < b:
        return a
    else:
        return b

# ------------------------------------------------------------------------------
# 10. Create a function called `multigreeting` that takes a name
# and a language code and returns a version of "Hello, <name>!"
# in the specified language. The supported languages and their
# translations are below.
#
# en - Hello, <name>!
# es - ¡Hola, <name>!
# fr - Bonjour, <name>!
# eo - Saluton, <name>!
#
# If any other language code is used, return nothing.
def multigreeting(name, lang):
    if lang == "en":
        return f"Hello, {name}!"
    elif lang == "es":
        return f"¡Hola, {name}!"
    elif lang == "fr":
        return f"Bonjour, {name}!"
    elif lang == "eo":
        return f"Saluton, {name}!"
    else:
        return

# ------------------------------------------------------------------------------
# 11. The greatest common divisor (https://en.wikipedia.org/wiki/Greatest_common_divisor)
# is the largest integer that, given two other integers, can be divided into them. For
# example, the greatest common divisor of 24 and 81 is 3. The greatest common divisor of
# 10 and 25 is 5.
#
# One method of calculating the greatest common divisor is the "binary GCD algorithm."
# (https://en.wikipedia.org/wiki/Greatest_common_divisor#Binary_GCD_algorithm)
# It can be written out like the following:
#
# Input: a, b positive integers
# Output: The greatest common divisor, which is g * 2**d
# d = 0
# while a and b are both even
#     a = a/2
#     b = b/2
#     d = d + 1
# while a != b
#     if a is even then a = a/2
#     else if b is even then b = b/2
#     else if a > b then a = (a – b)/2
#     else b = (b – a)/2
# g = a
# output g * 2**d

# Write a function called `gcd` that takes two arguments and returns the greatest
# common divisor using the instructions above.
def gcd(a, b):
    d = 0
    while is_even(a) and is_even(b):
        a = a/2
        b = b/2
        d += 1
    while a != b:
        if is_even(a):
            a = a/2
        elif is_even(b):
            b = b/2
        elif a > b:
            a = (a-b)/2
        else:
            b = (b-a)/2
    g = a
    return g * 2**d