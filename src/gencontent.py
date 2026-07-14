import os
from pathlib import Path

from block_markdown import markdown_to_html_node, markdown_to_blocks

def extract_title(markdown) -> str:
    nodes = markdown_to_blocks(markdown)
    for node in nodes:
        if node.startswith("# "):
            return node[2:].strip()
    raise Exception("There's no h1 header")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_content = f.read()
    with open(template_path) as f:
        template_content = f.read()
    html_string = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_string)
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_content)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    """contents = []
    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, dest_dir_path)
    else:
        contents = os.listdir(dir_path_content)
        for content in contents:
            if os.path.isfile(os.path.join(dir_path_content, content)):
                new_file_name = os.path.splitext(content)[0] + ".html"
                generate_page(os.path.join(dir_path_content, content), template_path, os.path.join(dest_dir_path, new_file_name))
            else:
                generate_pages_recursive(os.path.join(dir_path_content, content), template_path, os.path.join(dest_dir_path, content))"""
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)