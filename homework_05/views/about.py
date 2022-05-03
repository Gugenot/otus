from flask import (
    Blueprint,
    render_template,
)

about_app = Blueprint("about_app", __name__)

@about_app.get("/", endpoint="about_page")
def about_page():
    return render_template("pages/about.html")
