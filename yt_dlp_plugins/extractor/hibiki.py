from yt_dlp.extractor.common import InfoExtractor


class HiBiKiIE(InfoExtractor):
    _VALID_URL = r'https://hibiki-radio\.jp/description/(?P<id>[a-zA-Z0-9_-]+)/detail'

    _TESTS = [{
        'url': 'https://hibiki-radio.jp/description/haruyuri/detail',
        'info_dict': {
            'id': 'haruyuri',
            'title': '福嶋晴菜・藤本侑里のはるゆり開花宣言',
        },
        'playlist_mincount': 1,
    }]

    _API_BASE = 'https://vcms-api.hibiki-radio.jp/api/v1'
    _HEADERS = {
        'Origin': 'https://hibiki-radio.jp',
        'Referer': 'https://hibiki-radio.jp/',
        'X-Requested-With': 'XMLHttpRequest',
    }

    def _real_extract(self, url):
        program_id = self._match_id(url)

        program = self._download_json(
            f'{self._API_BASE}/programs/{program_id}',
            program_id,
            headers=self._HEADERS,
        )

        episode = program['episode']
        program_name = program.get('name', '')
        episode_name = episode.get('name', '')
        thumbnail = program.get('sp_image_url') or program.get('pc_image_url')
        description = program.get('description')

        entries = []

        for key, is_additional in [('video', False), ('additional_video', True)]:
            video = episode.get(key)
            if not video:
                continue

            video_id = video['id']

            play_check = self._download_json(
                f'{self._API_BASE}/videos/play_check?video_id={video_id}',
                program_id,
                headers=self._HEADERS,
                note=f'Downloading {"additional " if is_additional else ""}video play token',
            )

            playlist_url = play_check['playlist_url']
            formats = self._extract_m3u8_formats(playlist_url, str(video_id))

            title = f'{program_name} {episode_name}'
            if is_additional:
                title += '（楽屋裏）'

            entries.append({
                'id': str(video_id),
                'title': title,
                'formats': formats,
                'thumbnail': thumbnail,
                'description': description,
            })

        return self.playlist_result(
            entries,
            playlist_id=program_id,
            playlist_title=program_name,
            playlist_description=description,
        )
