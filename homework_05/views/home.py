from flask import (
    Blueprint,
    render_template,
)

home_app = Blueprint("home_app", __name__)

@home_app.get("/", endpoint="home_page")
def home_page():
    return render_template("pages/home.html")
