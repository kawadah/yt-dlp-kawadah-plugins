from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import (
    traverse_obj,
    unified_timestamp,
    url_or_none,
)


class JOQRPodcastsIE(InfoExtractor):
    _VALID_URL = r"https?://podcastqr\.joqr\.co\.jp/programs/(?P<id>[a-zA-Z0-9_-]+)"

    _TESTS = [
        {
            "url": "https://podcastqr.joqr.co.jp/programs/golden_shinshi",
            "info_dict": {
                "id": "golden_shinshi",
                "title": "大竹紳士交遊録 - 大竹まことゴールデンラジオ！",
            },
            "playlist_mincount": 1,
            "params": {"skip_download": True},
        },
    ]

    def _real_extract(self, url):
        program_id = self._match_id(url)

        data = self._download_json(
            f"https://podcastqr.joqr.co.jp/api/programs/{program_id}/episodes",
            program_id,
            query={"page": 1},
        )

        program = traverse_obj(data, ("data", 0, "program")) or {}

        entries = []
        for episode in traverse_obj(data, ("data", ...)):
            episode_id = episode.get("id")
            audio_url = url_or_none(episode.get("audioUrl"))
            if not episode_id or not audio_url:
                continue

            entries.append(
                {
                    "id": episode_id,
                    "title": episode.get("title"),
                    "url": audio_url,
                    "description": episode.get("description"),
                    "thumbnail": url_or_none(episode.get("imageUrl")),
                    "timestamp": unified_timestamp(episode.get("publishedAt")),
                    "series": traverse_obj(episode, ("program", "title")),
                }
            )

        return self.playlist_result(
            entries,
            playlist_id=program_id,
            playlist_title=program.get("title"),
            playlist_description=program.get("description"),
        )
