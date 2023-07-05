import sys

num_of_args = len(sys.argv)
try:
    assert num_of_args <= 2, 'more than one argument is provided'
    if num_of_args == 2:
        assert sys.argv[1].lstrip(' -+').strip().isdigit(), 'argument is not an integer'
        value = int(sys.argv[1])
        if value % 2 == 0:
            print('I\'m Even.')
        else:
	        print('I\'m Odd.')
except AssertionError as e:
    print('{}: {}'.format(str(type(e).__name__), str(e)))
