from file_manager import save_history
from utils import show_result


def material_balance_menu():
    print("\n========== Material Balance ==========")
    print("1. Overall Mass Balance")
    print("2. Component Balance")
    print("3. Conversion")
    print("4. Yield")
    print("5. Selectivity")
    print("6. Recycle Ratio")
    print("7. Purge Ratio")
    print("8. Mixing")
    print("9. Separation Efficiency")
    print("10. Back")


def material_balance(eng):

    while True:

        material_balance_menu()

        choice = input("Choose an option: ")

        # ==========================================
        # Overall Mass Balance
        # ==========================================
        if choice == "1":

            try:
                mass_in = float(input("Mass Entering (kg): "))
                accumulation = float(input("Accumulation (kg): "))

                result = eng.overall_mass_balance(
                    mass_in,
                    accumulation
                )

                show_result(
                    "Overall Mass Balance",
                    result,
                    "kg",
                    f"The process leaves {result} kg after accounting for accumulation."
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Component Balance
        # ==========================================
        elif choice == "2":

            try:
                component_in = float(input("Component Entering (kg): "))
                accumulation = float(input("Component Accumulation (kg): "))

                result = eng.component_balance(
                    component_in,
                    accumulation
                )

                show_result(
                    "Component Balance",
                    result,
                    "kg",
                    f"The outlet stream contains {result} kg of the selected component."
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Conversion
        # ==========================================
        elif choice == "3":

            try:
                initial_amount = float(
                    input("Initial Reactant Amount (kg or mol): ")
                )

                final_amount = float(
                    input("Final Reactant Amount (kg or mol): ")
                )

                result = eng.conversion(
                    initial_amount,
                    final_amount
                )

                show_result(
                    "Conversion",
                    result,
                    "%",
                    f"{result}% of the reactant has reacted.\n{100 - result}% remains unreacted."
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Yield
        # ==========================================
        elif choice == "4":

            try:
                actual = float(input("Actual Product (kg): "))
                theoretical = float(input("Theoretical Product (kg): "))

                result = eng.yield_percentage(
                    actual,
                    theoretical
                )

                show_result(
                    "Yield",
                    result,
                    "%",
                    f"The process produced {result}% of the theoretical maximum product."
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Selectivity
        # ==========================================
        elif choice == "5":

            try:
                desired = float(input("Desired Product (kg): "))
                undesired = float(input("Undesired Product (kg): "))

                result = eng.selectivity(
                    desired,
                    undesired
                )

                show_result(
                    "Selectivity",
                    result,
                    "",
                    f"The process forms {result} times more desired product than undesired product."
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Recycle Ratio
        # ==========================================
        elif choice == "6":

            try:
                recycle_stream = float(input("Recycle Stream (kg): "))
                fresh_feed = float(input("Fresh Feed (kg): "))

                result = eng.recycle_ratio(
                    recycle_stream,
                    fresh_feed
                )

                show_result(
                    "Recycle Ratio",
                    result,
                    "",
                    f"For every 1 kg of fresh feed,\n{result} kg is recycled back into the process."
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Purge Ratio
        # ==========================================
        elif choice == "7":

            try:
                purge_stream = float(input("Purge Stream (kg): "))
                recycle_stream = float(input("Recycle Stream (kg): "))

                result = eng.purge_ratio(
                    purge_stream,
                    recycle_stream
                )

                show_result(
                    "Purge Ratio",
                    result,
                    "",
                    f"For every 1 kg of recycle stream,\n{result} kg is removed as purge."
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Mixing
        # ==========================================
        elif choice == "8":

            try:
                mass1 = float(
                    input("Stream 1 Mass (kg): ")
                )

                composition1 = float(
                    input("Stream 1 Composition (0-1): ")
                )

                mass2 = float(
                    input("Stream 2 Mass (kg): ")
                )

                composition2 = float(
                    input("Stream 2 Composition (0-1): ")
                )

                total_mass, mixed_composition = eng.mixing(
                    mass1,
                    composition1,
                    mass2,
                    composition2
                )

                show_result(
                    "Mixing",
                    total_mass,
                    "kg",
                    f"Total mixed stream = {total_mass} kg\n"
                    f"Final composition = {mixed_composition}"
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Separation Efficiency
        # ==========================================
        elif choice == "9":

            try:
                recovered = float(
                    input("Recovered Material (kg): ")
                )

                feed = float(
                    input("Feed Material (kg): ")
                )

                result = eng.separation_efficiency(
                    recovered,
                    feed
                )

                show_result(
                    "Separation Efficiency",
                    result,
                    "%",
                    f"The separation process recovered {result}% of the feed material."
                )

                save_history(eng.history)

            except ValueError:
                print("Please enter valid numbers.")

        # ==========================================
        # Back
        # ==========================================
        elif choice == "10":
            break

        else:
            print("Invalid choice.")