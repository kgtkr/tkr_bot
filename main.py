from mastodon import Mastodon, StreamListener
import settings
import re
import MeCab
import random

m = MeCab.Tagger("-Owakati")


class Listner(StreamListener):
    def __init__(self):
        self.data = dict()
        self.count = 0

    def on_update(self, data):
        words = m.parse(re.sub(
            r"([@#:][a-zA-Z0-9_\-]+\:?)|(<a(.*?)/a>)|(<(.*?)>)", "", data.content)).strip().split(" ")
        self.add_data(words)
        self.count += 1
        if self.count % 10 == 0:
            print(self.gen_text())

    def add_data(self, words):
        for x in zip([None]+words, words+[None]):
            k = x[0]
            v = x[1]
            if k not in self.data:
                self.data[k] = []
            self.data[k].append(v)

    def gen_text(self):
        res = []
        key = None
        while key in self.data and len(self.data[key]) != 0:
            key = random.choice(self.data[key])
            if key == None:
                break
            res.append(key)
        return "".join(res)


mastodon = Mastodon(
    access_token=settings.token,
    api_base_url="https://mstdn.jp"
)
mastodon.stream_public(Listner())
