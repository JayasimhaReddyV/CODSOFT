#Task 3 - Creating a Random Password Generator using Python
#Importing the random and string modules
import string
import random

#Function to generate a password based on Length and Complexity specified by The User
def generator(length,complexity):
    if complexity == 'Simple':
        Characters = string.ascii_lowercase + string.digits
    elif complexity == 'Intermediate':
        Characters = string.ascii_letters + string.digits
    elif complexity == 'Strong':
        Characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid Choice of Complexity!! Please choose 'Simple', 'Intermediate' or 'Strong'.")
    password = ''.join(random.choice(Characters) for i in range(length))
    return password

#Main function to drive the base code
def main():
    while True:
        try:
            print("Welcome to the Password Generator Application!!")
            Length = int(input("Enter the Desired Length of Password to be Generated: "))
            Complexity = input("Enter the Desired Complexity for the Password ('Simple', 'Intermediate', 'Strong'): ")
            Password = generator(Length,Complexity)
            print("The Password Generated is: ",Password,"\n")
        except ValueError:
            print("Invalid Input!! Please enter a number for Desired Length!!")

if __name__ == "__main__":
    main()