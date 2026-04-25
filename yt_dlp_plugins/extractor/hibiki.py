from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import traverse_obj, unified_timestamp, url_or_none


# HiBiKi Radio Station
class HiBiKiIE(InfoExtractor):
    _VALID_URL = r"https://hibiki-radio\.jp/description/(?P<id>[a-zA-Z0-9_-]+)/detail"

    _TESTS = [
        {
            "url": "https://hibiki-radio.jp/description/haruyuri/detail",
            "info_dict": {
                "id": "haruyuri",
                "title": "福嶋晴菜・藤本侑里のはるゆり開花宣言",
            },
            "playlist_count": 2,
            "playlist": [
                {
                    "info_dict": {
                        "id": "21157",
                        "ext": "m4a",
                        "title": "福嶋晴菜・藤本侑里のはるゆり開花宣言 第26回（最終回）",  # noqa: E501
                        "series": "福嶋晴菜・藤本侑里のはるゆり開花宣言",
                        "episode": "第26回（最終回）",
                        "episode_id": "17247",
                        "duration": 4130,
                        "release_date": "20260130",
                        "release_timestamp": 1769770800,
                    },
                },
                {
                    "info_dict": {
                        "id": "21158",
                        "ext": "m4a",
                        "title": "福嶋晴菜・藤本侑里のはるゆり開花宣言 第26回（最終回）（楽屋裏）",  # noqa: E501
                        "series": "福嶋晴菜・藤本侑里のはるゆり開花宣言",
                        "episode": "第26回（最終回）",
                        "episode_id": "17247",
                        "duration": 776.99,
                        "release_date": "20260130",
                        "release_timestamp": 1769770800,
                    },
                },
            ],
            "params": {"skip_download": True},
        }
    ]

    _API_BASE = "https://vcms-api.hibiki-radio.jp/api/v1"
    _HEADERS = {
        "Origin": "https://hibiki-radio.jp",
        "Referer": "https://hibiki-radio.jp/",
        "X-Requested-With": "XMLHttpRequest",
    }

    def _real_extract(self, url):
        program_id = self._match_id(url)

        program = self._download_json(
            f"{self._API_BASE}/programs/{program_id}",
            program_id,
            headers=self._HEADERS,
        )

        episode = program.get("episode") or {}
        program_name = program.get("name", "")
        episode_name = episode.get("name", "")
        description = program.get("description")

        thumbnails = []
        for img_key, info_key in [
            ("sp_image_url", "sp_image_info"),
            ("pc_image_url", "pc_image_info"),
        ]:
            img_url = url_or_none(program.get(img_key))
            if img_url:
                thumbnails.append(
                    {
                        "url": img_url,
                        **traverse_obj(
                            program,
                            (
                                info_key,
                                {
                                    "width": ("width", {int}),
                                    "height": ("height", {int}),
                                },
                            ),
                        ),
                    }
                )

        release_timestamp = unified_timestamp(
            program.get("episode_updated_at"), tz_offset=9
        )

        entries = []

        for key, is_additional in [("video", False), ("additional_video", True)]:
            video = episode.get(key)
            if not video:
                continue

            video_id = video.get("id")
            if not video_id:
                continue

            kind = "additional " if is_additional else ""
            note = f"Downloading {kind}video playlist URL"
            play_check = self._download_json(
                f"{self._API_BASE}/videos/play_check?video_id={video_id}",
                program_id,
                headers=self._HEADERS,
                note=note,
            )

            playlist_url = url_or_none(play_check.get("playlist_url"))
            if not playlist_url:
                continue

            formats = self._extract_m3u8_formats(playlist_url, str(video_id))

            title = f"{program_name} {episode_name}"
            if is_additional:
                title += "（楽屋裏）"

            entries.append(
                {
                    "id": str(video_id),
                    "title": title,
                    "formats": formats,
                    "thumbnails": thumbnails,
                    "description": description,
                    "duration": video.get("duration"),
                    "series": program_name,
                    "episode": episode_name,
                    "episode_id": str(episode.get("id") or ""),
                    "release_timestamp": release_timestamp,
                }
            )

        return self.playlist_result(
            entries,
            playlist_id=program_id,
            playlist_title=program_name,
            playlist_description=description,
        )
