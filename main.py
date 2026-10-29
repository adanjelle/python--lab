from utils import square, is_even, celsius_to_fahrenheit, greet

name = input("Enter your name: ")
print(greet(name))

number = int(input("Enter a number: "))

print("Square:", square(number))
print("Even or odd:", "Even" if is_even(number) else "Odd")
print("Fahrenheit:", celsius_to_fahrenheit(number))
