import os
from pytube import Playlist
import pytube

print("Enter YouTube Playlist url:")
# input
youtube_playlist_link = input() 
playlist = Playlist(youtube_playlist_link)


# Create folder for playList
newpath = playlist.title 
if not os.path.exists(newpath):
    os.makedirs(newpath)


# Downloading playlist
print("\nDownloading playlist into '%s' Folder" % playlist.title)
print('Number of videos in playlist: %s' % len(playlist.video_urls))
print("please wait...\n")

for youtube_link in playlist.video_urls:
  yt = pytube.YouTube(youtube_link)
  
  # output
  print("Downloading:   ", yt.title)

  stream = yt.streams.get_highest_resolution()
  stream.download(playlist.title)