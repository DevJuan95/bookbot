from stats import get_num_words, get_chars_count, get_book_text


def main():
    book_text = get_book_text()
    num_words = get_num_words(book_text)
    char_count_map = get_chars_count(book_text)

    print(f"{num_words} words found in the document")
    for char in char_count_map:
        print(f"'{char}': {char_count_map[char]}")

main()