from flask import render_template, request, redirect
from app import app
from app.model.player import Player

# @app.route('/events')
# def index():
#     return render_template('index.html', title='Events', events=events_list)

# @app.route('/events', methods=['POST'])
# def create_event():
#     eventName = request.form['event_name']
#     eventDate = request.form['date']
#     newEvent = Event(eventDate, eventName, eventGuests, eventRoom, eventDesc,eventRecurring)
#     create_new_event(newEvent) 
#     return redirect('/events')