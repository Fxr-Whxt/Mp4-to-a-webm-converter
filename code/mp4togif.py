from moviepy.editor import VideoFileClip
import os

videoClip = VideoFileClip(str(input("video:")))

videoClip.write_gif("gifile.gif")