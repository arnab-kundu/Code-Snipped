# python -m pip install pytube
# python -m pip install --upgrade pytube
import os
import msvcrt
from pytube import Playlist
import pytube

def downloadPlaylist():
  print("Enter YouTube Playlist url:")
  # input
  youtube_playlist_link = input() 
  playlist = pytube.Playlist(youtube_playlist_link)

  # Create folder for playList
  folderName = playlist.title + " by " + pytube.YouTube(playlist.video_urls[0]).author
  if not os.path.exists(folderName):
    os.makedirs(folderName)


  # Downloading playlist
  print("\nDownloading playlist into '%s' Folder" % folderName)
  print('Number of videos in playlist: %s' % len(playlist.video_urls))
  print("please wait...\n")

  for youtube_link in playlist.video_urls:
    youtube_video = pytube.YouTube(youtube_link)
  
    # output
    print("Downloading:   ", youtube_video.title)

    stream = youtube_video.streams.get_highest_resolution()
    stream.download(folderName)

  print("Download Successfull !!!")
  reDownloadConfirmation()

def reDownloadConfirmation():  
  print('\nPress `Escape` to Exit: \n\tor \nPress `Enter` to download again : ')
  key = msvcrt.getch()
  #print(key)

  if(key == chr(27).encode()):
    print('Exit()')
  elif(key == b'\r'):
    #print('Enter key pressed')
    downloadPlaylist()
  else:
    print('Invalid input')

downloadPlaylist()