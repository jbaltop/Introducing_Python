import multiprocessing
import os
import time
import random


def now():
    r = random.randint(1, 5)
    time.sleep(r)
    print(
        "process {}: waited {} second(s). current time is {}.".format(
            os.getpid(), r, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        )
    )


if __name__ == "__main__":
    print("\nplease wait for a moment.\n")
    for n in range(3):
        p = multiprocessing.Process(target=now)
        p.start()
