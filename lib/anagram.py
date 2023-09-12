class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, strings):
        return [strings for strings in strings if sorted(strings.lower()) == sorted(self.word.lower()) and strings.lower() != self.word.lower()]
