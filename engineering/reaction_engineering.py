import math

from constants import R


class ReactionEngineering:

    def __init__(self):
        self.history = []

    # --------------------------------------
    # Reaction Rate
    #
    # -rA = k(CA)^n
    # --------------------------------------
    def reaction_rate(
        self,
        rate_constant,
        concentration,
        reaction_order
    ):

        if rate_constant <= 0:
            raise ValueError(
                "Rate constant must be greater than zero."
            )

        if concentration < 0:
            raise ValueError(
                "Concentration cannot be negative."
            )

        if reaction_order < 0:
            raise ValueError(
                "Reaction order cannot be negative."
            )

        result = (
            rate_constant
            * concentration ** reaction_order
        )

        self.history.append(
            f"Reaction Rate: {result:.6f}"
        )

        return round(result, 6)

    # --------------------------------------
    # First Order Reaction
    #
    # CA = CA0 e^(-kt)
    # --------------------------------------
    def first_order_reaction(
        self,
        initial_concentration,
        rate_constant,
        time
    ):

        if initial_concentration < 0:
            raise ValueError(
                "Initial concentration cannot be negative."
            )

        if rate_constant <= 0:
            raise ValueError(
                "Rate constant must be greater than zero."
            )

        if time < 0:
            raise ValueError(
                "Time cannot be negative."
            )

        result = (
            initial_concentration
            * math.exp(
                -rate_constant * time
            )
        )

        self.history.append(
            f"First Order Reaction: "
            f"CA = {result:.6f}"
        )

        return round(result, 6)

    # --------------------------------------
    # Second Order Reaction
    #
    # CA = CA0 / (1 + k CA0 t)
    # --------------------------------------
    def second_order_reaction(
        self,
        initial_concentration,
        rate_constant,
        time
    ):

        if initial_concentration <= 0:
            raise ValueError(
                "Initial concentration must "
                "be greater than zero."
            )

        if rate_constant <= 0:
            raise ValueError(
                "Rate constant must be greater than zero."
            )

        if time < 0:
            raise ValueError(
                "Time cannot be negative."
            )

        denominator = (
            1
            + rate_constant
            * initial_concentration
            * time
        )

        if denominator <= 0:
            raise ValueError(
                "Invalid inputs produced a "
                "non-positive denominator."
            )

        result = (
            initial_concentration
            / denominator
        )

        self.history.append(
            f"Second Order Reaction: "
            f"CA = {result:.6f}"
        )

        return round(result, 6)

    # --------------------------------------
    # Arrhenius Equation
    #
    # k = A exp(-Ea / RT)
    #
    # Temperature MUST be Kelvin.
    # --------------------------------------
    def arrhenius_equation(
        self,
        frequency_factor,
        activation_energy,
        temperature
    ):

        if frequency_factor <= 0:
            raise ValueError(
                "Frequency factor must "
                "be greater than zero."
            )

        if activation_energy < 0:
            raise ValueError(
                "Activation energy cannot be negative."
            )

        if temperature <= 0:
            raise ValueError(
                "Temperature must be greater "
                "than zero Kelvin."
            )

        result = (
            frequency_factor
            * math.exp(
                -activation_energy
                / (R * temperature)
            )
        )

        self.history.append(
            f"Arrhenius Equation: "
            f"k = {result:.8f}"
        )

        return round(result, 8)

    # --------------------------------------
    # Residence Time
    #
    # τ = V / Q
    # --------------------------------------
    def residence_time(
        self,
        reactor_volume,
        volumetric_flow_rate
    ):

        if reactor_volume <= 0:
            raise ValueError(
                "Reactor volume must "
                "be greater than zero."
            )

        if volumetric_flow_rate <= 0:
            raise ValueError(
                "Volumetric flow rate must "
                "be greater than zero."
            )

        result = (
            reactor_volume
            / volumetric_flow_rate
        )

        self.history.append(
            f"Residence Time: "
            f"{result:.3f} s"
        )

        return round(result, 3)

    # --------------------------------------
    # Reactor Conversion
    #
    # X = ((FA0 - FA) / FA0) × 100
    # --------------------------------------
    def reactor_conversion(
        self,
        inlet_moles,
        outlet_moles
    ):

        if inlet_moles <= 0:
            raise ValueError(
                "Inlet moles must "
                "be greater than zero."
            )

        if outlet_moles < 0:
            raise ValueError(
                "Outlet moles cannot be negative."
            )

        if outlet_moles > inlet_moles:
            raise ValueError(
                "Outlet moles cannot exceed "
                "inlet moles."
            )

        result = (
            (inlet_moles - outlet_moles)
            / inlet_moles
        ) * 100

        self.history.append(
            f"Conversion: {result:.2f}%"
        )

        return round(result, 2)

    # --------------------------------------
    # First-Order Half Life
    #
    # t1/2 = ln(2) / k
    # --------------------------------------
    def half_life(self, rate_constant):

        if rate_constant <= 0:
            raise ValueError(
                "Rate constant must "
                "be greater than zero."
            )

        result = math.log(2) / rate_constant

        self.history.append(
            f"Half Life: {result:.3f} s"
        )

        return round(result, 3)

    # --------------------------------------
    # CSTR Reactor Volume
    #
    # V = FA0 X / (-rA)
    # --------------------------------------
    def cstr_volume(
        self,
        inlet_molar_flow,
        conversion,
        reaction_rate
    ):

        if inlet_molar_flow <= 0:
            raise ValueError(
                "Molar flow must "
                "be greater than zero."
            )

        if not 0 <= conversion <= 1:
            raise ValueError(
                "Conversion must be "
                "between 0 and 1."
            )

        if reaction_rate <= 0:
            raise ValueError(
                "Reaction rate must "
                "be greater than zero."
            )

        result = (
            inlet_molar_flow
            * conversion
            / reaction_rate
        )

        self.history.append(
            f"CSTR Volume: {result:.3f} m³"
        )

        return round(result, 3)

    # --------------------------------------
    # Simplified PFR Reactor Volume
    #
    # V ≈ FA0 X / (-rA)
    #
    # NOTE:
    # This is an approximation using a
    # representative/constant reaction rate.
    # General PFR design requires integration:
    #
    # V = FA0 ∫(dX / -rA)
    # --------------------------------------
    def pfr_volume(
        self,
        inlet_molar_flow,
        conversion,
        reaction_rate
    ):

        if inlet_molar_flow <= 0:
            raise ValueError(
                "Molar flow must "
                "be greater than zero."
            )

        if not 0 <= conversion <= 1:
            raise ValueError(
                "Conversion must be "
                "between 0 and 1."
            )

        if reaction_rate <= 0:
            raise ValueError(
                "Reaction rate must "
                "be greater than zero."
            )

        result = (
            inlet_molar_flow
            * conversion
            / reaction_rate
        )

        self.history.append(
            f"Simplified PFR Volume: "
            f"{result:.3f} m³"
        )

        return round(result, 3)

    # --------------------------------------
    # Simplified Equilibrium Constant
    #
    # K = Products / Reactants
    #
    # Educational simplified form.
    # --------------------------------------
    def equilibrium_constant(
        self,
        products,
        reactants
    ):

        if products < 0:
            raise ValueError(
                "Products cannot be negative."
            )

        if reactants <= 0:
            raise ValueError(
                "Reactants must "
                "be greater than zero."
            )

        result = products / reactants

        self.history.append(
            f"Equilibrium Constant: "
            f"{result:.6f}"
        )

        return round(result, 6)