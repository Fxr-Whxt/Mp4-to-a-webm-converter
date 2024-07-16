from moviepy.editor import VideoFileClip

videoClip = VideoFileClip(str(input("video:")))

videoClip.write_gif("gifile.gif")