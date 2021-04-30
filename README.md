# gridmaus

Turn-based dimensional search game guided solely by a display of velocity relative to the goal

## Gameplay

You will begin at the center of the "game world", or the setting for this particular iteration of the game, in every dimension.

### Demo mode

Run the game normally. Add details using the shell as requested.

Explanation of messages:

* "Length of game world": Changes the number of units in any particular dimension
* "Number of dimensions of game world": Changes the number of dimensions through which the player must navigate
* "Coordinates": Displays your Cartesian coordinates within the game world
* "Current velocity": Basically a numerical display of "hotter or colder". Positive results indicate that you are moving toward the goal. Use this as a guide; when playing by script, you will receive only the current velocity back from the game.
* "Movement in dimension X": Adds input to your coordinate in that dimension.
* "Pow! The mouse runs into a wall!": You tried to move beyond the limits of the game world. The game kept you from doing so.

### Regular play (by script)

Fork the game. In game.py, change `run_game(demo=True)` to `run_game(demo=False)`. Edit script.py with your code. Then run the game normally.

## To do

* Write game flavor
* Add database for high scores and submitted scripts
* Add functionality for limited movement and teleportation
* Publish online
* Build a code distribution
* Add scoring system
