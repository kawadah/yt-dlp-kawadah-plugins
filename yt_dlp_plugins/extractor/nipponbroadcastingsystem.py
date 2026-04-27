from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import (
    int_or_none,
    unified_timestamp,
    url_or_none,
    xpath_element,
    xpath_text,
)


# ニッポン放送 PODCAST STATION
class NipponBroadcastingSystemIE(InfoExtractor):
    _VALID_URL = r"https?://podcast\.1242\.com/(?P<id>[^/?#]+)"

    _TESTS = [
        {
            "url": "https://podcast.1242.com/muso/",
            "info_dict": {
                "id": "muso",
                "title": "長浜広奈　天下無双【オールナイトニッポンPODCAST】",
            },
            "playlist_mincount": 1,
            "params": {"skip_download": True},
        },
        {
            "url": "https://podcast.1242.com/muso/?ep=0",
            "info_dict": {
                "id": "muso-0",
                "ext": "mp3",
                "title": "#1 無双開始",
            },
            "params": {"skip_download": True},
        },
    ]

    _ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"

    def _real_extract(self, url):
        podcast_id = self._match_id(url)
        ep_param = self._search_regex(
            r"[?&]ep=(\d+)", url, "ep parameter", default=None
        )

        webpage = self._download_webpage(url, podcast_id)

        rss_url = self._search_json(
            r"var\s+myAjaxObject\s*=\s*",
            webpage,
            "Ajax object",
            podcast_id,
        ).get("rssfeed")

        feed = self._download_xml(rss_url, podcast_id, note="Downloading RSS feed")
        channel = feed.find("channel")

        podcast_title = xpath_text(channel, "title")
        podcast_description = xpath_text(channel, "description")

        items = channel.findall("item")

        if ep_param is not None:
            item = items[-(int(ep_param) + 1)]
            enclosure = xpath_element(item, "enclosure")
            itunes_image = xpath_element(item, f"{{{self._ITUNES_NS}}}image")
            return {
                "id": f"{podcast_id}-{ep_param}",
                "title": xpath_text(item, "title"),
                "url": url_or_none(enclosure.get("url"))
                if enclosure is not None
                else None,
                "description": xpath_text(item, "description"),
                "thumbnail": url_or_none(itunes_image.get("href"))
                if itunes_image is not None
                else None,
                "duration": int_or_none(
                    xpath_text(item, f"{{{self._ITUNES_NS}}}duration")
                ),
                "timestamp": unified_timestamp(xpath_text(item, "pubDate")),
                "series": podcast_title,
                "author": xpath_text(item, f"{{{self._ITUNES_NS}}}author"),
            }

        entries = []
        for i, item in enumerate(items):
            enclosure = xpath_element(item, "enclosure")
            audio_url = (
                url_or_none(enclosure.get("url")) if enclosure is not None else None
            )
            if not audio_url:
                continue
            itunes_image = xpath_element(item, f"{{{self._ITUNES_NS}}}image")
            ep_index = len(items) - 1 - i
            entries.append(
                {
                    "id": f"{podcast_id}-{ep_index}",
                    "title": xpath_text(item, "title"),
                    "url": audio_url,
                    "description": xpath_text(item, "description"),
                    "thumbnail": url_or_none(itunes_image.get("href"))
                    if itunes_image is not None
                    else None,
                    "duration": int_or_none(
                        xpath_text(item, f"{{{self._ITUNES_NS}}}duration")
                    ),
                    "timestamp": unified_timestamp(xpath_text(item, "pubDate")),
                    "series": podcast_title,
                    "author": xpath_text(item, f"{{{self._ITUNES_NS}}}author"),
                }
            )

        return self.playlist_result(
            entries,
            playlist_id=podcast_id,
            playlist_title=podcast_title,
            playlist_description=podcast_description,
        )
