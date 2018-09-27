# p156


def get_description():
    """Return random weather, just like the pros"""
    import random

    possibilities = ["rain", "snow", "sleet", "fog", "sun", "who knows"]
    return random.choice(possibilities)


print(get_description())
