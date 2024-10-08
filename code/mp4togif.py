from moviepy.editor import VideoFileClip
import os

def convertator(input_file, output_format):
    if output_format not in ['webm', 'mp4', 'gif']:
        raise ValueError('Wrong format. use these formats: gif, mp4, webm. ')
    
    input_filename, input_extension = os.path.splitext(input_file)
    output_file = f"{input_filename}.{output_format}"

    video = VideoFileClip(input_file)

    if output_format == 'gif':
        video.write_gif(output_file)
    else:
        video.write_videofile(output_file, codec='libvpx' if output_format == 'webm' else 'libx264')
    
    video.close()

    print(f"Your video has succsesful convertation to chosen format: {output_format}, and saved as : {output_file}")
    return output_file