def count_words(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents


def sort_on(dict):
    return dict["number"]


def count_characters(text):
    char_count = {}
    words = text.split()
    for word in words:
        for character in word:
            character = character.lower()
            if (character not in char_count) and (character.isalpha()):
                char_count[character] = 1
            elif character.isalpha():
                char_count[character] += 1
    return char_count


def sort_char_count(char_count):
    sorted_char_count = []
    for entry in char_count:
        sorted_char_count.append({"character": entry, "number": char_count[entry]})
    sorted_char_count.sort(key=sort_on, reverse=True)
    return sorted_char_count


def print_count_report(book_path, num_words, sorted_char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document")
    print()
    for entry in sorted_char_count:
        print(f"The '{entry['character']}' character was found {entry['number']} times")
    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"

    file_contents = get_text(book_path)

    num_words = count_words(file_contents)

    char_count = count_characters(file_contents)

    sorted_char_count = sort_char_count(char_count)

    print_count_report(book_path, num_words, sorted_char_count)


main()
