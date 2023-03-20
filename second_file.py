import os 
import sys

#Add these lines of code (and anything else you like)
print(sys.path)
help("modules")
days_of_the_week = 7
def say_hello(recipient):
    print("Hello, world! Hello {} ".format(recipient))
    return recipient