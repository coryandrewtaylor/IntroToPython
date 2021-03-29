from flask import Flask, request, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    @app.route("/greeting")
    def greet():
        _greeting = {"greeting": "Hello, world!"}
        return _greeting

    
    @app.route("/greeting/<user>")
    def greet_user(user):
        return render_template("user.html", user=user)


    @app.route("/api/v1/greeting/<user>")
    def api_greet_user(user):
        _response = {"greeting": "Hello", "user": user}
        return _response


    @app.route("/math/sum", methods=["POST"])
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