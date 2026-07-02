from services.youtube_service import YouTubeService
from core.utils import *

url = input("Link: ")

video = YouTubeService.get_info(url)

print()

print(video["title"])
print(video["channel"])
print(seconds_to_time(video["duration"]))
print(format_views(video["views"]))
print(format_date(video["upload_date"]))
print(video["thumbnail"])