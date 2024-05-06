def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    count = word_count(text)
    dictionary = letter_count(text)
    sorted_list = create_sorted_list(dictionary)
    print(f"--- Begin report of {path} ---")
    print(f"{count} words were found in the document" )
    print()
    for item in sorted_list:
        print(item['letter'])

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
        if character.isalpha():
            if character in character_dict:
                character_dict[character] += 1
            else: character_dict[character] = 1
    return character_dict

def sort_data_by(d):
    return d['num']

def create_sorted_list(character_dict):
    sorted_list = []
    for char in character_dict:
        sorted_list.append({"letter": char, "num": character_dict[char]})
    sorted_list.sort(reverse=True, key=sort_data_by)
    return sorted_list
    

main()