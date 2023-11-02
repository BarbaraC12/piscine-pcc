import sys
import time
from math import floor


class ProgressBar:
    """
    This class allows you to make easily a progress bar.
    """
    def __init__(self, steps, maxbar=50):
        if steps <= 0 or maxbar <= 0 or maxbar > 100:
            raise ValueError
        self.steps = steps
        self.maxbar = maxbar
        self.perc = 0
        self._completed_steps = 0
        self.status = 0
        self.update()

    def update(self, increase=True):
        if increase:
            self._completed_steps += 1
        self.perc = floor(self._completed_steps / self.steps * 100)
        if self._completed_steps > self.steps:
            self._completed_steps = self.steps
        steps_bar = floor(self.perc / 100 * self.maxbar)
        if steps_bar == 0:
            visual_bar = self.maxbar * ' '
        else:
            visual_bar = (steps_bar - 1) * '-' + '>' + (self.maxbar - steps_bar) * ' '
            self.status = int(self.maxbar * self.perc / 100)


        sys.stdout.write(f"\r{str(self.perc)} %\t|[ {visual_bar} ]| {self.status}/{self.maxbar}")
        sys.stdout.flush()


if __name__ == '__main__':
    bar = ProgressBar(50, 100)

    i = 0
    while bar.perc != 100:
        bar.update()
        time.sleep(0.5)
        i += 1
