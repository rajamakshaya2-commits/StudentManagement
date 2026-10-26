
from flask import Flask, request
app = Flask(__name__)
s = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        s.append(request.form["name"])
    return "<h2>Student Management System</h2><form method='post'><input name='name'><button>Add</button></form><h3>Students:</h3>" + "<br>".join(s)

app.run()
