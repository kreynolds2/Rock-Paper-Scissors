import random

player1 = input("Rock, Paper, or Scissors? ").lower()
player2 = random.choice(["Rock", "Paper", "Scissors"]).lower()
print("Janken!: ", player2)

if player1 == "rock" and player2 == "scissors":
    print("You Won!")
elif player1 == "paper" and player2 == "rock":
    print("You Won!")
elif player1 == "scissors" and player2 == "paper":
    print("You Won!")
elif player1 == player2:
    print("You tied")
else:
    print("pathetic")