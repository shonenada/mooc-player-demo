from flask import Flask
from flask.ext.gears import Gears
from gears_stylus import StylusCompiler
from gears_coffeescript import CoffeeScriptCompiler

from demo.player.view import player_app


gears = Gears()


def setup_compilers(app):

    _compilers = {
        '.styl': StylusCompiler.as_handler(),
        '.coffee': CoffeeScriptCompiler.as_handler()
    }

    def gears_environment(app):
        return app.extensions['gears']['environment']

    env = gears_environment(app)
    for extension, compiler in _compilers.iteritems():
        env.compilers.register(extension, compiler)


def create_app():
    app = Flask(__name__)

    gears.init_app(app)
    setup_compilers(app)
    
    app.register_blueprint(player_app)
    
    return app
