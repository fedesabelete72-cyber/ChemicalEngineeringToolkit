# Chemical Engineering Toolkit

## Developed by

**Fedesa Belete**

## Version

**1.1**

## Description

Chemical Engineering Toolkit is a Python-based engineering application designed to help Chemical Engineering students perform common engineering calculations quickly and easily.

The project combines Python programming, Object-Oriented Programming (OOP), and Chemical Engineering principles into one interactive command-line toolkit.

## Features

### General Tools

- Basic Calculator
- Unit Converter
- Calculation History
- Clear History
- About Section

### Fluid Mechanics

- Density
- Reynolds Number
- Flow Rate
- Velocity
- Pressure Drop

### Thermodynamics

- Ideal Gas Law
- Boyle's Law
- Charles's Law
- Combined Gas Law
- Specific Heat
- Enthalpy Change

### Material Balance

- Overall Mass Balance
- Component Balance
- Conversion
- Yield
- Selectivity
- Recycle Ratio
- Purge Ratio
- Mixing
- Separation Efficiency

### Heat Transfer

- Heat Conduction
- Heat Convection
- Heat Radiation
- Overall Heat Transfer Coefficient
- Log Mean Temperature Difference (LMTD)
- Heat Exchanger Effectiveness

### Mass Transfer

- Fick's First Law
- Diffusion Coefficient
- Mass Flux
- Convective Mass Transfer
- Sherwood Number
- Schmidt Number
- Lewis Number
- Peclet Number
- Overall Mass Transfer Coefficient

### Reaction Engineering

- Reaction Rate
- First-Order Reaction
- Second-Order Reaction
- Arrhenius Equation
- Residence Time
- Reactor Conversion
- Half-Life
- CSTR Volume
- PFR Volume
- Equilibrium Constant

### Chemistry

- Molar Mass Calculator
- Chemical Formula Validation
- Support for common chemical elements
- Error handling for invalid formulas

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Modular Programming
- File Handling
- Command-Line Interface (CLI)

## Project Structure

```text
ChemicalEngineeringToolkit/
│
├── main.py
├── calculator.py
├── constants.py
├── input_handler.py
├── unit_converter.py
├── file_manager.py
├── menus.py
├── about.py
│
├── fluid_mechanics.py
├── thermodynamics.py
├── material_balance.py
├── heat_transfer.py
├── mass_transfer.py
├── reaction_engineering.py
│
├── engineering/
│   ├── calculator.py
│   ├── chemistry.py
│   ├── fluid_mechanics.py
│   ├── heat_transfer.py
│   ├── mass_transfer.py
│   ├── material_balance.py
│   ├── reaction_engineering.py
│   └── thermodynamics.py
│
├── data/
│   ├── calculations.csv
│   └── history.txt
│
├── tests/
│
├── periodic_table.json
├── requirements.txt
├── .gitignore
└── README.md