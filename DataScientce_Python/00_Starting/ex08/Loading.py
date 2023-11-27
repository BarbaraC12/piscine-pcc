import sys
import time
import sutil


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()
    ecriture = "...%|| .../... [....<.... secs]'"
    def get_terminal_width():
        return shutil.get_terminal_size().columns

    def print_bar(it):
        percent = ("{0:.0f}").format(100 * (it / float(total)))
        fill_len = int(length * it // total)
        bar = '█' * fill_len + '-' * (length - fill_len)

        elapsed_time = time.time() - start_time
        t_remain = round((elapsed_time / it if it else 0) * it, 2)
        eta = round((elapsed_time / it) * (total - it), 2)
        trunc = ("{0:.0f}").format(truncate(it, -1))
        ecriture = f'\r{percent}%|| {trunc}/{total} [{t_remain}<{eta} secs]'
        sys.stdout.write(f'\r{percent}%|{bar}| {trunc}/{total} [{t_remain}<{eta} secs]')
        sys.stdout.flush()

    length = get_terminal_width() - len(ecriture)

    for i, _ in enumerate(lst, 1):
        percent = ("{0:.1f}").format(100 * (i / float(total)))
        fill_len = int(length * i // total)
        bar = '█' * fill_len + '-' * (length - fill_len)

        print_bar(i)

        yield _

    # sys.stdout.write('\n')
    sys.stdout.flush()
