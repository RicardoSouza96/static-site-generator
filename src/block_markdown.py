from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

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

def markdown_to_html_node(markdown):
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            nodes.append(heading_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            nodes.append(quote_to_html_node(block))
        elif block_type == BlockType.ORDERED_LIST:
            nodes.append(ordered_list_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
            nodes.append(unordered_list_to_html_node(block))
        elif block_type == BlockType.PARAGRAPH:
            nodes.append(paragraph_to_html_node(block))
        elif block_type == BlockType.CODE:
            nodes.append(code_to_html_node(block))
        else:
            raise ValueError("invalid block type")
    return ParentNode("div", nodes)

def heading_to_html_node(block):
    count = 0
    for ch in block:
        if ch == "#":
            count += 1
        else:
            break
    if count + 1 >= len(block):
        raise ValueError(f"invalid heading level: {count}")
    text = block[count:].lstrip()
    children = text_to_children(text)
    return ParentNode(f"h{count}", children)

def quote_to_html_node(block):
    lines = block.split("\n")
    quotes = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        quotes.append(line[1:].lstrip())
    children = text_to_children(" ".join(quotes))
    return ParentNode("blockquote", children)

def ordered_list_to_html_node(block):
    items = block.split("\n")
    li_nodes = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ol", li_nodes)

def unordered_list_to_html_node(block):
    items = block.split("\n")
    li_nodes = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ul", li_nodes)

def paragraph_to_html_node(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    return ParentNode("p", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    text_node = TextNode(text, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    code = ParentNode("code", [html_node])
    return ParentNode("pre", [code])

def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes