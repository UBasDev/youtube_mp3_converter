import yt_dlp
import os
from constants import OUTPUT_PATH

class ProcessLinkService:
    def __init__(self):
        self.ydl_options = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(OUTPUT_PATH, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }

    def download_youtube_as_mp3(self, url: str) -> None:
        if url is None or url.strip() == "":
            raise ValueError("URL is empty. Please provide a valid Youtube URL")
        
        with yt_dlp.YoutubeDL(self.ydl_options) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Completed track: {info_dict['title']}")