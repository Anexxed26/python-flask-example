from flask import Flask, Response
import os

app = Flask(__name__)
porta = os.environ.get("APP_PORT")

@app.route("/health")
def health():
    return Response("tudo certo!", status=200)

@app.route("/")
def hello_world():
    return "teste"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=porta, debug=True)
