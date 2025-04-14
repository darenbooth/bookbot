import sys
from stats import char_dict_to_sorted_dict_list, text_to_num_words, get_book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    #book_path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {text_to_num_words(book_path)} total words")
    print("--------- Character Count -------")

    sorted_list = char_dict_to_sorted_dict_list(book_path)
    char_dict_to_sorted_dict_list(book_path)
    for char_dict in sorted_list:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
            
    print("============= END ===============")

main()