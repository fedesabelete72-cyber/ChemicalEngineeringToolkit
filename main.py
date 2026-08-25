from result_display import show_result
from input_handler import get_number

from calculator import Calculator
from unit_converter import UnitConverter

from engineering.fluid_mechanics import FluidMechanics
from engineering.thermodynamics import Thermodynamics
from engineering.material_balance import MaterialBalance
from engineering.heat_transfer import HeatTransfer
from engineering.reaction_engineering import ReactionEngineering
from engineering.mass_transfer import MassTransfer
from engineering.chemistry import Chemistry

from about import about
from file_manager import load_history, clear_history
from menus import (
    main_menu,
    calculator_menu,
    unit_converter_menu,
    fluid_mechanics_menu,
    thermodynamics_menu,
    material_balance_menu,
    heat_transfer_menu,
    mass_transfer_menu,
    reaction_engineering_menu,
)


def main():

    # =========================
    # Initialize calculators
    # =========================

    calculator = Calculator()
    unit_converter = UnitConverter()

    fluid = FluidMechanics()
    thermo = Thermodynamics()
    material = MaterialBalance()
    heat = HeatTransfer()
    reaction = ReactionEngineering()
    mass = MassTransfer()
    chem = Chemistry()

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

          while True:

            unit_converter_menu()

            option = input("Choose conversion: ").strip()

            if option == "29":
                break

            try:
                value = get_number("Enter value: ")

                # =========================
                # Temperature
                # =========================

                if option == "1":
                    result = unit_converter.celsius_to_kelvin(value)
                    print("Result:", result, "K")

                elif option == "2":
                    result = unit_converter.kelvin_to_celsius(value)
                    print("Result:", result, "°C")

                elif option == "3":
                    result = unit_converter.celsius_to_fahrenheit(value)
                    print("Result:", result, "°F")

                elif option == "4":
                    result = unit_converter.fahrenheit_to_celsius(value)
                    print("Result:", result, "°C")

                # =========================
                # Mass
                # =========================

                elif option == "5":
                    result = unit_converter.kg_to_gram(value)
                    print("Result:", result, "g")

                elif option == "6":
                    result = unit_converter.gram_to_kg(value)
                    print("Result:", result, "kg")

                # =========================
                # Length
                # =========================

                elif option == "7":
                    result = unit_converter.meter_to_cm(value)
                    print("Result:", result, "cm")

                elif option == "8":
                    result = unit_converter.cm_to_meter(value)
                    print("Result:", result, "m")

                elif option == "9":
                    result = unit_converter.meter_to_mm(value)
                    print("Result:", result, "mm")

                elif option == "10":
                    result = unit_converter.mm_to_meter(value)
                    print("Result:", result, "m")

                # =========================
                # Pressure
                # =========================

                elif option == "11":
                    result = unit_converter.pascal_to_kilopascal(value)
                    print("Result:", result, "kPa")

                elif option == "12":
                    result = unit_converter.kilopascal_to_pascal(value)
                    print("Result:", result, "Pa")

                elif option == "13":
                    result = unit_converter.pascal_to_bar(value)
                    print("Result:", result, "bar")

                elif option == "14":
                    result = unit_converter.bar_to_pascal(value)
                    print("Result:", result, "Pa")

                elif option == "15":
                    result = unit_converter.pascal_to_atmosphere(value)
                    print("Result:", result, "atm")

                elif option == "16":
                    result = unit_converter.atmosphere_to_pascal(value)
                    print("Result:", result, "Pa")

                # =========================
                # Volume
                # =========================

                elif option == "17":
                    result = unit_converter.cubic_meter_to_liter(value)
                    print("Result:", result, "L")

                elif option == "18":
                    result = unit_converter.liter_to_cubic_meter(value)
                    print("Result:", result, "m³")

                elif option == "19":
                    result = unit_converter.liter_to_milliliter(value)
                    print("Result:", result, "mL")

                elif option == "20":
                    result = unit_converter.milliliter_to_liter(value)
                    print("Result:", result, "L")

                # =========================
                # Energy
                # =========================

                elif option == "21":
                    result = unit_converter.joule_to_kilojoule(value)
                    print("Result:", result, "kJ")

                elif option == "22":
                    result = unit_converter.kilojoule_to_joule(value)
                    print("Result:", result, "J")

                # =========================
                # Power
                # =========================

                elif option == "23":
                    result = unit_converter.watt_to_kilowatt(value)
                    print("Result:", result, "kW")

                elif option == "24":
                    result = unit_converter.kilowatt_to_watt(value)
                    print("Result:", result, "W")

                # =========================
                # Time
                # =========================

                elif option == "25":
                    result = unit_converter.second_to_minute(value)
                    print("Result:", result, "min")

                elif option == "26":
                    result = unit_converter.minute_to_second(value)
                    print("Result:", result, "s")

                elif option == "27":
                    result = unit_converter.minute_to_hour(value)
                    print("Result:", result, "h")

                elif option == "28":
                    result = unit_converter.hour_to_minute(value)
                    print("Result:", result, "min")

                else:
                    print("Invalid conversion.")

            except ValueError:
                print("Please enter a valid number.")

        # =========================
        # Fluid Mechanics
        # =========================

        elif choice == "3":

            while True:

                fluid_mechanics_menu()

                option = input("Choose an option: ").strip()

                try:

                    if option == "1":

                        mass_value = get_number("Mass (kg): ")
                        volume = get_number("Volume (m³): ")

                        result = fluid.density(
                            mass_value,
                            volume
                        )

                        show_result("Density", result, "kg/m³")

                    elif option == "2":

                        density = get_number("Density (kg/m³): ")
                        velocity = get_number("Velocity (m/s): ")
                        diameter = get_number("Diameter (m): ")
                        viscosity = get_number("Viscosity (Pa·s): ")

                        result = fluid.reynolds_number(
                            density,
                            velocity,
                            diameter,
                            viscosity
                        )

                        show_result("Reynolds Number", result)

                    elif option == "3":

                        area = get_number("Pipe Area (m²): ")
                        velocity = get_number("Velocity (m/s): ")

                        result = fluid.flow_rate(
                            area,
                            velocity
                        )

                        show_result("Flow Rate", result, "m³/s")

                    elif option == "4":

                        flow_rate = get_number("Flow Rate (m³/s): ")
                        area = get_number("Pipe Area (m²): ")

                        result = fluid.velocity(
                            flow_rate,
                            area
                        )

                        show_result(" Pipe Velocity", result, "m/s")

                    elif option == "5":

                        friction_factor = get_number("Friction Factor: ")
                        length = get_number("Length (m): ")
                        diameter = get_number("Diameter (m): ")
                        density = get_number("Density (kg/m³): ")
                        velocity = get_number("Velocity (m/s): ")

                        result = fluid.pressure_drop(
                            friction_factor,
                            length,
                            diameter,
                            density,
                            velocity
                        )

                        show_result("Pressure Drop", result, "Pa")

                    elif option == "6":

                        pressure1 = get_number("Pressure 1 (Pa): ")
                        velocity1 = get_number("Velocity 1 (m/s): ")
                        elevation1 = get_number("Elevation 1 (m): ")

                        velocity2 = get_number("Velocity 2 (m/s): ")
                        elevation2 = get_number("Elevation 2 (m): ")

                        density = get_number("Density (kg/m³): ")

                        result = fluid.bernoulli_equation(
                            pressure1,
                            velocity1,
                            elevation1,
                            velocity2,
                            elevation2,
                            density
                        )

                        show_result("Bernoulli Equation - Pressure 2", result, "Pa")

                    elif option == "7":
                        break

                    else:
                        print("Invalid option.")

                except ValueError:
                    print("Please enter valid numbers.")

        # =========================
        # Thermodynamics
        # =========================

        elif choice == "4":

            while True:

                thermodynamics_menu()

                option = input("Choose an option: ").strip()

                try:

                    if option == "1":

                        pressure = get_number("Pressure (Pa): ")
                        volume = get_number("Volume (m³): ")
                        temperature = get_number("Temperature (K): ")

                        result = thermo.ideal_gas_law(
                            pressure,
                            volume,
                            temperature
                        )

                        show_result("Ideal Gas Law - Number of Moles", result, "mol")

                    elif option == "2":

                        pressure1 = get_number("Initial Pressure: ")
                        volume1 = get_number("Initial Volume: ")
                        volume2 = get_number("Final Volume: ")

                        result = thermo.boyles_law(
                            pressure1,
                            volume1,
                            volume2
                        )

                        show_result("Boyle's Law - Final Pressure", result, "Pa")

                    elif option == "3":

                        volume1 = get_number("Initial Volume: ")
                        temperature1 = get_number("Initial Temperature (K): ")
                        temperature2 = get_number("Final Temperature (K): ")

                        result = thermo.charles_law(
                            volume1,
                            temperature1,
                            temperature2
                        )

                        show_result("Charles's Law - Final Volume", result, "m³")

                    elif option == "4":

                        pressure1 = get_number("Initial Pressure: ")
                        volume1 = get_number("Initial Volume: ")
                        temperature1 = get_number("Initial Temperature (K): ")
                        volume2 = get_number("Final Volume: ")
                        temperature2 = get_number("Final Temperature (K): ")

                        result = thermo.combined_gas_law(
                            pressure1,
                            volume1,
                            temperature1,
                            volume2,
                            temperature2
                        )

                        show_result("Combined Gas Law - Final Pressure", result, "Pa")

                    elif option == "5":

                        mass_value = get_number("Mass (kg): ")
                        specific_heat_capacity = get_number(
                            "Specific Heat Capacity (J/kg·K): "
                        )
                        temperature_change = get_number(
                            "Temperature Change (K): "
                        )

                        result = thermo.specific_heat(
                            mass_value,
                            specific_heat_capacity,
                            temperature_change
                        )

                        show_result("Specific Heat - Heat Transfer", result, "J")

                    elif option == "6":

                        mass_value = get_number("Mass (kg): ")
                        cp = get_number("Cp (J/kg·K): ")
                        temperature_change = get_number(
                            "Temperature Change (K): "
                        )

                        result = thermo.enthalpy_change(
                            mass_value,
                            cp,
                            temperature_change
                        )

                        show_result("Enthalpy Change", result, "J")

                    elif option == "7":
                        break

                    else:
                        print("Invalid option.")

                except ValueError:
                    print("Please enter valid numbers.")

        # =========================
        # Material Balance
        # =========================

        elif choice == "5":

            while True:

                material_balance_menu()

                option = input("Choose an option: ").strip()

                try:

                    if option == "1":

                        mass_in = get_number("Mass In: ")
                        accumulation = get_number("Accumulation: ")

                        result = material.overall_mass_balance(
                            mass_in,
                            accumulation
                        )

                        show_result("Overall Mass Balance", result, "kg")

                    elif option == "2":

                        component_in = get_number("Component In: ")
                        accumulation = get_number("Accumulation: ")

                        result = material.component_balance(
                            component_in,
                            accumulation
                        )

                        show_result("Component Balance", result, "kg")

                    elif option == "3":

                        initial = get_number("Initial Amount: ")
                        final = get_number("Final Amount: ")

                        result = material.conversion(
                            initial,
                            final
                        )

                        show_result("Conversion", result, "%")

                    elif option == "4":

                        actual = get_number("Actual Product: ")
                        theoretical = get_number("Theoretical Product: ")

                        result = material.yield_percentage(
                            actual,
                            theoretical
                        )

                        show_result("Yield Percentage", result, "%")

                    elif option == "5":

                        desired = get_number("Desired Product: ")
                        undesired = get_number("Undesired Product: ")

                        result = material.selectivity(
                            desired,
                            undesired
                        )

                        show_result("Selectivity", result, "")

                    elif option == "6":

                        recycle = get_number("Recycle Stream: ")
                        fresh_feed = get_number("Fresh Feed: ")

                        result = material.recycle_ratio(
                            recycle,
                            fresh_feed
                        )

                        show_result("Recycle Ratio", result, "")

                    elif option == "7":

                        purge = get_number("Purge Stream: ")
                        recycle = get_number("Recycle Stream: ")

                        result = material.purge_ratio(
                            purge,
                            recycle
                        )

                        show_result("Purge Ratio", result, "")

                    elif option == "8":

                        mass1 = get_number("Mass 1: ")
                        composition1 = get_number("Composition 1: ")
                        mass2 = get_number("Mass 2: ")
                        composition2 = get_number("Composition 2: ")

                        result = material.mixing(
                            mass1,
                            composition1,
                            mass2,
                            composition2
                        )

                        show_result("Total Mass", result[0], "kg")
                        show_result("Mixed Composition", result[1], "")

                    elif option == "9":

                        recovered = get_number("Recovered Amount: ")
                        feed = get_number("Feed: ")

                        result = material.separation_efficiency(
                            recovered,
                            feed
                        )

                        show_result("Separation Efficiency", result, "%")

                    elif option == "10":
                        break

                    else:
                        print("Invalid option.")

                except ValueError:
                    print("Please enter valid numbers.")

        # =========================
        # Heat Transfer
        # =========================

        elif choice == "6":

            while True:

                heat_transfer_menu()

                option = input("Choose an option: ").strip()

                try:

                    if option == "1":

                        k = get_number("Thermal Conductivity (W/m·K): ")
                        area = get_number("Area (m²): ")
                        t1 = get_number("Temperature 1 (K): ")
                        t2 = get_number("Temperature 2 (K): ")
                        thickness = get_number("Thickness (m): ")

                        result = heat.heat_conduction(
                            k,
                            area,
                            t1,
                            t2,
                            thickness
                        )

                        show_result("Heat Transfer", result, "W")

                    elif option == "2":

                        h = get_number("Heat Transfer Coefficient: ")
                        area = get_number("Area (m²): ")
                        surface_temperature = get_number(
                            "Surface Temperature: "
                        )
                        fluid_temperature = get_number(
                            "Fluid Temperature: "
                        )

                        result = heat.heat_convection(
                            h,
                            area,
                            surface_temperature,
                            fluid_temperature
                        )

                        show_result("Heat Transfer", result, "W")

                    elif option == "3":

                        emissivity = get_number("Emissivity (0-1): ")
                        area = get_number("Area (m²): ")
                        surface_temperature = get_number(
                            "Surface Temperature (K): "
                        )
                        surrounding_temperature = get_number(
                            "Surrounding Temperature (K): "
                        )

                        result = heat.heat_radiation(
                            emissivity,
                            area,
                            surface_temperature,
                            surrounding_temperature
                        )

                        show_result("Radiation Heat Transfer", result, "W")

                    elif option == "4":

                        heat_rate = get_number("Heat Rate (W): ")
                        area = get_number("Area (m²): ")
                        temperature_difference = get_number(
                            "Temperature Difference (K): "
                        )

                        result = heat.overall_heat_transfer_coefficient(
                            heat_rate,
                            area,
                            temperature_difference
                        )

                        show_result("Overall Heat Transfer Coefficient", result, "W")

                    elif option == "5":

                        delta_t1 = get_number("ΔT1 (K): ")
                        delta_t2 = get_number("ΔT2 (K): ")

                        result = heat.lmtd(
                            delta_t1,
                            delta_t2
                        )

                        show_result("LMTD", result, "K")

                    elif option == "6":

                        actual = get_number("Actual Heat Transfer: ")
                        maximum = get_number("Maximum Heat Transfer: ")

                        result = heat.heat_exchanger_effectiveness(
                            actual,
                            maximum
                        )

                        show_result("Effectiveness", result, "%")

                    elif option == "7":
                        break

                    else:
                        print("Invalid option.")

                except ValueError:
                    print("Please enter valid numbers.")

        # =========================
        # Mass Transfer
        # =========================

        elif choice == "7":

            while True:

                mass_transfer_menu()

                option = input("Choose an option: ").strip()

                try:

                    if option == "1":

                        diffusion_coefficient = get_number(
                            "Diffusion Coefficient (m²/s): "
                        )
                        concentration_difference = get_number(
                            "Concentration Difference: "
                        )
                        distance = get_number(
                            "Distance (m): "
                        )

                        result = mass.ficks_first_law(
                            diffusion_coefficient,
                            concentration_difference,
                            distance
                        )

                        show_result("Mass Flux", result, "kg/(m²·s)")

                    elif option == "2":

                        mass_flux = get_number("Mass Flux: ")
                        concentration_difference = get_number(
                            "Concentration Difference: "
                        )
                        distance = get_number("Distance (m): ")

                        result = mass.calculate_diffusion_coefficient(
                            mass_flux,
                            concentration_difference,
                            distance
                        )

                        show_result("Diffusion Coefficient", result, "m²/s")

                    elif option == "3":

                        mass_flow_rate = get_number("Mass Flow Rate: ")
                        area = get_number("Area (m²): ")

                        result = mass.mass_flux(
                            mass_flow_rate,
                            area
                        )

                        show_result("Mass Flux", result, "kg/(m²·s)")

                    elif option == "4":

                        coefficient = get_number(
                            "Mass Transfer Coefficient: "
                        )
                        surface = get_number(
                            "Surface Concentration: "
                        )
                        bulk = get_number(
                            "Bulk Concentration: "
                        )

                        result = mass.convective_mass_transfer(
                            coefficient,
                            surface,
                            bulk
                        )

                        show_result("Mass Transfer", result, "kg/s")

                    elif option == "5":

                        coefficient = get_number(
                            "Mass Transfer Coefficient: "
                        )
                        length = get_number(
                            "Characteristic Length: "
                        )
                        diffusion = get_number(
                            "Diffusion Coefficient: "
                        )

                        result = mass.sherwood_number(
                            coefficient,
                            length,
                            diffusion
                        )

                        show_result("Sherwood Number", result, "")

                    elif option == "6":

                        viscosity = get_number("Viscosity: ")
                        density = get_number("Density: ")
                        diffusion = get_number(
                            "Diffusion Coefficient: "
                        )

                        result = mass.schmidt_number(
                            viscosity,
                            density,
                            diffusion
                        )

                        show_result("Schmidt Number", result, "")

                    elif option == "7":

                        thermal_diffusivity = get_number(
                            "Thermal Diffusivity: "
                        )
                        diffusion = get_number(
                            "Diffusion Coefficient: "
                        )

                        result = mass.lewis_number(
                            thermal_diffusivity,
                            diffusion
                        )

                        show_result("Lewis Number", result, "")

                    elif option == "8":

                        reynolds = get_number("Reynolds Number: ")
                        schmidt = get_number("Schmidt Number: ")

                        result = mass.peclet_number(
                            reynolds,
                            schmidt
                        )
                        show_result("Peclet Number", result, "")

                    elif option == "9":

                        mass_flux = get_number("Mass Flux: ")
                        concentration_difference = get_number(
                            "Concentration Difference: "
                        )

                        result = mass.overall_mass_transfer_coefficient(
                            mass_flux,
                            concentration_difference
                        )

                        show_result("Overall Mass Transfer Coefficient", result, "kg/(m²·s)")

                    elif option == "10":
                        break

                    else:
                        print("Invalid option.")

                except ValueError:
                    print("Please enter valid numbers.")

        # =========================
        # Reaction Engineering
        # =========================

        elif choice == "8":

            while True:

                reaction_engineering_menu()

                option = input("Choose an option: ").strip()

                try:

                    if option == "1":

                        rate_constant = get_number("Rate Constant: ")
                        concentration = get_number("Concentration: ")
                        reaction_order = get_number("Reaction Order: ")

                        result = reaction.reaction_rate(
                            rate_constant,
                            concentration,
                            reaction_order
                        )

                        show_result("Reaction Rate", result, "mol/(m³·s)")

                    elif option == "2":

                        initial = get_number(
                            "Initial Concentration: "
                        )
                        rate_constant = get_number(
                            "Rate Constant: "
                        )
                        time = get_number("Time: ")

                        result = reaction.first_order_reaction(
                            initial,
                            rate_constant,
                            time
                        )

                        show_result("Final Concentration", result, "mol/m³")

                    elif option == "3":

                        initial = get_number(
                            "Initial Concentration: "
                        )
                        rate_constant = get_number(
                            "Rate Constant: "
                        )
                        time = get_number("Time: ")

                        result = reaction.second_order_reaction(
                            initial,
                            rate_constant,
                            time
                        )

                        show_result("Final Concentration", result, "mol/m³")

                    elif option == "4":

                        frequency_factor = get_number(
                            "Frequency Factor A: "
                        )
                        activation_energy = get_number(
                            "Activation Energy (J/mol): "
                        )
                        temperature = get_number(
                            "Temperature (K): "
                        )

                        result = reaction.arrhenius_equation(
                            frequency_factor,
                            activation_energy,
                            temperature
                        )

                        show_result("Rate Constant", result, "1/s")

                    elif option == "5":

                        reactor_volume = get_number(
                            "Reactor Volume (m³): "
                        )
                        flow_rate = get_number(
                            "Volumetric Flow Rate (m³/s): "
                        )

                        result = reaction.residence_time(
                            reactor_volume,
                            flow_rate
                        )

                        show_result("Residence Time", result, "s")

                    elif option == "6":

                        inlet = get_number("Inlet Moles: ")
                        outlet = get_number("Outlet Moles: ")

                        result = reaction.reactor_conversion(
                            inlet,
                            outlet
                        )

                        show_result("Conversion", result, "%")

                    elif option == "7":

                        rate_constant = get_number(
                            "Rate Constant: "
                        )

                        result = reaction.half_life(
                            rate_constant
                        )

                        show_result("Half Life", result, "s")

                    elif option == "8":

                        inlet_flow = get_number(
                            "Inlet Molar Flow: "
                        )
                        conversion = get_number(
                            "Conversion (0-1): "
                        )
                        reaction_rate = get_number(
                            "Reaction Rate: "
                        )

                        result = reaction.cstr_volume(
                            inlet_flow,
                            conversion,
                            reaction_rate
                        )

                        show_result("CSTR Volume", result, "m³")

                    elif option == "9":

                        inlet_flow = get_number(
                            "Inlet Molar Flow: "
                        )
                        conversion = get_number(
                            "Conversion (0-1): "
                        )
                        reaction_rate = get_number(
                            "Reaction Rate: "
                        )

                        result = reaction.pfr_volume(
                            inlet_flow,
                            conversion,
                            reaction_rate
                        )

                        show_result("PFR Volume", result, "m³")

                    elif option == "10":

                        products = get_number("Products: ")
                        reactants = get_number("Reactants: ")

                        result = reaction.equilibrium_constant(
                            products,
                            reactants
                        )

                        show_result("Equilibrium Constant", result, "")

                    elif option == "11":
                        break

                    else:
                        print("Invalid option.")

                except ValueError:
                    print("Please enter valid numbers.")

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

                show_result("Molar Mass", result, "g/mol")

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

            print(
                "Invalid option. Please choose 1-13."
            )


# =========================
# Program Entry Point
# =========================

if __name__ == "__main__":
    main()