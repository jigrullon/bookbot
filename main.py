def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    character_count = get_character_count(text)
    sorted_list = chars_dict_to_sorted_list(character_count)
    for char in sorted_list:
        print(f"The {char['char']} character was found {char['num']} times")
    print(f"--- End report of {book_path} ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_character_count(text):
    lowered_string = text.lower()
    character_count = {}
    for char in lowered_string:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1
    return character_count

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

main()