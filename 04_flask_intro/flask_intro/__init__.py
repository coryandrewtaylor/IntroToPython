from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


def create_app(csrf_key_path):
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    with open(csrf_key_path) as fo:
        app.secret_key = fo.read()

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.route("/")
    # @app.route("/greeting")
    def greet():
        _greeting = {"greeting": "Hello, world!"}
        return _greeting

    
    @app.route("/greeting")
    @app.route("/greeting/<user>")
    def greet_user(user=None):
        _user = user if user else "world"
        return render_template("user.html", user=_user)


    @app.route("/api/v1/greeting/<user>")
    def api_greet_user(user):
        _response = {"greeting": "Hello", "user": user}
        return _response


    @app.route("/api/v1/math/sum", methods=["POST"])
    def add_by_api():
        """
        {"add": [list of numbers]}

        Returns:
            [type]: [description]
        """
        _to_add = request.form.getlist("add")
        _all_addable = all(n.isnumeric() for n in _to_add)
        
        if bool(_to_add) is True and _all_addable is True:
            _sum = sum(float(n) for n in _to_add)
            return {"sum": _sum}, 200
        else:
            return 'Bad request', 400
    
    return app