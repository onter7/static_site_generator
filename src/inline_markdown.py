from textnode import (
    TextNode,
    text_type_text
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