def read_book(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    text = text.lower()
    character_dict = {}
    for character in text:
        if character in character_dict:
            character_dict[character] += 1
        else: character_dict[character] = 1
    return character_dict

def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    count = word_count(text)
    letter_count_dict = letter_count(text)
    print("-- Begin report of " + path)
    print("\n %s words were found in the document" % (count))

main()