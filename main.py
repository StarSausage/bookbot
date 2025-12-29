from stats import get_num_words, count_characters,sort_list_words
import sys

def main():
    if(len(sys.argv)==2):
        print(sys.argv)
        book_path = sys.argv[1] 
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(book_path)
    characters = count_characters(text)
    num_words = get_num_words(text)
    sorted_words = sort_list_words(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for e in sorted_words:
        if e["char"].isalpha():
            print(f"{e["char"]}: {e["num"]}")
    print("============= END ===============")
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
main()






