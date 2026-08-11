import math

from constants import STEFAN_BOLTZMANN


class HeatTransfer:

    def __init__(self):
        self.history = []

    # --------------------------------
    # Fourier's Law of Heat Conduction
    # Q = k A (T1 - T2) / L
    # --------------------------------
    def heat_conduction(
        self,
        k,
        area,
        t1,
        t2,
        thickness
    ):

        if k <= 0:
            raise ValueError(
                "Thermal conductivity must be greater than zero."
            )

        if area <= 0:
            raise ValueError(
                "Area must be greater than zero."
            )

        if thickness <= 0:
            raise ValueError(
                "Thickness must be greater than zero."
            )

        result = (
            k
            * area
            * (t1 - t2)
            / thickness
        )

        self.history.append(
            f"Heat Conduction: "
            f"({k} × {area} × ({t1} - {t2})) / "
            f"{thickness} = {result:.3f} W"
        )

        return round(result, 3)

    # --------------------------------
    # Newton's Law of Cooling
    # Q = h A (Ts - Tf)
    # --------------------------------
    def heat_convection(
        self,
        h,
        area,
        surface_temperature,
        fluid_temperature
    ):

        if h <= 0:
            raise ValueError(
                "Heat transfer coefficient must be greater than zero."
            )

        if area <= 0:
            raise ValueError(
                "Area must be greater than zero."
            )

        result = (
            h
            * area
            * (
                surface_temperature
                - fluid_temperature
            )
        )

        self.history.append(
            f"Heat Convection: "
            f"{h} × {area} × "
            f"({surface_temperature} - {fluid_temperature}) "
            f"= {result:.3f} W"
        )

        return round(result, 3)

    # --------------------------------
    # Stefan-Boltzmann Radiation
    #
    # Q = ε σ A (Ts⁴ - Tsur⁴)
    #
    # Temperatures MUST be Kelvin.
    # --------------------------------
    def heat_radiation(
        self,
        emissivity,
        area,
        surface_temperature,
        surrounding_temperature
    ):

        if not 0 <= emissivity <= 1:
            raise ValueError(
                "Emissivity must be between 0 and 1."
            )

        if area <= 0:
            raise ValueError(
                "Area must be greater than zero."
            )

        if surface_temperature <= 0:
            raise ValueError(
                "Surface temperature must be greater than zero Kelvin."
            )

        if surrounding_temperature <= 0:
            raise ValueError(
                "Surrounding temperature must be greater than zero Kelvin."
            )

        result = (
            emissivity
            * STEFAN_BOLTZMANN
            * area
            * (
                surface_temperature ** 4
                - surrounding_temperature ** 4
            )
        )

        self.history.append(
            f"Heat Radiation: {result:.3f} W"
        )

        return round(result, 3)

    # --------------------------------
    # Overall Heat Transfer Coefficient
    #
    # U = Q / (A ΔT)
    # --------------------------------
    def overall_heat_transfer_coefficient(
        self,
        heat_rate,
        area,
        temperature_difference
    ):

        if area <= 0:
            raise ValueError(
                "Area must be greater than zero."
            )

        if temperature_difference == 0:
            raise ValueError(
                "Temperature difference cannot be zero."
            )

        result = (
            heat_rate
            / (
                area
                * temperature_difference
            )
        )

        self.history.append(
            f"Overall Heat Transfer Coefficient: "
            f"{result:.3f} W/m²·K"
        )

        return round(result, 3)

    # --------------------------------
    # Log Mean Temperature Difference
    #
    # LMTD = (ΔT1 - ΔT2) /
    #        ln(ΔT1 / ΔT2)
    # --------------------------------
    def lmtd(
        self,
        delta_t1,
        delta_t2
    ):

        if delta_t1 <= 0:
            raise ValueError(
                "Delta T1 must be greater than zero."
            )

        if delta_t2 <= 0:
            raise ValueError(
                "Delta T2 must be greater than zero."
            )

        if delta_t1 == delta_t2:
            result = delta_t1

        else:
            result = (
                delta_t1
                - delta_t2
            ) / math.log(
                delta_t1 / delta_t2
            )

        self.history.append(
            f"LMTD = {result:.3f} K"
        )

        return round(result, 3)

    # --------------------------------
    # Heat Exchanger Effectiveness
    #
    # ε = Qactual / Qmax
    # --------------------------------
    def heat_exchanger_effectiveness(
        self,
        actual_heat_transfer,
        maximum_heat_transfer
    ):

        if actual_heat_transfer < 0:
            raise ValueError(
                "Actual heat transfer cannot be negative."
            )

        if maximum_heat_transfer <= 0:
            raise ValueError(
                "Maximum heat transfer must be greater than zero."
            )

        if actual_heat_transfer > maximum_heat_transfer:
            raise ValueError(
                "Actual heat transfer cannot exceed "
                "maximum heat transfer."
            )

        result = (
            actual_heat_transfer
            / maximum_heat_transfer
        ) * 100

        self.history.append(
            f"Heat Exchanger Effectiveness = "
            f"{result:.2f}%"
        )

        return round(result, 2)