import sys


NESTED_MORSE = {
  ' ': '/',
  'A':'.-', 'B':'-...',
	'C':'-.-.', 'D':'-..', 'E':'.',
	'F':'..-.', 'G':'--.', 'H':'....',
	'I':'..', 'J':'.---', 'K':'-.-',
	'L':'.-..', 'M':'--', 'N':'-.',
	'O':'---', 'P':'.--.', 'Q':'--.-',
	'R':'.-.', 'S':'...', 'T':'-',
	'U':'..-', 'V':'...-', 'W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.',
	'0':'-----'
  }

def is_not_morse_char(char) -> bool:
    return str(char).upper() not in NESTED_MORSE.keys()

def main(argv) -> None:
    num_of_args = len(sys.argv)
    try:
        assert num_of_args == 2, 'the arguments are bad'
        string = sys.argv[1]
        not_morse_chars = list(filter(is_not_morse_char, string))
        assert len(not_morse_chars) == 0, 'the arguments are bad'
        morse_string = ''
        for char in string:
            morse_string += '{} '.format(NESTED_MORSE[str(char).upper()])
        print('{}'.format(morse_string[:-1]))
    except AssertionError as e:
        print('{}: {}'.format(str(type(e).__name__), str(e)))
    except Exception as e:
        print('Jussi, 0 points. Error: {}'.format(str(e)))

if __name__ == '__main__':
    main(sys.argv)
