'''The code for the web app'''

from flask import Flask
from flask_login import LoginManager

import game

app = Flask(__name__)

login_manager = LoginManager()

@app.route('/play/manual')
def manual_play():
    return game.run_game(world_controls='manual')

@app.route('/play/script')
def script_play():
    return game.run_game(world_controls='script')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
