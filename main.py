from stats import get_num_words, get_char_count, sort_on, sort_dict

def main():
    get_num_words()

    char_count = get_char_count()
    sorted_list = sort_dict(char_count)

    for char_dict in sorted_list:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

main()