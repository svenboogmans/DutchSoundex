class Soundex:
    """
    """

    def __init__(self):
        self.length = 4
        self.mapping = {"b": "1",
                        "f": "1",
                        "p": "1",
                        "v": "1",
                        "c": "2",
                        "g": "2",
                        "j": "2",
                        "k": "2",
                        "q": "2",
                        "s": "2",
                        "x": "2",
                        "z": "2",
                        "d": "3",
                        "t": "3",
                        "l": "4",
                        "m": "5",
                        "n": "5",
                        "r": "6"}

    def preprocess(self, name):
        return str(name).lower()

    def calculate(self, name):
        name = self.preprocess(name)
        soundex_code = ""
        soundex_code += name[0]
        prev_digit = ""
        for letter in name[1:]:
            if len(soundex_code) == self.length:
                return soundex_code
            elif letter in self.mapping.keys():
                digit = self.mapping[letter]
                if digit != prev_digit:
                    soundex_code += self.mapping[letter]
                    prev_digit = digit
            else:
                prev_digit = ""
        if len(soundex_code) < self.length:
            soundex_code += "0" * (self.length - len(soundex_code))
        return soundex_code
