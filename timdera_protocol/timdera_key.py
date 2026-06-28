class TIMDERKey:
    """
    Klucz J — dodawany przy każdym przejściu.
    Automat pobiera kolejne klucze jako część struktury.
    """

    def __init__(self, seed=1):
        self.seed = seed

    def compress(self, data):
        return [(x ^ self.seed) for x in data]

    def decompress(self, data):
        return [(x ^ self.seed) for x in data]

    def rotate(self):
        self.seed = (self.seed * 3) % 257
