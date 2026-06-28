class TIMDERLayers:
    """
    Warstwy Λ–τ–ρ:
    Λ — struktura
    τ — transformacja
    ρ — defekt
    """

    def apply_structure(self, data):
        return [x + 1 for x in data]

    def reverse_structure(self, data):
        return [x - 1 for x in data]

    def apply_transform(self, data):
        return [x * 2 for x in data]

    def reverse_transform(self, data):
        return [x // 2 for x in data]

    def apply_defect(self, data):
        return [x + (i % 3) for i, x in enumerate(data)]

    def reverse_defect(self, data):
        return [x - (i % 3) for i, x in enumerate(data)]
