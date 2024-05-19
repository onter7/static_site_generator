import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(None, None, None, props)
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())