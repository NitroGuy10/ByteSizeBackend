from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<video_id>/ascii")
def get_video_ascii(video_id):
    return "<p>TODO return the ascii text file</p>"

@app.route("/<video_id>/original")
def get_video_original(video_id):
    return "<p>TODO return the original (mp4) video file</p>"

@app.route("/<video_id>/uncompressed")
def get_video_uncompressed(video_id):
    return "<p>TODO return the uncompressed video file</p>"

