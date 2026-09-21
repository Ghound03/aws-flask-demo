from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from my first AWS Flask project!"


if __name__ == "__main__":
    app.run(debug=True)