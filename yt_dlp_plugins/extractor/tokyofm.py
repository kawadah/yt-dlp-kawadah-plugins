from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import (
    int_or_none,
    unified_timestamp,
    url_or_none,
    xpath_element,
    xpath_text,
)


# Tokyofm ポッドキャスト
class TOKYOFMPodcastsIE(InfoExtractor):
    _VALID_URL = r"https?://www\.tfm\.co\.jp/podcast/(?P<id>[a-zA-Z0-9_-]+)"

    _TESTS = [
        {
            "url": "https://www.tfm.co.jp/podcast/iberis-and",
            "info_dict": {
                "id": "iberis-and",
                "title": "IBERIs&のKeep On Talking!",
            },
            "playlist_mincount": 1,
            "params": {"skip_download": True},
        },
    ]

    _ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"

    def _real_extract(self, url):
        podcast_id = self._match_id(url)

        webpage = self._download_webpage(url, podcast_id)

        rss_url = self._search_regex(
            r"const\s+rssUrl\s*=\s*'([^']+)'", webpage, "RSS URL"
        )

        feed = self._download_xml(rss_url, podcast_id, note="Downloading RSS feed")
        channel = feed.find("channel")

        channel_title = xpath_text(channel, "title")
        channel_description = xpath_text(channel, "description")

        entries = []

        for item in channel.findall("item"):
            guid = xpath_text(item, "guid")
            if not guid:
                continue

            enclosure = xpath_element(item, "enclosure")
            audio_url = (
                url_or_none(enclosure.get("url")) if enclosure is not None else None
            )
            if not audio_url:
                continue

            itunes_image = xpath_element(item, f"{{{self._ITUNES_NS}}}image")
            itunes_duration = xpath_text(item, f"{{{self._ITUNES_NS}}}duration")
            itunes_author = xpath_text(item, f"{{{self._ITUNES_NS}}}author")

            entries.append(
                {
                    "id": guid,
                    "title": xpath_text(item, "title"),
                    "url": audio_url,
                    "description": xpath_text(item, "description"),
                    "thumbnail": url_or_none(itunes_image.get("href"))
                    if itunes_image is not None
                    else None,
                    "duration": int_or_none(itunes_duration),
                    "timestamp": unified_timestamp(xpath_text(item, "pubDate")),
                    "series": channel_title,
                    "author": itunes_author,
                }
            )

        return self.playlist_result(
            entries,
            playlist_id=podcast_id,
            playlist_title=channel_title,
            playlist_description=channel_description,
        )
