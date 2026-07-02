from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(markdown):
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    result = markdown.split('\n')
    if all(line.startswith(">") for line in result):
        return BlockType.QUOTE
    if all(linie.startswith("- ") for linie in result):
        return BlockType.UNORDERED_LIST
    for i, linies in enumerate(result, start=1):
        if not linies.startswith(str(i) + ". "):
            return BlockType.PARAGRAPH
    return BlockType.ORDERED_LIST
        
