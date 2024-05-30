import unittest

from markdown_blocks import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
            markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
            blocks = markdown_to_blocks(markdown)
            self.assertListEqual(
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                    "* This is a list\n* with items"
                ],
                blocks
            )

    def test_markdown_to_blocks_newlines(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ],
            blocks
        )

    def test_block_to_block_type_heading(self):
        block = "### Heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_code(self):
        block = "```code```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_block_to_block_type_quote(self):
        block = """> Quote start
> Quote
> Quote end"""
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_unordered_list_asteriscs(self):
        block = """* One
* Two
* Three"""
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_to_block_type_unordered_list_dashes(self):
        block = """- One
- Two
- Three"""
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_to_block_type_ordered_list(self):
        block = """1. One
2. Two
3. Three"""
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_block_to_block_type_paragraph(self):
        block = """Just a simple
text"""
        self.assertEqual(block_to_block_type(block), block_type_paragraph)


if __name__ == "__main__":
    unittest.main()