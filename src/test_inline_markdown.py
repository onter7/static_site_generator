import unittest

from inline_markdown import (
    split_nodes_delimeter,
    extract_markdown_images,
    extract_markdown_links
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_code,
    text_type_bold,
    text_type_italic
)


class TextInlineMarkdow(unittest.TestCase):
    def test_split_nodes_delimeter_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimeter([node], '`', text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes
        )

    def test_split_nodes_delimeter_bold(self):
        node = TextNode("This is **bold text**", text_type_text)
        new_nodes = split_nodes_delimeter([node], '**', text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("bold text", text_type_bold)
            ],
            new_nodes
        )

    def test_split_nodes_delimeter_italic(self):
        node = TextNode("*This is* an italic text", text_type_text)
        new_nodes = split_nodes_delimeter([node], '*', text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is", text_type_italic),
                TextNode(" an italic text", text_type_text)
            ],
            new_nodes
        )

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        res = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
            ],
            res
        )

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        res = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another")
            ],
            res)


if __name__ == "__main__":
    unittest.main()