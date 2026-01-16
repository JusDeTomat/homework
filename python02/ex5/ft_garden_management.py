

class Plant():
    def __init__(self, name, water, sun):
        assert name == str(name), "name need to be in type str"
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager():
    def __init__(self):
        self.lst_plant = []
    
    def add_plant(self,plant):
        try:
            if not isinstance(plant,Plant):
                raise ValueError("Plant need to be type Plant")
            if (plant.name == ""):
                raise ValueError("Plant name cannot be empty!")
        except ValueError as e:
            print(f"Error adding plant: {e}")
        finally:
            self.lst_plant.append(plant)
            print(f"Added {plant.name} successfully")
        
    def water_plant(self):
        print("Opening watering system")
        for plant in self.lst_plant:
            print(f"Watering {plant.name} - success")
        print("Closing watering system (cleanup)")

    def check_plant_health(self):
        try:
            for plant in self.lst_plant:
                if (plant.water > 10):
                    raise ValueError(f"Water level {plant.water} is too high (max 10)")
                if (plant.water < 1):
                    raise ValueError(f"Water level {plant.water} is too low (min 1)")
                if (plant.sun > 12):
                    raise ValueError(f"Sunlight hours  {plant.sun} is too high (max 12)")
                if (plant.sun < 2):
                    raise ValueError(f"Sunlight hours  {plant.sun} is too low (min 2)")
        except ValueError as e:
            print(f"Error checking {plant.name}: {e}")
        finally:
            print(f"{plant.name}: healthy (water: {plant.water}, sun: {plant.sun})")

if (__name__ == "__main__"):
    tomat = Plant("Tomate",2,5)
    garden = GardenManager()
    garden.add_plant(tomat)
    print()
    garden.water_plant()
    print()
    garden.check_plant_health()
    print()
