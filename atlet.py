class Atlet:
    def __init__(self, ism, sport, yosh):
        self.ism = ism
        self.sport = sport
        self.yosh = yosh
        print("Sportchini Ma'lumotlari")
    

    def malumot(self):
        print(self.ism, self.sport, self.yosh)

s1 = Atlet(ism="Ollayor",sport="Kurash", yosh=17)

s1.malumot()