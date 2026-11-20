class Player:
    def __init__(self, name):
        self.name = name
        self.quvat = 100

    def use_energy(self, amount):
        self.quvat -= amount
        if self.quvat < 0:
            self.quvat = 0

    def show_status(self):
        print(f"O‘yinchi: {self.name}")
        print(f"Energiya: {self.quvat}")


player = Player('Hero')
player.use_energy(35)
player.show_status()