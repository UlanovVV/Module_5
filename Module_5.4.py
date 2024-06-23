
class Building:
    total = 0

    def __init__(self):
        Building.total += 1

buildings = []
for _ in range(40):
    buildings.append(Building())

for building in buildings:
    print(building)

print(f"Всего создано {Building.total} объектов Building.")