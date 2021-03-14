from app.model.player import *
from random import choice

class Game():
    def __init__(self, name_of_player,choice_of_player):
        self.name_of_player = name_of_player
        self.choice_of_player = choice_of_player

def game_result(player1_choice,player2_choice):
    if player1_choice == "rock" and player2_choice =="rock":
        return f"Its a DRAW!!!!"
    if player1_choice == "paper" and player2_choice =="paper":
        return f"Its a DRAW!!!!"
    if player1_choice == "scissors" and player2_choice =="scissors":
        return f"Its a DRAW!!!!"
    elif player1_choice == "rock" and player2_choice == "scissors":
        return f"Player 1 WINS, {player1_choice} beats {player2_choice}"
    elif player1_choice == "rock" and player2_choice == "paper":
        return f"Player 2 WINS, {player2_choice} beats {player1_choice}"
    elif player1_choice == "paper" and player2_choice == "rock":
        return f"Player 1 WINS, {player1_choice} beats {player2_choice}"
    elif player1_choice == "paper" and player2_choice == "scissors":
        return f"Player 2 WINS, {player2_choice} beats {player1_choice}"
    elif player1_choice == "scissors" and player2_choice == "paper":
        return f"Player 1 WINS, {player1_choice} beats {player2_choice}"
    elif player1_choice == "scissors" and player2_choice == "rock":
        return f"Player 2 WINS, {player2_choice} beats {player1_choice}"
    else: return f"Please type only type rock, paper or scissors"

def game_result_vs_pc(name_of_player,choice_of_player):
    pc_choice = choice(["rock","paper","scissors"])
    if choice_of_player == "rock" and pc_choice =="rock":
        return f"Its a DRAW!!!!"
    if choice_of_player == "paper" and pc_choice =="paper":
        return f"Its a DRAW!!!!"
    if choice_of_player == "scissors" and pc_choice =="scissors":
        return f"Its a DRAW!!!!"
    elif choice_of_player == "rock" and pc_choice == "scissors":
        return f"Player 1 WINS, {choice_of_player} beats {pc_choice}"
    elif choice_of_player == "rock" and pc_choice == "paper":
        return f"Player 2 WINS, {pc_choice} beats {choice_of_player}"
    elif choice_of_player == "paper" and pc_choice == "rock":
        return f"Player 1 WINS, {choice_of_player} beats {pc_choice}"
    elif choice_of_player == "paper" and pc_choice == "scissors":
        return f"Player 2 WINS, {pc_choice} beats {choice_of_player}"
    elif choice_of_player == "scissors" and pc_choice == "paper":
        return f"Player 1 WINS, {choice_of_player} beats {pc_choice}"
    elif choice_of_player == "scissors" and pc_choice == "rock":
        return f"Player 2 WINS, {pc_choice} beats {choice_of_player}"
    else: return f"Please type only type rock, paper or scissors"