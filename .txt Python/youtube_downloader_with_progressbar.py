import pytube
from pytube.cli import on_progress
        
print("Enter YouTube url:")
# input
youtube_link = input()

yt = pytube.YouTube(youtube_link, on_progress_callback=on_progress)

# output
print("Downloading:   ", yt.title)

stream = yt.streams.get_highest_resolution()
stream.download()
