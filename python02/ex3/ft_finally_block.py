
def water_plants(plant_list):
    error = 0
    try:
        print("Opening watering system")
        
        for plante in plant_list:
            if not isinstance(plante, str):
                error = 1
                raise ValueError(f"Error: Cannot water {plante} - invalid plant!")
            
            print(f"Watering : {plante}")
            
    except ValueError as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")
        if error != 1:
            print("Watering completed successfully!")

def test_watering_system():
    """
    Runs tests to demonstrate how the system handles success and errors.
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    good_plants = ["Rose", "Lily", "Cactus"]
    water_plants(good_plants)

    print("\nTesting with error...")
    bad_plants = ["Sunflower", 123, "Daisy"]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()