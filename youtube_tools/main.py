from pprint import pprint

from yt_dlp import YoutubeDL
from .utils import path

from pathlib import Path
from requests import Session




CONFIG = {
    "ignoreerrors": True,
    "verbose": True,
    "debug": True,
    'yes-playlist': True,
    'cookiesfrombrowser': ('chrome',),
    # "extract_flat": True,
    # "dump_single_json": "",
    # "print_to_file"
}


class YoutubeTools:
    WATCH_LATER_URL = 'https://www.youtube.com/playlist?list=WL'
    HISTORY_URL = 'https://www.youtube.com/feed/history'

    def __init__(self, config=CONFIG):
        self.youtube_dl = YoutubeDL(config)

    def watch_later(self):
        #     with YoutubeDL(ydl_opts) as ydl:
        #         info = ydl.extract_info(self.WATCH_LATER_URL, download=False)
        #         print(info)
        return self.youtube_dl.extract_info(self.WATCH_LATER_URL, download=False)



wl_json_path = path / 'watchlater.json'

client = Session()
DOMAIN = 'http://127.0.0.1:8090'


def process_local():
    o = wl_json_path.read_json()
    # print(o.keys(), o['title'], )
    for i in o['entries']:
        if (not i):
            print('shhh', i)
            continue
        data = {
            "title": i.get('title', ''),
            "language": 'en',
            "channel": i['channel'],
            "like_count": i.get('like_count', 0),
            "view_count": i['view_count'],
            "original_url": i['original_url'],
            "availability": i['availability'],
            # "upload_date":  i['upload_date'],
            "duration": i['duration_string']
        }
        # pprint(list(i.keys()))
        print(
            i['resolution'],
            i['description'],
            i['channel_follower_count'],
            i['release_timestamp'],
            i['chapters'],
            sep=" ____\n---- ")

        req = client.post(
            DOMAIN + '/api/collections/watch_later/records', json=data)
        print(req)
        # break


def start():
    process_local()

    # yt = YoutubeTools()
    # info = yt.watch_later()
    # print(info)
    # wl_json_path.write_json(info)
