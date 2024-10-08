from moviepy.editor import VideoFileClip
import os

def convertator(input_file, output_format):
    if output_format not in ['webm', 'mp4', 'gif']: #checking for a mistakes
        raise ValueError('Wrong format. use these formats: gif, mp4, webm. ') #giving an Error when mistake was given
    
    input_filename, input_extension = os.path.splitext(input_file) #spliting a file for convertation
    output_file = f"{input_filename}.{output_format}" #writing an a format to a file for convertation

    video = VideoFileClip(input_file)

    if output_format == 'gif':
        video.write_gif(output_file) # here convertating to a gif 
    else:
        video.write_videofile(output_file, codec='libvpx' if output_format == 'webm' else 'libx264') # here for webm or mp4
    
    video.close() # closing a file

    print(f"Your video has succsesful convertation to chosen format: {output_format}, and saved as : {output_file}")
    return output_file # return converted file to you