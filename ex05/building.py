import sys


def main(argv):
    """ex05"""
    num_of_args = len(argv)
    try:
        assert num_of_args <= 2, 'more than one argument is provided'
    except AssertionError as e:
        print('{}: {}'.format(str(type(e).__name__), str(e)))
    input_string = ''
    if num_of_args == 1:
        while input_string == '':
            input_string = input('What is the text to count?\n')
    else:
        input_string = sys.argv[1]
    char_types = [
        'upper letters',
        'lower letters',
        'punctuation marks',
        'spaces',
        'digits'
        ]
    count = dict()
    for char_type in char_types:
        count[char_type] = 0
    for char in input_string:
        if str(char).isdigit():
            count['digits'] += 1
        elif str(char).islower():
            count['lower letters'] += 1
        elif str(char).isupper():
            count['upper letters'] += 1
        elif str(char).isspace():
            count['spaces'] += 1
        else:
            count['punctuation marks'] += 1
    for char_type in char_types:
        value = str(count[char_type])
        print('{} {}'.format(value, char_type))


if __name__ == '__main__':
    main(sys.argv)
