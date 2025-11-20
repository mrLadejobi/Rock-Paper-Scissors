def addition(a, b):
    return a + b

def mul_numbers(a, b):
    return a * b

def subtract_numbers(a, b):
    return a - b

def divide_numbers(a, b):
    return a // b

result = divide_numbers(20, 5)
print(result)


username = input("What is your name?")
def say_hello(username):
    return f"Hello {username}"


response = say_hello(username)
print(response)



answer = addition(202020, 303030)
print(answer)


fruits = ['apple', 'banana', 'oranges', 'watermelon', 'coconut', 'pawpaw', 'lemon', 'pineapple']

for fruit in fruits:
    print(fruit)

number = 1
for numbers in range (0, 200):
    while numbers >= 0:
        number += 1
        print(number)

