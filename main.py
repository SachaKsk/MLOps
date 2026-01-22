from flask import Flask

app = Flask(__name__)

@app.route("/<int:surface>")
def home(surface):
    return {"surface": 1}

if __name__ == "__main__":
    app.run(debug=True)
