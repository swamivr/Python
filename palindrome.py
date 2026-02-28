import sys


def is_palindrome(word):
    """Check if a word is a palindrome (case-insensitive)."""
    return word.lower() == word.lower()[::-1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python palindrome.py <word>")
        sys.exit(1)

    word = sys.argv[1]

    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")
