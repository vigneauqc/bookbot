import sys
from stats import get_num_words
from stats import get_characters_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {sys.argv[1]}...')
        print('----------- Word Count ----------')

        get_num_words(f"/home/vigne/workspace/github/vigneauqc/bookbot/{sys.argv[1]}")

        print('--------- Character Count -------')

        get_characters_count(f"/home/vigne/workspace/github/vigneauqc/bookbot/{sys.argv[1]}")

        print('============= END ===============')

main()