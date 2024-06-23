
class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __int__(self):
        return f"{self.numberOfFloors}"

    def __str__(self):
        return f"{self.buildingType}"

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

building1 = Building(10, "Жилой")
building2 = Building(5, "Офисный")
building3 = Building(10, "Жилой")
print(building2)
print(building2 == building3)
print(building1 == building3)