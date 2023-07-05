import sys

def count_num_of_words(string, num_of_chars) -> list:
    new_list = [x for x in string if ]
    return

def main(argv) -> None:
    num_of_args = len(sys.argv)
    try:
        assert num_of_args == 3, 'the arguments are bad'
        assert sys.argv[2].lstrip(' +').strip().isdigit(), 'the arguments are bad'
    except AssertionError as e:
        print('{}: {}'.format(str(type(e).__name__), str(e)))


if __name__ == '__main__':
    main(sys.argv)
