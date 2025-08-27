import os
import sys
from pathlib import Path

import asyncio

os.environ.setdefault("API_ID", "1")
os.environ.setdefault("API_HASH", "hash")
os.environ.setdefault("BOT_TOKEN", "token")
os.environ.setdefault("OWNER_ID", "1")

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from mbot.utils.mainhelper import parse_spotify_url


def test_parse_spotify_url_with_spotify_scheme():
    item_type, item_id = asyncio.run(parse_spotify_url("spotify:track:12345"))
    assert item_type == "track"
    assert item_id == "12345"


def test_parse_spotify_url_with_http_url(monkeypatch):
    class MockResponse:
        def __init__(self, url):
            self.url = url

    def mock_get(url):
        return MockResponse(url)

    monkeypatch.setattr("mbot.utils.mainhelper.get", mock_get)
    item_type, item_id = asyncio.run(parse_spotify_url("https://open.spotify.com/track/abcde"))
    assert item_type == "track"
    assert item_id == "abcde"
