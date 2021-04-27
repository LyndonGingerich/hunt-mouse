'''The code for the web app'''

from flask import Flask

import game

app = Flask(__name__)

@app.route('/play/manual')
def manual_play():
    return game.run_game(world_controls='manual')

@app.route('/play/script')
def script_play():
    return game.run_game(world_controls='script')
