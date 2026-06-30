def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_listen = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_listen.append(old_node)
            continue
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdown syntax")
        for i in range(len(sections)):
            if i % 2 == 0:
                new_listen.append(TextNode(sections[i], TextType.TEXT))
            else:
                new_listen.append(TextNode(sections[i], text_type))
    return new_listen


    
