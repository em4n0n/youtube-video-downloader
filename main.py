from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url) #grabs an instance of the YouTube video
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution() #gets the highest resolution stream
        highest_res_stream.download(output_path=save_path) #downloads the video to the specified path
        print(f"Downloaded: {yt.title} to {save_path}")
        
    except Exception as e:
        print(e)
        
url = ""
save_path = "D:/videos"

download_video(url, save_path)
        