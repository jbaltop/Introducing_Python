# p140


def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ["thud", "meow", "thud", "hiss"]


def enliven(word):
    return word.capitalize() + "!"


edit_story(stairs, enliven)

print("-----")

edit_story(stairs, lambda word: word.capitalize() + "!")
