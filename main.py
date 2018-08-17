from mastodon import Mastodon, StreamListener
import settings
import re
import MeCab

m = MeCab.Tagger("-Owakati")


class Listner(StreamListener):
    def on_update(self, data):
        print(
            m.parse(re.sub(r"([@#:][a-zA-Z0-9_\-]+\:?)|(<a(.*?)/a>)|(<(.*?)>)", "", data.content)).strip().split(" "))


mastodon = Mastodon(
    access_token=settings.token,
    api_base_url="https://mstdn.jp"
)
mastodon.stream_public(Listner())
