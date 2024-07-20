def main():
    book_path = "books/frankenstein.txt"

    book_text = get_book_text(book_path)
    
    word_count = count_words(book_text)

    character_count = count_characters(book_text)

    sorted_char_count = sort_dictionary(character_count)

    print_report(book_path, word_count, sorted_char_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(string):
    words = string.split()
    return len(words)


def count_characters(string):
    char_count = {}
    for char in string:
        char_lower = char.lower()
        if char_lower.isalpha():
            if char_lower not in char_count:
                char_count[char_lower] = 1
            else:
                char_count[char_lower] += 1

    return char_count

def sort_on(dict):
    value = next(iter(dict.values()))
    return value

def sort_dictionary(dict):
    list_of_dicts = [{key: value} for key, value in dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def print_report(book_path, words, sorted_char_list):

    print(f"--- Begin report of {book_path} ---")

    print(f"There are {words} in this document.")
    
    for dict in sorted_char_list:
        for char, num in dict.items():
           print(f"The '{char}' character was found {num} times.")

    print("--- End Report ---")


main()