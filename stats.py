def get_num_words():
    text = get_book_text()
    words = text.split()
    word_count = 0
    for word in words:
        if word:
            word_count += 1
    print(f"{word_count} words found in the document")

def get_book_text():
    with open("books/frankenstein.txt") as f:
      file_contents = f.read()
    return file_contents

def get_char_count():
    text = get_book_text().lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def sort_dict(char_count_dict):
    dict_list = []
    for char, count in char_count_dict.items():
        dict_list.append({"character": char, "count": count})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list