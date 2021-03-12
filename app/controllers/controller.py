from flask import render_template, request, redirect
from app import app
from app.model.player import Player

@app.route('/<player1>/<player2>')
def index(player1,player2):
    return render_template('index.html', title='Welcome Page', player1=player1, player2=player2)

# @app.route('/<player1>/<player2>')
# def index():
#     player1_choice = player1
#     player2_choice = player2
#     return render_template('index.html', title='Welcome Page', player1=player1, player2=player2)

# @app.route('/events', methods=['POST'])
# def create_event():
#     eventName = request.form['event_name']
#     eventDate = request.form['date']
#     newEvent = Event(eventDate, eventName, eventGuests, eventRoom, eventDesc,eventRecurring)
#     create_new_event(newEvent) 
#     return redirect('/events')