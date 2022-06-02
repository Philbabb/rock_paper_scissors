import random

choices = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

print("""
Starting Game
This is Rock, Paper, Scissors
Select R for Rock, P for Paper, S for Scissors
""")
computer = random.choice(list(choices))

player = input("Select R, P or S: ").upper()

while player not in choices:
    print("Input not valid")
    player = input("Select R, P or S: ").upper()
        
if player == computer:
    print("Player:(",choices[player],") : CPU (",choices[computer],")")
    print("It's a tie")
    player = input("Select R, P or S: ").upper()

elif player == "R":
    if computer == "P":
        print("Player:(",choices[player],") : CPU (",choices[computer],")")
        print("Computer Wins!")

    elif computer == "S":
        print("Player:(",choices[player],") : CPU (",choices[computer],")")
        print("You Win!")

elif player == "S":
    if computer == "R":
        print("Player:(",choices[player],") : CPU (",choices[computer],")")
        print("Computer Wins!")

    elif computer == "P":
        print("Player:(",choices[player],") : CPU (",choices[computer],")")
        print("You Win!")

elif player == "P":
    if computer == "S":
        print("Player:(",choices[player],") : CPU (",choices[computer],")")
        print("Computer Wins!")

    elif computer == "R":
        print("Player:(",choices[player],") : CPU (",choices[computer],")")
        print("You Win!")

