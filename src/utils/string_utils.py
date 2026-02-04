"""String utility functions."""


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a string.

    Args:
        text: The input string to process.

    Returns:
        String with each word capitalized.
    """
    return text.title()


def reverse_string(text: str) -> str:
    """Reverse a string.

    Args:
        text: The input string to reverse.

    Returns:
        The reversed string.
    """
    return text[::-1]


def count_vowels(text: str) -> int:
    """Count the number of vowels in a string.

    Args:
        text: The input string to analyze.

    Returns:
        The number of vowels (a, e, i, o, u) in the string.
    """
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)


def truncate(text: str, max_length: int) -> str:
    """Truncate a string to a maximum length.

    Args:
        text: The input string to truncate.
        max_length: Maximum length of the output string.

    Returns:
        Truncated string with '...' appended if it was shortened.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


# TODO: Implement a function to check if a string is a palindrome
# Function name: is_palindrome
# Should return True if the string reads the same forwards and backwards
# Should ignore spaces and be case-insensitive
