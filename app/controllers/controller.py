from flask import render_template, request, redirect
from app import app
from app.model.game import Game, game_result
from app.model.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Welcome Page')

@app.route('/<player1>/<player2>')
def show_game_result(player1,player2):
    player1_choice = player1
    player2_choice = player2
    outcome = game_result(player1_choice,player2_choice)
    return render_template('game_result.html', title='Game Result', outcome = outcome)

@app.route('/play')
def show_game_result_vs_pc():
    # name_of_player = request.form['player_name']
    # choice_of_player = request.form['player_choice']
    # play_pc = Game(name_of_player,choice_of_player)
    # outcome_vs_pc = game_result_vs_pc(play_pc) 
    return render_template('play.html')
    
