from agents import function_tool

@function_tool
def word_counter(text: str) -> int:
    """Counts the number of words in a text."""
    return len(text.split())