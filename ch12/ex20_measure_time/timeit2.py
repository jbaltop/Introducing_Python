# p424

from timeit import repeat

print(repeat("num = 5; num *= 2", number=1, repeat=3))

# this task is too simple, so sometimes it takes 0 seconds to complete.
