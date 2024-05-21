import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


def split_nodes_delimeter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Matching closing delimeter {delimiter} not found: {node.text}")
        for idx, part in enumerate(parts):
            if not part: continue
            split_nodes.append(TextNode(part, text_type_text if idx % 2 == 0 else text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        text = node.text
        for alt_text, url in images:
            sections = text.split(f"![{alt_text}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0]:
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(alt_text, text_type_image, url))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        text = node.text
        for alt_text, url in links:
            sections = text.split(f"[{alt_text}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0]:
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(alt_text, text_type_link, url))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, text_type_text))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimeter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimeter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimeter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
