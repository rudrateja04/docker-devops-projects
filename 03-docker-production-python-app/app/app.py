from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Production-ready Python app running in Docker"

if __name__ == "__main__":
    app.run()
