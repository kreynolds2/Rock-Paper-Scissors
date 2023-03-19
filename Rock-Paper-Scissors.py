import random

def rps_round():
    player1 = input("Rock, Paper, or Scissors? ").lower()
    player2 = random.choice(["Rock", "Paper", "Scissors"]).lower()
    print("Janken!: ", player2)
    winner = determine_winner(player1, player2)
    if winner == "You tied":
        print("TIE, AGAIN!")
        rps_round()
    else:
        print(f'Winner is {winner}')
        play_again()

def determine_winner(player1_move, player2_move):
    if (player1_move == "rock" and player2_move == "scissors") or \
        (player1_move == "paper" and player2_move == "rock") or \
        (player1_move == "scissors" and player2_move == "paper"):
        return "Player 1"
    elif player1_move == player2_move:
        return "You tied"
    elif (player2_move == "rock" and player1_move == "scissors") or \
        (player2_move == "paper" and player1_move == "rock") or \
        (player2_move == "scissors" and player1_move == "paper"):
        return "Player 2"
    else: 
        print("Please input rock paper or scissors")
        rps_round()

def play_again():
    play_again_input = input("Play Again? press Y or N ").lower()
    if play_again_input == ("y"):
        rps_round()
    else:
        print("RIP")

rps_round()