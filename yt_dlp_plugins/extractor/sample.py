# ⚠ Don't use relative imports
from yt_dlp.extractor.common import InfoExtractor

# ℹ️ If you need to import from another plugin
# from yt_dlp_plugins.extractor.example import ExamplePluginIE

# ℹ️ Instructions on making extractors can be found at:
# 🔗 https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md#adding-support-for-a-new-site


# ⚠ The class name must end in "IE"
class SamplePluginIE(InfoExtractor):
    _WORKING = False
    _VALID_URL = r"^sampleplugin:"

    def _real_extract(self, url):
        self.to_screen(f'URL "{url}" successfully captured')
