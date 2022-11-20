from pprint import pprint

from yt_dlp import YoutubeDL
import json

from pathlib import Path


def write_json(self, data):
    with self.open('w', encoding='utf-8') as w:
        json.dump(data, w)


def read_json(self):
    with self.open('r', encoding='utf-8') as r:
        return json.load(r)


Path.write_json = write_json
Path.read_json = read_json


CONFIG = {
    "ignore_errors": True,
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


path = Path(__file__).parent
wl_json_path = path / 'watchlater.json'


def start():
    # o = wl_json_path.read_json()
    # print(o.keys(), o['title'], )
    # pprint(o['entries'][0])

    yt = YoutubeTools()
    info = yt.watch_later()
    print(info)
    wl_json_path.write_json(info)
