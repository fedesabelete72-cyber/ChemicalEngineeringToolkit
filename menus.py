def clear_screen():
    print("\033[2J\033[H", end="")


def header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)


def show_options(options):
    for number, text in options:
        print(f"  [{number}]  {text}")


def main_menu():
    clear_screen()
    header("CHEMICAL ENGINEERING TOOLKIT")

    print("\n  ENGINEERING CALCULATIONS")
    print("  " + "-" * 46)

    show_options([
        (1, "Basic Calculator"),
        (2, "Unit Converter"),
        (3, "Fluid Mechanics"),
        (4, "Thermodynamics"),
        (5, "Material Balance"),
        (6, "Heat Transfer"),
        (7, "Mass Transfer"),
        (8, "Reaction Engineering"),
        (9, "Molar Mass Calculator"),
    ])

    print("\n  APPLICATION")
    print("  " + "-" * 46)

    show_options([
        (10, "View Saved History"),
        (11, "Clear History"),
        (12, "About"),
    ])

    print("\n  [13]  Exit")
    print("\n" + "=" * 50)


def calculator_menu():
    clear_screen()
    header("BASIC CALCULATOR")

    show_options([
        (1, "Add"),
        (2, "Subtract"),
        (3, "Multiply"),
        (4, "Divide"),
        (5, "Back"),
    ])

    print("\n" + "=" * 50)


def unit_converter_menu():
    clear_screen()
    header("UNIT CONVERTER")

    print("\n  TEMPERATURE")
    print("  " + "-" * 46)

    show_options([
        (1, "Celsius       -> Kelvin"),
        (2, "Kelvin        -> Celsius"),
        (3, "Celsius       -> Fahrenheit"),
        (4, "Fahrenheit    -> Celsius"),
    ])

    print("\n  MASS")
    print("  " + "-" * 46)

    show_options([
        (5, "Kilogram      -> Gram"),
        (6, "Gram          -> Kilogram"),
    ])

    print("\n  LENGTH")
    print("  " + "-" * 46)

    show_options([
        (7, "Meter         -> Centimeter"),
        (8, "Centimeter    -> Meter"),
        (9, "Meter         -> Millimeter"),
        (10, "Millimeter    -> Meter"),
    ])

    print("\n  PRESSURE")
    print("  " + "-" * 46)

    show_options([
        (11, "Pascal        -> Kilopascal"),
        (12, "Kilopascal    -> Pascal"),
        (13, "Pascal        -> Bar"),
        (14, "Bar           -> Pascal"),
        (15, "Pascal        -> Atmosphere"),
        (16, "Atmosphere    -> Pascal"),
    ])

    print("\n  VOLUME")
    print("  " + "-" * 46)

    show_options([
        (17, "Cubic Meter   -> Liter"),
        (18, "Liter         -> Cubic Meter"),
        (19, "Liter         -> Milliliter"),
        (20, "Milliliter    -> Liter"),
    ])

    print("\n  ENERGY")
    print("  " + "-" * 46)

    show_options([
        (21, "Joule         -> Kilojoule"),
        (22, "Kilojoule     -> Joule"),
    ])

    print("\n  POWER")
    print("  " + "-" * 46)

    show_options([
        (23, "Watt          -> Kilowatt"),
        (24, "Kilowatt      -> Watt"),
    ])

    print("\n  TIME")
    print("  " + "-" * 46)

    show_options([
        (25, "Second        -> Minute"),
        (26, "Minute        -> Second"),
        (27, "Minute        -> Hour"),
        (28, "Hour          -> Minute"),
    ])

    print("\n  [29]  Back")
    print("\n" + "=" * 50)

def fluid_mechanics_menu():
     clear_screen()
     header("FLUID MECHANICS")

     show_options([
        (1, "Density"),
        (2, "Reynolds Number"),
        (3, "Flow Rate"),
        (4, "Pipe Velocity"),
        (5, "Pressure Drop"),
        (6, "Bernoulli Equation"),
        (7, "Back"),
    ])

     print("\n" + "=" * 50)
def thermodynamics_menu():
    clear_screen()
    header("THERMODYNAMICS")

    show_options([
        (1, "Ideal Gas Law"),
        (2, "Boyle's Law"),
        (3, "Charles's Law"),
        (4, "Combined Gas Law"),
        (5, "Specific Heat"),
        (6, "Enthalpy Change"),
        (7, "Back"),
    ])

    print("\n" + "=" * 50)

def material_balance_menu():
    clear_screen()
    header("MATERIAL BALANCE")

    show_options([
        (1, "Overall Mass Balance"),
        (2, "Component Balance"),
        (3, "Conversion"),
        (4, "Yield"),
        (5, "Selectivity"),
        (6, "Recycle Ratio"),
        (7, "Purge Ratio"),
        (8, "Mixing"),
        (9, "Separation Efficiency"),
        (10, "Back"),
    ])

    print("\n" + "=" * 50)

def heat_transfer_menu():
    clear_screen()
    header("HEAT TRANSFER")

    show_options([
        (1, "Heat Conduction"),
        (2, "Heat Convection"),
        (3, "Heat Radiation"),
        (4, "Overall Heat Transfer Coefficient"),
        (5, "LMTD"),
        (6, "Heat Exchanger Effectiveness"),
        (7, "Back"),
    ])

    print("\n" + "=" * 50)

def mass_transfer_menu():
    clear_screen()
    header("MASS TRANSFER")

    show_options([
        (1, "Fick's First Law"),
        (2, "Diffusion Coefficient"),
        (3, "Mass Flux"),
        (4, "Convective Mass Transfer"),
        (5, "Sherwood Number"),
        (6, "Schmidt Number"),
        (7, "Lewis Number"),
        (8, "Peclet Number"),
        (9, "Overall Mass Transfer Coefficient"),
        (10, "Back"),
    ])

    print("\n" + "=" * 50)

def reaction_engineering_menu():
    clear_screen()
    header("REACTION ENGINEERING")

    show_options([
        (1, "Reaction Rate"),
        (2, "First Order Reaction"),
        (3, "Second Order Reaction"),
        (4, "Arrhenius Equation"),
        (5, "Residence Time"),
        (6, "Reactor Conversion"),
        (7, "Half Life"),
        (8, "CSTR Volume"),
        (9, "PFR Volume"),
        (10, "Equilibrium Constant"),
        (11, "Back"),
    ])

    print("\n" + "=" * 50)