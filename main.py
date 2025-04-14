from stats import char_dict_to_sorted_dict_list, text_to_num_words

def main():
    book_path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {text_to_num_words()} total words")
    print("--------- Character Count -------")

    sorted_list = char_dict_to_sorted_dict_list()
    char_dict_to_sorted_dict_list()
    for char_dict in sorted_list:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
            
    print("============= END ===============")

main()