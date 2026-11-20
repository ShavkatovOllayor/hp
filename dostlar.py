class Dostlar:
    def __init__(self, ism, raqam):
        self.ism = ism
        self.raqam = raqam

    def malumot(self):
        print(f"Ismi: {self.ism}")
        print(f"Raqam: {self.raqam}")

d1 = Dostlar(ism="Malika", raqam=2805)
d1.malumot()