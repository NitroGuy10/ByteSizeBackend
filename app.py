from flask import Flask, abort, send_file
from flask_cors import CORS

# import os
# os.environ["BUCKET_URL"]

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return send_file("upload.html")

@app.route("/<video_id>/ascii")
def get_video_ascii(video_id):
    return "<p>TODO return the ascii text file</p>"

@app.route("/<video_id>/original")
def get_video_original(video_id):
    return "<p>TODO return the original (mp4) video file</p>"

@app.route("/<video_id>/uncompressed")
def get_video_uncompressed(video_id):
    return "<p>TODO return the uncompressed video file</p>"

@app.route("/process_video", methods=["POST"])
def upload_and_process_video():
    if request.method == "POST":
        return "bingus"
    else:
        abort(400)

