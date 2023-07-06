import sys


def ft_tqdm(lst: range) -> None:
    # your code here
    OKBLUE = '\033[98m'
    ENDC = '\033[0m'
    for i in lst:
        # print(end=LINE_CLEAR)
        percentage = int(100 * (i + 1) / len(lst))
        num_of_chars = int(percentage * 1.27)
        total_num = 127
        if i < 100:
            total_num += 1
        print('{:>3}%|{}{}{}{}| {}/{}  '.format(str(percentage), OKBLUE, '█' * num_of_chars, ENDC, ' ' * (total_num - num_of_chars), str(i + 1), str(len(lst))), flush=True)
        print("\033[F", end='', flush=True)
        yield i
