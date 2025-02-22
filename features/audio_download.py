from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_audio(url, name):
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    if name == "":
        name = yt.title

    ys = yt.streams.get_audio_only()
    ys.download(output_path="temp/",filename=f"{name}.m4a")