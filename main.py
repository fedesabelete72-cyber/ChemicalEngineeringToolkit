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
from mass_transfer import mass_transfer      # <-- ADD THIS
from about import about

from unit_converter import UnitConverter
from file_manager import load_history, clear_history
def about():

    print("\n====================================")
    print(" Chemical Engineering Toolkit v1.0 ")
    print("====================================")

    print("""
A Python-based engineering calculation toolkit.

Modules included:
- Basic Calculator
- Unit Converter
- Fluid Mechanics
- Thermodynamics
- Material Balance
- Heat Transfer
- Mass Transfer
- Reaction Engineering
- Chemistry / Molar Mass

Purpose:
Helping chemical engineering students
perform common engineering calculations.

Developed using:
Python + Object-Oriented Programming

Version:
1.0
""")

from menus import (
    main_menu,
    calculator_menu,
    unit_converter_menu,
)
calculator = Calculator()
fluid = FluidMechanics()
thermo = Thermodynamics()
material = MaterialBalance()
heat = HeatTransfer()
reaction = ReactionEngineering()
mass = MassTransfer()
chem = Chemistry()
unit_converter = UnitConverter()

while True:

    main_menu()

    choice = input("\nChoose an option: ")

    # =========================
    # Basic Calculator
    # =========================
    if choice == "1":
        try:
            a = get_number("First number: ")
            b = get_number("Second number: ")

            calculator_menu()

            operation = input("Choose operation: ")

            if operation == "1":
                print("Result:", calculator.add(a, b))

            elif operation == "2":
                print("Result:", calculator.subtract(a, b))

            elif operation == "3":
                print("Result:", calculator.multiply(a, b))

            elif operation == "4":
                print("Result:", calculator.divide(a, b))

            else:
                print("Invalid operation.")

        except ValueError:
            print("Please enter valid numbers.")

    # =========================
    # Unit Converter
    # =========================
    elif choice == "2":

        unit_converter_menu()

        option = input("Choose conversion: ")

        try:
            value = float(input("Enter value: "))

            if option == "1":
                print("Result:", unit_converter.celsius_to_kelvin(value))

            elif option == "2":
                print("Result:", unit_converter.kelvin_to_celsius(value))

            elif option == "3":
                print("Result:", unit_converter.kg_to_gram(value))

            elif option == "4":
                print("Result:", unit_converter.gram_to_kg(value))

            elif option == "5":
                print("Result:", unit_converter.meter_to_cm(value))

            elif option == "6":
                print("Result:", unit_converter.cm_to_meter(value))

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
    # Molar Mass
    # =========================
    elif choice == "9":

        formula = input("Enter chemical formula (Example: H2O): ")

        result = chem.molar_mass(formula)

        print(f"Molar Mass = {result} g/mol")

    # =========================
    # View History
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
        print("Thank you for using the Chemical Engineering Toolkit!")
        break

    else:
        print("Invalid option.")
    