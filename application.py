from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def application_page():
     return render_template("application-form.html")


@app.route("/application-response", methods=["POST"])
def response_page():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    job = request.form.get("job")

    return render_template(
        "application-response.html",
        firstname=firstname, 
        lastname=lastname,
        salary=salary, 
        job=job)




if __name__ == "__main__":
    app.run(debug=True)
