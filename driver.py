from flask import Flask, jsonify, request

from bot import process

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page (Test)'



log_file_path = "out/app.log"

@app.route('/submit-msg', methods = ['POST'])
def submit_msg():
    data = request.get_json()
    return process(data), 200

if __name__ == '__main__':
    from waitress import serve
    print("Running server")
    serve(app, host="0.0.0.0", port=8080)
