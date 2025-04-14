def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def text_to_num_words():
    word_count = 0
    book_text = get_book_text()
    words = book_text.split()
    for word in words:
        word_count += 1
    return word_count

def text_to_num_chars():
    char_count_dict = {}
    chars = get_book_text().lower()
    for char in chars:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_dict(dict):
    return dict["count"]

def char_dict_to_sorted_dict_list():
    char_count_dict = text_to_num_chars()
    sorted_list_dict = []
    for char, count in char_count_dict.items():
        sorted_list_dict.append({"character": char, "count": count})
    sorted_list_dict.sort(reverse=True, key=sort_dict)
    return sorted_list_dict