'''The code for the web app'''

from flask import Flask

import game

app = Flask(__name__)

@app.route('/play/manual')
def manual_play():
    return game.run_game(world_controls='manual')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
