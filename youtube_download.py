from pytube import YouTube
from halo import Halo

@Halo(text='Downloading', spinner='dots')
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("\n Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)