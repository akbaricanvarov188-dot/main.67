class Oquvchi:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def malumot(self):
        print(f"Ism: {self.ism}")
        print(f"Yosh: {self.yosh}")


oquvchi = Oquvchi("Akbar", 16)
oquvchi.malumot()


class Telefon:
    def __init__(self, brend, model, narx):
        self.brend = brend
        self.model = model
        self.narx = narx

    def malumot(self):
        print(f"Brend: {self.brend}")
        print(f"Model: {self.model}")
        print(f"Narx: {self.narx}")


telefon = Telefon("Xiaomi", "Redmi A3x", 1000000)
telefon.malumot()

class Mashina:
    def __init__(self, model, rang, tezlik):
        self.model = model
        self.rang = rang
        self.tezlik = tezlik

    def yurish(self):
        print(f"{self.model} {self.tezlik} km/soat tezlikda yurmoqda")


mashina = Mashina("BMW", "Qora", 200)
mashina.yurish()


class Hayvon:
    def __init__(self, ism):
        self.ism = ism

    def malumot(self):
        print(f"Hayvon: {self.ism}")


class Mushuk(Hayvon):
    def miyovlash(self):
        print("Miyov-miyov!")


mushuk = Mushuk("Mosh")
mushuk.malumot()
mushuk.miyovlash()