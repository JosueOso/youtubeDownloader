from pytube import YouTube

def get_url():
    url = input("Enter the url of the video: ")
    return url

def download_video(url):
    yt = YouTube(url)
    title = yt.title 
    print("Downloading..." + title)
    yt.streams.filter(progressive= True, file_extension= 'mp4').order_by
    ('resolution').desc().first().download('/Users/josue/Desktop/YouTube Downloads')
    print("Download Complete" + title)
    return title

download_video(get_url())
