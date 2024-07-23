from pytubefix import YouTube 
import pprint
# where to save 
SAVE_PATH = "videos" #to_do 

# link of the video to be downloaded 
link = "https://www.youtube.com/watch?v=pBL-ygQs14g"

try: 
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for mp4 files
mp4_streams_audio = yt.streams.filter(type='audio').order_by('abr')
mp4_streams_video = yt.streams.filter(type='video').order_by('resolution')

# get the video with the highest resolution
pprint.pp(list(mp4_streams_audio))
pprint.pp(list(mp4_streams_video))

# d_video = mp4_streams[-1]

# try: 
#     # downloading the video 
#     d_video.download(output_path=SAVE_PATH)
#     print('Video downloaded successfully!')
# except: 
#     print("Some Error!")
