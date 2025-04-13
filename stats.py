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