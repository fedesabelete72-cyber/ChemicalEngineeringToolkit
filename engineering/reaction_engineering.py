import math


class ReactionEngineering:

    def __init__(self):
        self.history = []

    # --------------------------------------
    # Reaction Rate
    # -rA = k(CA)^n
    # --------------------------------------
    def reaction_rate(
        self,
        rate_constant,
        concentration,
        reaction_order
    ):

        if rate_constant <= 0:
            return "Error: Rate constant must be positive."

        if concentration < 0:
            return "Error: Concentration cannot be negative."

        if reaction_order < 0:
            return "Error: Reaction order cannot be negative."

        result = rate_constant * (
            concentration ** reaction_order
        )

        self.history.append(
            f"Reaction Rate: {result:.6f}"
        )

        return round(result, 6)


    # --------------------------------------
    # First Order Reaction
    # CA = CA0 e^(-kt)
    # --------------------------------------
    def first_order_reaction(
        self,
        initial_concentration,
        rate_constant,
        time
    ):

        if initial_concentration < 0:
            return "Error: Initial concentration cannot be negative."

        if rate_constant <= 0:
            return "Error: Rate constant must be positive."

        if time < 0:
            return "Error: Time cannot be negative."

        result = initial_concentration * math.exp(
            -rate_constant * time
        )

        self.history.append(
            f"First Order Reaction: CA = {result:.6f}"
        )

        return round(result, 6)


    # --------------------------------------
    # Second Order Reaction
    # CA = CA0/(1+kCA0t)
    # --------------------------------------
    def second_order_reaction(
        self,
        initial_concentration,
        rate_constant,
        time
    ):

        if initial_concentration <= 0:
            return "Error: Initial concentration must be positive."

        if rate_constant <= 0:
            return "Error: Rate constant must be positive."

        if time < 0:
            return "Error: Time cannot be negative."

        denominator = (
            1 +
            rate_constant *
            initial_concentration *
            time
        )

        if denominator <= 0:
            return "Error: Invalid inputs."

        result = (
            initial_concentration /
            denominator
        )

        self.history.append(
            f"Second Order Reaction: CA = {result:.6f}"
        )

        return round(result, 6)


    # --------------------------------------
    # Arrhenius Equation
    # k = A exp(-Ea/RT)
    # --------------------------------------
    def arrhenius_equation(
        self,
        frequency_factor,
        activation_energy,
        temperature
    ):

        if frequency_factor <= 0:
            return "Error: Frequency factor must be positive."

        if activation_energy <= 0:
            return "Error: Activation energy must be positive."

        if temperature <= 0:
            return "Error: Temperature must be in Kelvin."

        R = 8.314

        result = frequency_factor * math.exp(
            -activation_energy /
            (R * temperature)
        )

        self.history.append(
            f"Arrhenius Equation: k = {result:.8f}"
        )

        return round(result, 8)


    # --------------------------------------
    # Residence Time
    # τ = V/Q
    # --------------------------------------
    def residence_time(
        self,
        reactor_volume,
        volumetric_flow_rate
    ):

        if reactor_volume <= 0:
            return "Error: Reactor volume must be positive."

        if volumetric_flow_rate <= 0:
            return "Error: Flow rate must be positive."

        result = (
            reactor_volume /
            volumetric_flow_rate
        )

        self.history.append(
            f"Residence Time: {result:.3f} s"
        )

        return round(result, 3)


    # --------------------------------------
    # Reactor Conversion
    # X = ((FA0-FA)/FA0)*100
    # --------------------------------------
    def reactor_conversion(
        self,
        inlet_moles,
        outlet_moles
    ):

        if inlet_moles <= 0:
            return "Error: Inlet moles must be positive."

        if outlet_moles < 0:
            return "Error: Outlet moles cannot be negative."

        if outlet_moles > inlet_moles:
            return "Error: Outlet cannot exceed inlet."

        result = (
            (inlet_moles - outlet_moles)
            / inlet_moles
        ) * 100

        self.history.append(
            f"Conversion: {result:.2f}%"
        )

        return round(result, 2)


    # --------------------------------------
    # Half Life
    # t1/2 = 0.693/k
    # First order only
    # --------------------------------------
    def half_life(self, rate_constant):

        if rate_constant <= 0:
            return "Error: Rate constant must be positive."

        result = 0.693 / rate_constant

        self.history.append(
            f"Half Life: {result:.3f} s"
        )

        return round(result, 3)


    # --------------------------------------
    # CSTR Reactor Volume
    # V = FA0X / (-rA)
    # --------------------------------------
    def cstr_volume(
        self,
        inlet_molar_flow,
        conversion,
        reaction_rate
    ):

        if inlet_molar_flow <= 0:
            return "Error: Molar flow must be positive."

        if conversion < 0 or conversion > 1:
            return "Error: Conversion must be between 0 and 1."

        if reaction_rate <= 0:
            return "Error: Reaction rate must be positive."

        result = (
            inlet_molar_flow *
            conversion /
            reaction_rate
        )

        self.history.append(
            f"CSTR Volume: {result:.3f} m³"
        )

        return round(result, 3)


    # --------------------------------------
    # PFR Reactor Volume
    # Simplified:
    # V = FA0X / (-rA)
    # --------------------------------------
    def pfr_volume(
        self,
        inlet_molar_flow,
        conversion,
        reaction_rate
    ):

        if inlet_molar_flow <= 0:
            return "Error: Molar flow must be positive."

        if conversion < 0 or conversion > 1:
            return "Error: Conversion must be between 0 and 1."

        if reaction_rate <= 0:
            return "Error: Reaction rate must be positive."

        result = (
            inlet_molar_flow *
            conversion /
            reaction_rate
        )

        self.history.append(
            f"PFR Volume: {result:.3f} m³"
        )

        return round(result, 3)


    # --------------------------------------
    # Equilibrium Constant
    # K = Products / Reactants
    # --------------------------------------
    def equilibrium_constant(
        self,
        products,
        reactants
    ):

        if reactants <= 0:
            return "Error: Reactants must be positive."

        result = products / reactants

        self.history.append(
            f"Equilibrium Constant: {result:.6f}"
        )

        return round(result, 6)