filepath = './books/frankenstein.txt'

def get_book_text() -> str:
    with open(filepath, 'r') as f:
        return f.read()

def get_num_words(book_text: str):
    words = book_text.split()
    return len(words)

def get_chars_count(book_text: str):
    counter = {}
    for char in book_text.lower():
        counter[char] = counter.get(char, 0) + 1
    return counter

def sort_char_count(counter: dict[str, int])-> list[dict[str, int]]:
    arr = []
    for char, count in counter.items():
        arr.append({"letter": char, "count": count})
    arr.sort(key=lambda x: x["count"], reverse=True)
    return arr