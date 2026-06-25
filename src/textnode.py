from enum import Enum


class TextType(Enum):
    TEXT = 'plain'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE_TEXT = 'code'
    LINKS = 'url_links'
    IMAGES = 'url_images'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

