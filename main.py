

def read_book(file):
    with open(file) as book:
        return book.read()

def word_count(book):
    words = book.split()
    return len(words)

def character_count(book: str):
    characters: dict[str, int] = {}
    for character in [character for character in book]:
        if not character.isalpha(): continue
        if character.lower() in characters:
            characters[character.lower()] += 1
        else:
            characters[character.lower()] = 1
    return characters

def character_report(file: str, characters: dict[str, int], num_words):
    keys = sorted(characters.keys())
    print(f"--- Begin report of {file} ---")
    print(f"{num_words} words found in the document")
    print()
    for key in keys:
        print(f"The '{key}' character was found {characters[key]} times")
    print("--- End report ---")

if __name__ == '__main__':
    book = read_book("books/frankenstein.txt")
    count = word_count(book)
    characters = character_count(book)
    print(count)
    print(characters)
    report = character_report("books/frankenstein.txt", characters, count)
