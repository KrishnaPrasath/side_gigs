from pytube import YouTube
from pprint import pprint
# uri = "https://www.youtube.com/watch?v=x3bfa3DZ8JM"
# path = 'C:\\Users\\Krishna\\New folder'
# yt = YouTube(uri)
# .streams.first().download(path)
# yt = yt.get('mp4', '720p')
# yt.download(path)


def welcome():
    print('Please paste the URI:')
    # uri = input()
    uri = 'https://www.youtube.com/watch?v=xxeBb7OyKXY'
    display_options(uri)


def display_options(uri):
    yt = YouTube(uri)
    streams = yt.streams.all()
    # sorted_streams = streams.sort(key=res)
    videos = []
    for st in streams:
        videos.append(st)

    # video = list(filter(lambda st: st.fps == 30, videos))
    video = list(map(lambda st: [st.itag, st.resolution], videos))
    pprint(video)


# def format_video_link(link):


# def __main__():
if __name__ == "__main__":
    welcome()
