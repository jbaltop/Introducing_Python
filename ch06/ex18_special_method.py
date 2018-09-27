# p189


class Word:
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word("ha")
second = Word("HA")
third = Word("eh")

print(first.equals(second))
print(first.equals(third))
