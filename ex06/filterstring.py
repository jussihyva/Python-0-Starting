import sys
from ft_filter import ft_filter

def is_long_enough(string, num_of_chars) -> bool:
    return len(string) >= num_of_chars

def main(argv) -> None:
    num_of_args = len(sys.argv)
    try:
        assert num_of_args == 3, 'the arguments are bad'
        assert sys.argv[2].lstrip(' +').strip().isdigit(), 'the arguments are bad'
        string = sys.argv[1]
        num_of_chars = int(sys.argv[2])
        words = string.split()
        selected_words = ft_filter(lambda word: is_long_enough(word, num_of_chars), words)
        print(list(selected_words))
    except AssertionError as e:
        print('{}: {}'.format(str(type(e).__name__), str(e)))
    except Exception as e:
        print('Jussi, 0 points. Error: {}'.format(str(e)))

if __name__ == '__main__':
    main(sys.argv)
