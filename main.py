
import sys

from stats import count_words, count_characters, organized_list, get_book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

main()

book_path = sys.argv[1]
text = get_book_text(book_path)
num_words = count_words(text)
char_dic = count_characters(text)
char_sort = organized_list(char_dic)


def print_report(book_path, num_words, char_sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("------------ Word Count --------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -----")
    for item in char_sort:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============ END ============")

print_report(book_path, num_words, char_sort)
