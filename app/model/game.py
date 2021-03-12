from app.model.player import *

def game_result(player1_choice,player2_choice):
    if player1_choice == player2_choice:
        return f"Its a DRAW!!!!"
    elif player1_choice == "rock" and player2_choice == "scissors":
        return f"Player 1 WINS, {player1_choice} beats {player2_choice}"
    elif player1_choice == "rock" and player2_choice == "paper":
        return f"Player 2 WINS, {player2_choice} beats {player1_choice}"
    elif player1_choice == "paper" and player2_choice == "rock":
        return f"Player 1 WINS, {player1_choice} beats {player1_choice}"
    elif player1_choice == "paper" and player2_choice == "scissors":
        return f"Player 2 WINS, {player2_choice} beats {player1_choice}"
    elif player1_choice == "scissors" and player2_choice == "paper":
        return f"Player 1 WINS, {player1_choice} beats {player1_choice}"
    elif player1_choice == "scissors" and player2_choice == "rock":
        return f"Player 2 WINS, {player2_choice} beats {player1_choice}"
    else: return f"Please type only type rock, paper or scissors"