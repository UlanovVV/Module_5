class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_number_of_floors(self, floors):
        self.number_of_floors = floors
        print(self.number_of_floors)

h1 = House()
h1.set_number_of_floors(6)