# Write a function is_even that will return true if the passed in number is even.

def is_even(value):
    return int(value) % 2 == 0

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num):
    print("Even!")
else:
    print("Odd")