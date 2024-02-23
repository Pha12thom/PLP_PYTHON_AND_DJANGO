"""
Create a new Python file and name it "user_input.py"
Use the input() function to ask the user for their name and store it in a variable called "name".
Use the input() function to ask the user for their age and store it in a variable called "age".
Use the input() function to ask the user for their location and store it in a variable called "location".
Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
Save and run the program to see the output.

"""

name, age, location = input("what is your name?"), int(input("what is your age? ")), input("whats your location?")
print(f"My name is {name}, i am  {age} old i live in  {location}")