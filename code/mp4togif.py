from moviepy.editor import VideoFileClip
import os

def convertator(input_file, output_format):
    if output_format not in ['webm', 'mp4', 'gif']:
        pass
    