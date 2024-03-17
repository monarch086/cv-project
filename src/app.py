import datetime as dt
from flask import Flask, request, jsonify
from object_detection import detect
import json

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<p><h2>Computer Vision Project: Object Detection Web Server.</h2></p>"

@app.route(
    "/detect",
    methods=["POST"],
)
def detect_objects():
    print(request.files)
    
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']

    results = detect(file)

    time = dt.datetime.now()

    result = {
        "image": file.filename,
        "timestamp": time.isoformat(),
        "objects": json.dumps(results)
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)