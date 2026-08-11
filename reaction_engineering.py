from file_manager import save_history


def reaction_engineering_menu():

    print("\n========== Reaction Engineering ==========")
    print("1. Reaction Rate")
    print("2. First Order Reaction")
    print("3. Second Order Reaction")
    print("4. Arrhenius Equation")
    print("5. Residence Time")
    print("6. Conversion")
    print("7. Back")


def reaction_engineering(eng):

    while True:

        reaction_engineering_menu()

        choice = input("Choose an option: ")

        if choice == "1":

            try:
                k = float(input("Rate Constant (k): "))
                concentration = float(input("Concentration (C): "))
                order = float(input("Reaction Order: "))

                result = eng.reaction_rate(
                    k,
                    concentration,
                    order
                )

                print(
                    "Reaction Rate =",
                    result
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "2":

            try:
                initial_concentration = float(
                    input("Initial Concentration: ")
                )

                rate_constant = float(
                    input("Rate Constant (k): ")
                )

                time = float(
                    input("Time: ")
                )

                result = eng.first_order_reaction(
                    initial_concentration,
                    rate_constant,
                    time
                )

                print(
                    "Final Concentration =",
                    result
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":

            try:
                initial_concentration = float(
                    input("Initial Concentration: ")
                )

                rate_constant = float(
                    input("Rate Constant (k): ")
                )

                time = float(
                    input("Time: ")
                )

                result = eng.second_order_reaction(
                    initial_concentration,
                    rate_constant,
                    time
                )

                print(
                    "Final Concentration =",
                    result
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "4":

            try:
                frequency_factor = float(
                    input("Frequency Factor (A): ")
                )

                activation_energy = float(
                    input("Activation Energy (J/mol): ")
                )

                temperature = float(
                    input("Temperature (K): ")
                )

                result = eng.arrhenius_equation(
                    frequency_factor,
                    activation_energy,
                    temperature
                )

                print(
                    "Rate Constant (k) =",
                    result
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":

            try:
                reactor_volume = float(
                    input("Reactor Volume (m³): ")
                )

                volumetric_flow_rate = float(
                    input("Volumetric Flow Rate (m³/s): ")
                )

                result = eng.residence_time(
                    reactor_volume,
                    volumetric_flow_rate
                )

                print(
                    "Residence Time =",
                    result,
                    "s"
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "6":

            try:
                initial_concentration = float(
                    input("Initial Concentration: ")
                )

                final_concentration = float(
                    input("Final Concentration: ")
                )

                result = eng.conversion(
                    initial_concentration,
                    final_concentration
                )

                print(
                    "Conversion =",
                    result
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "7":
            break

        else:
            print("Coming soon!")