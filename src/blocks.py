def markdown_to_blocks(markdown):
    splinter = markdown.split("\n\n")
    result = []
    for split in splinter:
        split = split.strip()
        if not split:
            continue
        result.append(split.strip())
    return result