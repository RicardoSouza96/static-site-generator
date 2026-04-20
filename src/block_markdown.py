from enum import Enum
from textnode import TextType, TextNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    nodes = markdown.split("\n\n")
    filtered_nodes = []
    for node in nodes:
        if node == "":
            continue
        filtered_nodes.append(node.strip())
    return filtered_nodes

def block_to_block_type(block):
    lines = block.split("\n")
    if(block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### "))):
        return BlockType.HEADING
    if(all(line.startswith((">")) for line in lines)):
        return BlockType.QUOTE
    if(all(line.startswith("- ") for line in lines)):
        return BlockType.UNORDERED_LIST
    if(all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1))):
        return BlockType.ORDERED_LIST
    if(len(lines) > 1 and (lines[0].startswith("```") and lines[-1].startswith("```"))):
        return BlockType.CODE
    else:
        return BlockType.PARAGRAPH