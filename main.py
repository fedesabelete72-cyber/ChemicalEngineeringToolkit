from input_handler import get_number

from calculator import Calculator

from engineering.fluid_mechanics import FluidMechanics
from engineering.thermodynamics import Thermodynamics
from engineering.material_balance import MaterialBalance
from engineering.heat_transfer import HeatTransfer
from engineering.reaction_engineering import ReactionEngineering
from engineering.mass_transfer import MassTransfer
from engineering.chemistry import Chemistry

from fluid_mechanics import fluid_mechanics
from thermodynamics import thermodynamics
from material_balance import material_balance
from heat_transfer import heat_transfer
from reaction_engineering import reaction_engineering
from mass_transfer import mass_transfer

from about import about

from unit_converter import UnitConverter

from file_manager import load_history, clear_history

from menus import (
    main_menu,
    calculator_menu,
    unit_converter_menu,
)


def main():

    # =========================
    # Initialize calculators
    # =========================

    calculator = Calculator()
    fluid = FluidMechanics()
    thermo = Thermodynamics()
    material = MaterialBalance()
    heat = HeatTransfer()
    reaction = ReactionEngineering()
    mass = MassTransfer()
    chem = Chemistry()
    unit_converter = UnitConverter()

    # =========================
    # Main program loop
    # =========================

    while True:

        main_menu()

        choice = input("\nChoose an option: ").strip()

        # =========================
        # Basic Calculator
        # =========================

        if choice == "1":

            try:
                a = get_number("First number: ")
                b = get_number("Second number: ")

                calculator_menu()

                operation = input("Choose operation: ").strip()

                if operation == "1":
                    result = calculator.add(a, b)
                    print("Result:", result)

                elif operation == "2":
                    result = calculator.subtract(a, b)
                    print("Result:", result)

                elif operation == "3":
                    result = calculator.multiply(a, b)
                    print("Result:", result)

                elif operation == "4":
                    result = calculator.divide(a, b)
                    print("Result:", result)

                else:
                    print("Invalid operation.")

            except ValueError:
                print("Please enter valid numbers.")

        # =========================
        # Unit Converter
        # =========================

        elif choice == "2":

            unit_converter_menu()

            option = input("Choose conversion: ").strip()

            try:
                value = get_number("Enter value: ")

                if option == "1":
                    result = unit_converter.celsius_to_kelvin(value)
                    print("Result:", result)

                elif option == "2":
                    result = unit_converter.kelvin_to_celsius(value)
                    print("Result:", result)

                elif option == "3":
                    result = unit_converter.kg_to_gram(value)
                    print("Result:", result)

                elif option == "4":
                    result = unit_converter.gram_to_kg(value)
                    print("Result:", result)

                elif option == "5":
                    result = unit_converter.meter_to_cm(value)
                    print("Result:", result)

                elif option == "6":
                    result = unit_converter.cm_to_meter(value)
                    print("Result:", result)

                else:
                    print("Invalid conversion.")

            except ValueError:
                print("Please enter a valid number.")

        # =========================
        # Fluid Mechanics
        # =========================

        elif choice == "3":

            fluid_mechanics(fluid)

        # =========================
        # Thermodynamics
        # =========================

        elif choice == "4":

            thermodynamics(thermo)

        # =========================
        # Material Balance
        # =========================

        elif choice == "5":

            material_balance(material)

        # =========================
        # Heat Transfer
        # =========================

        elif choice == "6":

            heat_transfer(heat)

        # =========================
        # Mass Transfer
        # =========================

        elif choice == "7":

            mass_transfer(mass)

        # =========================
        # Reaction Engineering
        # =========================

        elif choice == "8":

            reaction_engineering(reaction)

        # =========================
        # Molar Mass Calculator
        # =========================

        elif choice == "9":

            formula = input(
                "Enter chemical formula (Example: H2O): "
            ).strip()

            if not formula:
                print("Error: Chemical formula cannot be empty.")
                continue

            try:
                result = chem.molar_mass(formula)
                print(f"Molar Mass = {result} g/mol")
            except ValueError as e:
                print(f"Error: {e}")

        # =========================
        # View Saved History
        # =========================

        elif choice == "10":

            history = load_history()

            if history:
                print("\n===== Saved History =====")

                for item in history:
                    print(item)

            else:
                print("No saved history.")

        # =========================
        # Clear History
        # =========================

        elif choice == "11":

            clear_history()

            print("History cleared.")

        # =========================
        # About
        # =========================

        elif choice == "12":

            about()

        # =========================
        # Exit
        # =========================

        elif choice == "13":

            print(
                "\nThank you for using the "
                "Chemical Engineering Toolkit!"
            )

            break

        # =========================
        # Invalid Main Menu Choice
        # =========================

        else:

            print("Invalid option. Please choose 1-13.")


# =========================
# Program Entry Point
# =========================

if __name__ == "__main__":
    main()