from flask import Flask

from flask_intro import configure_routes

app = configure_routes(Flask(__name__))