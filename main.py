from stats import get_num_words, get_num_char, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    num_words = get_num_words(get_book_text(sys.argv[1]))
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_char = get_num_char(get_book_text(sys.argv[1]))
    sorted_char = sort_dict(num_char)

    for i in sorted_char:
        if i["name"].isalpha():
            print(f"{i["name"]}: {i["num"]}")
        else:
            pass
    
    print("============= END ===============")


main()