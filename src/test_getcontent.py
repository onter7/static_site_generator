import unittest

from getcontent import *


class TestGetContent(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Heading

Paragraph text

>Quote
>Multiline
"""
        heading = extract_title(md)
        self.assertEqual(
            heading,
            "Heading"
        )