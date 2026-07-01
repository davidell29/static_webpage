from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
