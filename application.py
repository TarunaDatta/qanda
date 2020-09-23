from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def qanda():
    if request.method = "POST"
    return render_template("index.html")
