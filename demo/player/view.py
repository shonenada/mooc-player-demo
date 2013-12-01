from flask import Blueprint, render_template


player_app = Blueprint('player', __name__, template_folder='../templates')


@player_app.route('/')
def player():
    return render_template('player.html')
