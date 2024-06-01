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

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>"
        )

    def test_headings(self):
        md = """
# Heading with **bolded** text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading with <b>bolded</b> text</h1></div>"
        )

    def test_quote(self):
        md = """
>This is a quote
>with *italic* text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <i>italic</i> text</blockquote></div>"
        )

    def test_code(self):
        md = """
```
This is a code block
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is a code block</code></pre></div>"
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3 *(additional)*
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3 <i>(additional)</i></li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. Item 1
2. Item 2
3. Item 3 **important**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3 <b>important</b></li></ol></div>"
        )


if __name__ == "__main__":
    unittest.main()