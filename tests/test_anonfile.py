#!/usr/bin/env python3

import unittest
from pathlib import Path

from src.anonfile import AnonFile

def test_option(token):
    global TOKEN
    TOKEN = token


class TestAnonFile(unittest.TestCase):
    def setUp(self):
        self.anon = AnonFile(TOKEN)
        self.test_file = Path("tests/test.txt")
        self.test_path = "https://anonfiles.com/93k5x1ucu0/test_txt"

    def test_upload(self):
        result = self.anon.upload(self.test_file)
        self.assertTrue(result.status, msg="Expected 200 HTTP Error Code")
        self.assertTrue(all([result.url.scheme, result.url.netloc, result.url.path]), msg="Invalid URL.")

    def test_download(self):
        result = self.anon.download(self.test_path)
        self.assertTrue(result.file_path.exists(), msg="Download not successful.")
        self.assertEqual(result.file_path.name, self.test_file.name, msg="Different file in download path detected.")
        result.file_path.unlink()
