# p191


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return "Word('" + self.text + "')"


first = Word("ha")

print(first)
