import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(None, None, None, props)
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())

    def test_to_html_paragraph(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_to_html_anchor_with_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual("<a href=\"https://www.google.com\">Click me!</a>", node.to_html())

    def test_no_tag(self):
        node = LeafNode(None, "It's just a simple text.")
        self.assertEqual("It's just a simple text.", node.to_html())

    def test_no_value(self):
        node = LeafNode()
        self.assertRaises(ValueError, node.to_html)

    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_nested_parent_node(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("p", "Bold text"),
                        LeafNode("i", "Italic text")
                    ]
                ),
                ParentNode(
                    "div",
                    [
                        LeafNode(None, "Normal text")
                    ]
                )
            ],
        )

        self.assertEqual("<div><div><p>Bold text</p><i>Italic text</i></div><div>Normal text</div></div>", node.to_html())


if __name__ == "__main__":
    unittest.main()