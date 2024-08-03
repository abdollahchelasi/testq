from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "ABDOLLAH CHELASI"


if __name__ == "__main__":
    app.run()
