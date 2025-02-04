def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_characters(text)
    chars_report = char_report(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for char_dict in chars_report:
        print(f"The '{char_dict['char']}' character was found '{char_dict['count']}' times")
    

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

def sort_on(dict):
    return dict["count"]

def char_report(dict):
    character_report = []
    for char, count in dict.items():
        if char.isalpha():
            character_report.append({"char": char, "count": count})
    character_report.sort(reverse=True, key=sort_on)
    return character_report



main()


