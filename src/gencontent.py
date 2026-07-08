import os

from block_markdown import markdown_to_html_node, markdown_to_blocks

def extract_title(markdown) -> str:
    nodes = markdown_to_blocks(markdown)
    for node in nodes:
        if node.startswith("# "):
            return node[2:].strip()
    raise Exception("There's no h1 header")

def generate_page(from_path: str, template_path: str, dest_path: str) -> str:
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