from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import (
    clean_html,
    float_or_none,
    traverse_obj,
    unified_timestamp,
    url_or_none,
)


# JFN Pods
class JFNPodsIE(InfoExtractor):
    _VALID_URL = r"https?://jfn-pods\.com/program/(?P<program_id>[0-9]+)/voice/(?P<id>[a-zA-Z0-9]+)"

    _TESTS = [
        {
            "url": "https://jfn-pods.com/program/300011016/voice/F0o28r8LF5",
            "info_dict": {
                "id": "JPFMN6911673150",
                "ext": "mp3",
                "title": "2026年4月25日放送",
                "series": "KOTORIの「遠き山に陽は落ちて」",
            },
            "params": {"skip_download": True},
        },
    ]

    def _real_extract(self, url):
        voice_id = self._match_id(url)

        webpage = self._download_webpage(url, voice_id)

        episode_id = self._search_regex(
            r'https://playlist\.megaphone\.fm/?\?e=([^"&\s]+)',
            webpage,
            "episode ID",
        )

        data = self._download_json(
            f"https://player.megaphone.fm/playlist/episode/{episode_id}",
            voice_id,
        )

        episode = traverse_obj(data, ("episodes", 0)) or {}

        return {
            "id": episode.get("uid") or voice_id,
            "title": episode.get("title"),
            "url": (
                url_or_none(episode.get("audioUrl"))
                or url_or_none(episode.get("episodeUrlHRef"))
            ),
            "description": clean_html(episode.get("summary")),
            "thumbnail": url_or_none(episode.get("imageUrl")),
            "duration": float_or_none(episode.get("duration")),
            "timestamp": unified_timestamp(episode.get("pubDate")),
            "series": data.get("podcastTitle"),
        }
