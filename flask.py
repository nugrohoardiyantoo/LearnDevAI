from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return {"massage" : "Hello World"}

# after those run in terminal use "flask --app server --debug run"
# run curl -X GET -i -w '\n' localhost:5000s