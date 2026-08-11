from file_manager import save_history


def heat_transfer_menu():

    print("\n========== Heat Transfer ==========")
    print("1. Heat Conduction")
    print("2. Heat Convection")
    print("3. Heat Radiation")
    print("4. Overall Heat Transfer Coefficient")
    print("5. Back")


def heat_transfer(eng):

    while True:

        heat_transfer_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                k = float(input("Thermal Conductivity (W/mK): "))
                area = float(input("Area (m²): "))
                t1 = float(input("Hot Temperature (K): "))
                t2 = float(input("Cold Temperature (K): "))
                thickness = float(input("Thickness (m): "))

                result = eng.heat_conduction(
                    k,
                    area,
                    t1,
                    t2,
                    thickness
                )

                print("Heat Transfer Rate =", result, "W")
                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "2":
            try:
                h = float(input("Heat Transfer Coefficient (W/m²K): "))
                area = float(input("Area (m²): "))
                surface_temperature = float(input("Surface Temperature (K): "))
                fluid_temperature = float(input("Fluid Temperature (K): "))

                result = eng.heat_convection(
                    h,
                    area,
                    surface_temperature,
                    fluid_temperature
                )

                print("Heat Transfer Rate =", result, "W")
                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                emissivity = float(input("Emissivity: "))
                area = float(input("Area (m²): "))
                surface_temperature = float(input("Surface Temperature (K): "))
                surrounding_temperature = float(input("Surrounding Temperature (K): "))

                result = eng.heat_radiation(
                    emissivity,
                    area,
                    surface_temperature,
                    surrounding_temperature
                )

                print("Heat Transfer Rate =", result, "W")
                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "4":
            try:
                heat_rate = float(input("Heat Transfer Rate (W): "))
                area = float(input("Heat Transfer Area (m²): "))
                temperature_difference = float(input("Temperature Difference (K): "))

                result = eng.overall_heat_transfer_coefficient(
                    heat_rate,
                    area,
                    temperature_difference
                )

                print("Overall Heat Transfer Coefficient =", result, "W/m²K")
                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":
            break

        else:
            print("Invalid option.")