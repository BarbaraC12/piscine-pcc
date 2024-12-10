import sys
import time
from tqdm import tqdm
from time import sleep
import shutil


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def format_time(seconds):
    """Format seconds into HH:MM:SS or MM:SS depending on duration."""
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    if hours > 0:
        return f"{hours:02}:{mins:02}:{secs:02}"
    return f"{mins:02}:{secs:02}"


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()

    def get_terminal_width():
        return shutil.get_terminal_size().columns

    def print_bar(it):
        percent = (100 * (it / float(total)))
        elapsed_ti = time.time() - start_time
        speed = (it / elapsed_ti) if elapsed_ti > 0 else 0  # it/s
        eta = (total - it) / speed if speed > 0 else 0

        length = get_terminal_width() - 45  # Adjust bar len to width term
        fill_len = int(length * it // total)
        bar = '█' * fill_len + '-' * (length - fill_len)

        # Format output line
        sys.stdout.write(
            f"\r{percent:6.0f}%| {bar} | {it}/{total} "
            f"[{format_time(elapsed_ti)}<{format_time(eta)}, {speed:6.2f}it/s]"
        )
        sys.stdout.flush()

    for i, _ in enumerate(lst, 1):
        print_bar(i)
        yield _

    sys.stdout.write('\n')  # Move to the next line when finished
    sys.stdout.flush()
