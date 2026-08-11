from file_manager import save_history


def mass_transfer_menu():
    print("\n========== Mass Transfer ==========")
    print("1. Fick's First Law")
    print("2. Diffusion Coefficient")
    print("3. Mass Flux")
    print("4. Convective Mass Transfer")
    print("5. Sherwood Number")
    print("6. Schmidt Number")
    print("7. Back")


def mass_transfer(eng):
    while True:
        mass_transfer_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                diffusion_coefficient = float(
                    input("Diffusion Coefficient (m²/s): ")
                )

                concentration_difference = float(
                    input("Concentration Difference (mol/m³): ")
                )

                distance = float(
                    input("Distance (m): ")
                )

                result = eng.ficks_first_law(
                    diffusion_coefficient,
                    concentration_difference,
                    distance
                )

                print(
                    "Mass Flux =",
                    result,
                    "mol/m²·s"
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "2":
            try:
                mass_flux = float(
                    input("Mass Flux (mol/m²·s): ")
                )

                concentration_difference = float(
                    input("Concentration Difference (mol/m³): ")
                )

                distance = float(
                    input("Distance (m): ")
                )

                result = eng.diffusion_coefficient(
                    mass_flux,
                    concentration_difference,
                    distance
                )

                print(
                    "Diffusion Coefficient =",
                    result,
                    "m²/s"
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                mass_flow_rate = float(
                    input("Mass Flow Rate (kg/s): ")
                )

                area = float(
                    input("Area (m²): ")
                )

                result = eng.mass_flux(
                    mass_flow_rate,
                    area
                )

                print(
                    "Mass Flux =",
                    result,
                    "kg/m²·s"
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "4":
            try:
                mass_transfer_coefficient = float(
                    input("Mass Transfer Coefficient (m/s): ")
                )

                surface_concentration = float(
                    input("Surface Concentration (mol/m³): ")
                )

                bulk_concentration = float(
                    input("Bulk Concentration (mol/m³): ")
                )

                result = eng.convective_mass_transfer(
                    mass_transfer_coefficient,
                    surface_concentration,
                    bulk_concentration
                )

                print(
                    "Mass Transfer Rate =",
                    result
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":
            try:
                kc = float(
                    input("Mass Transfer Coefficient (m/s): ")
                )

                length = float(
                    input("Characteristic Length (m): ")
                )

                diffusion = float(
                    input("Diffusion Coefficient (m²/s): ")
                )

                result = eng.sherwood_number(
                    kc,
                    length,
                    diffusion
                )

                print(
                    "Sherwood Number =",
                    result
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "6":
            try:
                viscosity = float(
                    input("Dynamic Viscosity (Pa·s): ")
                )

                density = float(
                    input("Density (kg/m³): ")
                )

                diffusion_coefficient = float(
                    input("Diffusion Coefficient (m²/s): ")
                )

                result = eng.schmidt_number(
                    viscosity,
                    density,
                    diffusion_coefficient
                )

                print(
                    "Schmidt Number =",
                    result
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")
        elif choice == "7":
            break

        else:
            print("Invalid choice.")