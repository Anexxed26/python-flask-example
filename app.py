from flask import Flask, Response
import os

app = Flask(__name__)
porta = os.environ.get("APP_PORT")
contador = 0

@app.route("/health")
def health():
    return Response("tudo certo!", status=200)

@app.route("/")
def hello_world():
    return "teste"

@app.route("/counter")
def count():
    global contador
    contador += 1
    return str(contador)+'\n'

@app.route("/version")
def version_route():
    return "2.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=porta, debug=True)
