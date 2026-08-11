from engineering.thermodynamics import Thermodynamics

thermo = Thermodynamics()

print(thermo.ideal_gas_law(101325, 1, 300))

print(thermo.boyles_law(100000, 2, 1))

print(thermo.specific_heat(2, 4184, 20))