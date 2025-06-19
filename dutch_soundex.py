from soundex import Soundex


class DutchSoundex(Soundex):
    """
    """

    def __init__(self):
        super().__init__()
        self.length = 4
        self.mapping = {"b": "0",
                        "p": "0",
                        "d": "1",
                        "t": "1",
                        "f": "2",
                        "v": "2",
                        "w": "2",
                        "g": "3",
                        "k": "4",
                        "c": "4",
                        "q": "4",
                        "x": "5",
                        "l": "6",
                        "m": "7",
                        "n": "7",
                        "r": "8",
                        "s": "9",
                        "z": "9"}

    def preprocess(self, name):
        name = str(name).lower()
        name = name.replace("ch", "g")
        name = name.replace("ck", "k")
        name = name.replace("ks", "x")
        name = name.replace("sj", "s")
        name = name.replace("ng", "n")
        return name
