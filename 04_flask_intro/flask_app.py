import os.path

from flask_intro import create_app

secret_key_path = os.path.abspath("SECRET_KEY.txt")

app = create_app(secret_key_path)