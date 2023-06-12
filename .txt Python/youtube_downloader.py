# python -m pip install pytube
# python -m pip install --upgrade pytube
import pytube

print("Enter YouTube url:")
# input
youtube_link = input()

yt = pytube.YouTube(youtube_link)

# output
print("Downloading:   ", yt.title)

stream = yt.streams.get_highest_resolution()
stream.download()
print("Download Successfull !!!")
input("Press enter to exit;")
