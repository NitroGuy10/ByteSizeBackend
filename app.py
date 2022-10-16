import shutil
from flask import Flask, abort, send_file, request
from flask_cors import CORS

import boto3
from botocore.config import Config

import os
import uuid

import compress
import sys
sys.path.insert(0, "ByteSizeML")
import inference
import inferenceColor


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

@app.route("/video_to_text", methods=["POST"])
def video_to_text():
    if request.method == "POST":
        # Read the request
        request_data = request.get_json()
        bucket_location = request_data["bucketVideoKey"]
        text_uuid = uuid.uuid4()
        bucket_text_location = f"{os.environ['bucketTextDirName']}/{text_uuid}.txt"

        # Do the thing
        downloaded_file_name = "downloaded.mp4"
        s3_client.download_file(os.environ["bucketName"], bucket_location, downloaded_file_name)

        compress.processVideo(downloaded_file_name)

        # Upload the text to s3
        exported_text_file_name = "res.txt"
        s3_client.upload_file(exported_text_file_name, os.environ["bucketName"], bucket_text_location)

        # Done, now send a response
        return_dict = {
            "bucketTextLocation": bucket_text_location
        }
        print(return_dict)
        return return_dict
    else:
        abort(400)

@app.route("/text_to_video", methods=["POST"])
def text_to_video():
    if request.method == "POST":
        # Read the request
        request_data = request.get_json()
        bucket_location = request_data["bucketTextKey"]
        video_uuid = uuid.uuid4()
        bucket_reconstructed_video_location = f"{os.environ['bucketVideoDirName']}/{video_uuid}.mp4"

        # Prepare for ML on the text
        downloaded_file_name = "figure/res2.txt"
        s3_client.download_file(os.environ["bucketName"], bucket_location, downloaded_file_name)        

        # Do the ML
        inference.real_main("res2")

        # Upload the reconstructed video to s3
        reconstructed_video_path = "figure/videos/video_res2.mp4"
        s3_client.upload_file(reconstructed_video_path, os.environ["bucketName"], bucket_reconstructed_video_location)

        # Done, now send a response
        return_dict = {
            "bucketReconstructedVideoLocation": bucket_reconstructed_video_location
        }
        print(return_dict)
        return return_dict
    else:
        abort(400)

@app.route("/text_to_video_color", methods=["POST"])
def text_to_video_color():
    if request.method == "POST":
        # Read the request
        request_data = request.get_json()
        bucket_location = request_data["bucketTextKey"]
        video_uuid = uuid.uuid4()
        bucket_reconstructed_video_location = f"{os.environ['bucketVideoDirName']}/{video_uuid}.mp4"

        # Prepare for ML on the text
        downloaded_file_name = "figure/res2.txt"
        s3_client.download_file(os.environ["bucketName"], bucket_location, downloaded_file_name)        

        # Do the ML
        inferenceColor.real_main("res2")

        # Upload the reconstructed video to s3
        reconstructed_video_path = "figure/videos/video_res2.mp4"
        s3_client.upload_file(reconstructed_video_path, os.environ["bucketName"], bucket_reconstructed_video_location)

        # Done, now send a response
        return_dict = {
            "bucketReconstructedVideoLocation": bucket_reconstructed_video_location
        }
        print(return_dict)
        return return_dict
    else:
        abort(400)


#s3_client.upload_file("rickroll.mp4", os.environ["bucketName"], "videos/rickroll.mp4")
