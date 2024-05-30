import re


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")
    if bool(re.match(r"^[#]{1,6} ", block)):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if lines and all([line.startswith(">") for line in lines]):
        return block_type_quote
    if lines and (all([line.startswith("* ") for line in lines]) or all([line.startswith("- ") for line in lines])):
        return block_type_unordered_list
    if lines and all([line.startswith(f"{idx+1}. ") for idx, line in enumerate(block.split("\n"))]):
        return block_type_ordered_list
    return block_type_paragraph


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks