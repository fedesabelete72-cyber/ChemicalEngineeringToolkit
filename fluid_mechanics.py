from file_manager import save_history


def fluid_mechanics_menu():
    print("\n========== Fluid Mechanics ==========")
    print("1. Reynolds Number")
    print("2. Flow Rate")
    print("3. Pipe Velocity")
    print("4. Pressure Drop")
    print("5. Bernoulli Equation")
    print("6. Back")


def fluid_mechanics(eng):

    while True:

        fluid_mechanics_menu()

        choice = input("Choose an option: ")

        if choice == "1":

            density = float(input("Density (kg/m³): "))
            velocity = float(input("Velocity (m/s): "))
            diameter = float(input("Diameter (m): "))
            viscosity = float(input("Viscosity (Pa·s): "))

            print(
                "Reynolds Number =",
                eng.reynolds_number(
                    density,
                    velocity,
                    diameter,
                    viscosity,
                ),
            )

            save_history(eng.history)

        elif choice == "2":

            area = float(input("Pipe Area (m²): "))
            velocity = float(input("Velocity (m/s): "))

            print(
                "Flow Rate =",
                eng.flow_rate(area, velocity),
                "m³/s",
            )

            save_history(eng.history)

        elif choice == "3":

            flow_rate = float(input("Flow Rate (m³/s): "))
            area = float(input("Pipe Area (m²): "))

            print(
                "Velocity =",
                eng.velocity(flow_rate, area),
                "m/s",
            )

            save_history(eng.history)

        elif choice == "4":

            friction = float(input("Friction Factor: "))
            length = float(input("Length (m): "))
            diameter = float(input("Diameter (m): "))
            density = float(input("Density (kg/m³): "))
            velocity = float(input("Velocity (m/s): "))

            print(
                "Pressure Drop =",
                eng.pressure_drop(
                    friction,
                    length,
                    diameter,
                    density,
                    velocity,
                ),
                "Pa",
            )

            save_history(eng.history)

        elif choice == "5":
            print("Bernoulli Equation coming next!")

        elif choice == "6":
            break

        else:
            print("Invalid choice.")