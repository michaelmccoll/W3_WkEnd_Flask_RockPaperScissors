from flask import render_template, request, redirect
from app import app
from app.model.game import game_result
from app.model.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Welcome Page')

@app.route('/<player1>/<player2>')
def show_game_result(player1,player2):
    player1_choice = player1
    player2_choice = player2
    return game_result(player1_choice,player2_choice)