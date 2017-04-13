from flask import Flask
app = application = Flask(__name__)

@app.route("/settings")
def hello():
    return "Hello World! Settings "

if __name__ == "__main__":
    app.run()

