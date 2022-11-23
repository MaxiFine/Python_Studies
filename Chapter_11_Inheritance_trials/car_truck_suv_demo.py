# This program creates a Car object, a Truck object, and SUV object

import inheritance_vehicles_demo


def main():
    # Create a Car object for a used bmw 2001
    # 70000, 15000, 4
    car = inheritance_vehicles_demo.Car('BMW', 2001, 70000, 15000, 4)

    # Create a Truck object for a used 2002
    truck = inheritance_vehicles_demo.Truck('Toyota', 2002, 40000, 12000, '4WD')

    # Create an SUV object for a used
    suv = inheritance_vehicles_demo.SUV('Volvo', 2000, 30000, 18500, 5)

    print('USED CAR INVENTORY')
    print('======================')

    # Display the car's data
    print('The following car is in inventory:')
    print('Make:', car.get_make())
    print('Model:', car.get_model())
    print('Mileage:', car.get_mileage())
    print('Price:', car.get_price())
    print('Number of Doors:', car.get_doors())
    print()

    # Display the Truck's data
    print('The following pickup truck is in inventory')
    print('Make:', truck.get_make())
    print('Model:', truck.get_model())
    print('Mileage:', truck.get_mileage())
    print('Price:', truck.get_price())
    print('Drive Type:', truck.get_drive_type())
    print()

    # Display the SUV's data
    print('The following suv is in inventory')
    print('Make:', suv.get_make())
    print('Model:', suv.get_model())
    print('Mileage:', suv.get_mileage())
    print('Price:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())


main()
