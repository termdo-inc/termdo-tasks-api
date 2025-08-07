def snake_to_camel_case(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(part.title() for part in words[1:])
