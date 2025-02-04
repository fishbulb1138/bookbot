def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_characters(text)
    print(num_words)
    print(chars_dict)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    lc_book = text.lower()
    for char in lc_book:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()


