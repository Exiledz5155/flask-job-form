from flask import Flask, render_template


app = Flask(__name__)

# Decorator which calls a corresponding function
@app.route("/")
def index():
    return render_template("index.html")


app.run(debug=True, port=5001)