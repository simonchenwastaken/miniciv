""" The game server. """
from flask import Flask, render_template
app = Flask(__name__)


# #### TILE DEBUGGING #### #
@app.route('/debug/')
def debug_tile():
    return render_template('debug.html')


@app.route('/debug/tile/')
def send_tile():
    from graphics import GRASS_TILE  # CHANGE THIS CODE TO SEE WHAT TILE YOU ARE LOOKING AT
    return {'screen': GRASS_TILE}


if __name__ == '__main__':
    app.run(debug=True)