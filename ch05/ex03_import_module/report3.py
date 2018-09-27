# p156

import random


def get_description():
    """Return random weather, just like the pros"""

    possibilities = ["rain", "snow", "sleet", "fog", "sun", "who knows"]
    return random.choice(possibilities)


print(get_description())
