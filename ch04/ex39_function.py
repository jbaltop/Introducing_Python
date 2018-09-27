# p128


def commentary(color):
    if color == "red":
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == "bee purple":
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


comment = commentary("blue")
print(comment)
