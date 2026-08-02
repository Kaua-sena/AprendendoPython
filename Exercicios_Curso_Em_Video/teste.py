from rich import print
from flask import Flask

app = Flask(__name__)

@app.route("/usuario")
def usuario():
    return {
        "Nome": "Kaua",
        "Idade": 20
    }
app.run(debug=True)
