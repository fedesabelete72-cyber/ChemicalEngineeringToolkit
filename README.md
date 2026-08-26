# Chemical Engineering Toolkit

A modular Python-based engineering calculation toolkit designed for Chemical Engineering students and engineers.

The application provides a command-line interface for performing common calculations across fluid mechanics, thermodynamics, material balances, heat transfer, mass transfer, reaction engineering, and chemistry.

---

## Overview

Chemical Engineering Toolkit demonstrates the practical application of programming and engineering principles through a modular calculation system.

The project was developed to combine:

- Chemical Engineering fundamentals
- Python programming
- Object-Oriented Programming (OOP)
- Modular software architecture
- Input validation
- Exception handling
- File handling
- Calculation history
- Git and GitHub version control

The primary goal is to provide a structured educational engineering calculator while developing software engineering skills applicable to Chemical Engineering.

> **Note:** This toolkit is intended for educational and preliminary calculation purposes. Engineering results should be independently verified before being used in real industrial design or safety-critical applications.

---

# Features

## General Tools

- Basic Calculator
- Unit Converter
- Calculation History
- Clear History
- About Section

## Fluid Mechanics

- Density
- Reynolds Number
- Flow Rate
- Pipe Velocity
- Pressure Drop
- Bernoulli Equation

## Thermodynamics

- Ideal Gas Law
- Boyle's Law
- Charles's Law
- Combined Gas Law
- Specific Heat
- Enthalpy Change

## Material Balance

- Overall Mass Balance
- Component Balance
- Conversion
- Yield
- Selectivity
- Recycle Ratio
- Purge Ratio
- Mixing
- Separation Efficiency

## Heat Transfer

- Heat Conduction
- Heat Convection
- Heat Radiation
- Overall Heat Transfer Coefficient
- Log Mean Temperature Difference (LMTD)
- Heat Exchanger Effectiveness

## Mass Transfer

- Fick's First Law
- Diffusion Coefficient
- Mass Flux
- Convective Mass Transfer
- Sherwood Number
- Schmidt Number
- Lewis Number
- Peclet Number
- Overall Mass Transfer Coefficient

## Reaction Engineering

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

## Chemistry

- Molar Mass Calculator
- Chemical Formula Parsing
- Parenthesized Chemical Groups
- Formula Validation
- Element Validation
- Invalid Character Detection
- Empty Input Validation

---

# Project Structure

```text
ChemicalEngineeringToolkit/
│
├── engineering/
│   ├── __init__.py
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
├── about.py
├── calculator.py
├── constants.py
├── file_manager.py
├── history.py
├── input_handler.py
├── main.py
├── menus.py
├── unit_converter.py
├── utils.py
├── periodic_table.json
├── README.md
└── .gitignore
---

# Running the Application

## Requirements

- Python 3.10 or newer

## Run from Source

From the project directory, run:

```powershell
python main.py
```

## Windows Executable

A Windows executable can be built using PyInstaller:

```powershell
python -m PyInstaller ChemicalEngineeringToolkit.spec
```

The generated executable will be located in:

```text
dist/ChemicalEngineeringToolkit.exe
```
