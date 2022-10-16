from flask import Flask, abort, send_file, request
from flask_cors import CORS

import boto3
from botocore.config import Config

import os
import uuid

import compress


app = Flask(__name__)
CORS(app)

s3_config = Config(
    region_name = os.environ["bucketRegion"]
)

s3_client = boto3.client("s3", config=s3_config,
    aws_access_key_id = os.environ["bucketAccessKeyId"],
    aws_secret_access_key = os.environ["bucketSecretAccessKey"]
)

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
        # Read the request
        request_data = request.get_json()
        bucket_location = request_data["bucketVideoKey"]
        bucket_text_location = f"{os.environ['bucketTextDirName']}/{uuid.uuid4()}.txt"

        # Do the thing
        downloaded_file_name = "downloaded.mp4"
        s3_client.download_file(os.environ["bucketName"], bucket_location, downloaded_file_name)

        compress.processVideo(downloaded_file_name)

        # Upload it to s3
        s3_client.upload_file("res.txt", os.environ["bucketName"], bucket_text_location)

        # Done
        return "bingus"
    else:
        abort(400)


#s3_client.upload_file("rickroll.mp4", os.environ["bucketName"], "videos/rickroll.mp4")
