#Task 4 - Create a Rock, Paper, Scissors Game using Python

#importing the random module
import random

#function to determine the Winner of the Game
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice =="Scissors") or (user_choice == "Scissors" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"

#function to run the game
def play():
    user_score = 0
    computer_score = 0
    choice = ["Rock", "Paper", "Scissors"]
    print("Welcome to Codsoft's Rock-Paper-Scissors Game!!")
    print("Instruction: Please enter 'Rock', 'Paper', 'Scissors' to play the game! Enter 'quit' to exit!!\n")
    while True:
        user_choice = input("Your Choice (Rock/Paper/Scissors): ")
        if user_choice == "quit":
            print("Thanks for Playing")
            break
        elif user_choice not in choice:
            print("Invalid choice! Please enter a valid choice: ")
            continue
        computer_choice = random.choice(choice)
        print("Computer's Choice:",computer_choice)
        result = winner(user_choice, computer_choice)
        if result == "Tie":
            print("It is a Tie!\n")
        elif result == "User":
            print("You win this Round!\n")
            user_score = user_score + 1
        else:
            print("Computer wins this Round!\n")
            computer_score = computer_score + 1
        print("Current Scores - You:",user_score,"Computer:",computer_score)
        playagain = input("Do you want to play the next round (Yes/No): ")
        if playagain == "No":
            print("Final Scores - You:",user_score,"Computer:",computer_score)
            if user_score > computer_score:
                print("You win by",user_score-computer_score,"Points!!")
            elif user_score < computer_score:
                print("Computer wins by",computer_score-user_score,"Points!!")
            else:
                print("You and Computer have the Same Number of Points!!")
            print("Thanks for Playing!!")
            break

#Running the Game
play()
