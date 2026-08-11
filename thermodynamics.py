from file_manager import save_history


def thermodynamics_menu():
    print("\n========== Thermodynamics ==========")
    print("1. Ideal Gas Law")
    print("2. Boyle's Law")
    print("3. Charles's Law")
    print("4. Combined Gas Law")
    print("5. Specific Heat")
    print("6. Enthalpy Change")
    print("7. Back")


def thermodynamics(eng):

    while True:

        thermodynamics_menu()

        choice = input("Choose an option: ")

        # =========================
        # Ideal Gas Law
        # =========================
        if choice == "1":

            try:
                pressure = float(input("Pressure (Pa): "))
                volume = float(input("Volume (m³): "))
                temperature = float(input("Temperature (K): "))

                result = eng.ideal_gas_law(
                    pressure,
                    volume,
                    temperature
                )

                print("Moles =", result)

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # =========================
        # Boyle's Law
        # =========================
        elif choice == "2":

            try:
                pressure1 = float(input("Initial Pressure (Pa): "))
                volume1 = float(input("Initial Volume (m³): "))
                volume2 = float(input("Final Volume (m³): "))

                result = eng.boyles_law(
                    pressure1,
                    volume1,
                    volume2
                )

                print("Final Pressure =", result, "Pa")

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # =========================
        # Charles's Law
        # =========================
        elif choice == "3":

            try:
                volume1 = float(input("Initial Volume (m³): "))
                temperature1 = float(input("Initial Temperature (K): "))
                temperature2 = float(input("Final Temperature (K): "))

                result = eng.charles_law(
                    volume1,
                    temperature1,
                    temperature2
                )

                print("Final Volume =", result, "m³")

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "4":

            try:
                pressure1 = float(input("Initial Pressure (Pa): "))
                volume1 = float(input("Initial Volume (m³): "))
                temperature1 = float(input("Initial Temperature (K): "))
                volume2 = float(input("Final Volume (m³): "))
                temperature2 = float(input("Final Temperature (K): "))

                result = eng.combined_gas_law(
                    pressure1,
                    volume1,
                    temperature1,
                    volume2,
                    temperature2
                )

                print("Final Pressure =", result, "Pa")

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":

            try:
                mass = float(input("Mass (kg): "))
                specific_heat_capacity = float(
                    input("Specific Heat Capacity (J/kg·K): ")
                )
                temperature_change = float(
                    input("Temperature Change (K or °C): ")
                )

                result = eng.specific_heat(
                    mass,
                    specific_heat_capacity,
                    temperature_change
                )

                print("Heat Energy =", result, "J")

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "6":

            try:
                mass = float(input("Mass (kg): "))
                cp = float(input("Specific Heat Capacity Cp (J/kg·K): "))
                temperature_change = float(input("Temperature Change (K): "))

                result = eng.enthalpy_change(
                    mass,
                    cp,
                    temperature_change
                )

                print("Enthalpy Change =", result, "J")

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "7":
            break

        else:
            print("Invalid choice.")