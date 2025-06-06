from stats import count_words, count_letters,sorting
import sys

def main():
 if len(sys.argv) < 2:
   print("Usage: python3 main.py <path_to_book>")
   return sys.exit(1)
 
 print("============ BOOKBOT ============")
 print("Analyzing book found at books/frankenstein.txt...")

 content = get_book_text(sys.argv[1])
 word_count = count_words(content)
 char_counts = count_letters(content)
 sorted_chars = sorting(char_counts, word_count)

 print("----------- Word Count ----------")
 print(f"Found {word_count} total words")

 print("--------- Character Count -------")
 for item in sorted_chars:
   print(f"{item['char']}: {item['num']}")
 
 print("============= END ===============")


def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents


main()