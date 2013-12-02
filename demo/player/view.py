from flask import Blueprint, render_template, json


player_app = Blueprint('player', __name__, template_folder='../templates')


@player_app.route('/')
def player():
    return render_template('player.html')


@player_app.route('/getdata')
def get_data():
    return json.dumps(
        [
            {'time': '3.0',
             'q': 'what is this?',
             'a': ['First', 'S', 'C']
            },
            {'time': '8.0',
             'q': 'what is this222?',
             'a': ['First222', '222S', '222C']
            },
        ]
    )
