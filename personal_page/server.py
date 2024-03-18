from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # Run the app in the debug mode to auto_reload when the file is saved
    app.run(debug=True)
