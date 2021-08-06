from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome</h1>"

@app.route("/server-status")
def status():
    return make_response("", 200)


if __name__ == "__main__":
    app.run(port=5000)
