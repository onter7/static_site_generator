import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text node", "bold")
        node2 = TextNode("This is text node", "bold")
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is text node", "bold")
        node2 = TextNode("This is text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is text node", "bold")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is text node", "bold", "https://www.boot.dev")
        self.assertEqual("TextNode(This is text node, bold, https://www.boot.dev)", repr(node))


if __name__ == "__main__":
    unittest.main()