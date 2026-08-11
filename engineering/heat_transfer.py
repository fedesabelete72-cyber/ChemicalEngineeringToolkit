import math


class HeatTransfer:

    def __init__(self):
        self.history = []

    # -------------------------------
    # Fourier's Law of Heat Conduction
    # -------------------------------
    def heat_conduction(self, k, area, t1, t2, thickness):

        if k <= 0:
            return "Error: Thermal conductivity must be positive."

        if area <= 0:
            return "Error: Area must be positive."

        if thickness <= 0:
            return "Error: Thickness must be positive."

        result = (k * area * (t1 - t2)) / thickness

        self.history.append(
            f"Heat Conduction: ({k} × {area} × ({t1} - {t2})) / {thickness} = {result:.3f} W"
        )

        return round(result, 3)

    # -------------------------------
    # Newton's Law of Cooling
    # -------------------------------
    def heat_convection(self, h, area, surface_temperature, fluid_temperature):

        if h <= 0:
            return "Error: Heat transfer coefficient must be positive."

        if area <= 0:
            return "Error: Area must be positive."

        result = h * area * (surface_temperature - fluid_temperature)

        self.history.append(
            f"Heat Convection: {h} × {area} × ({surface_temperature} - {fluid_temperature}) = {result:.3f} W"
        )

        return round(result, 3)

    # -------------------------------
    # Stefan-Boltzmann Radiation
    # Temperatures MUST be in Kelvin
    # -------------------------------
    def heat_radiation(
        self,
        emissivity,
        area,
        surface_temperature,
        surrounding_temperature
    ):

        if emissivity < 0 or emissivity > 1:
            return "Error: Emissivity must be between 0 and 1."

        if area <= 0:
            return "Error: Area must be positive."

        if surface_temperature <= 0 or surrounding_temperature <= 0:
            return "Error: Temperatures must be in Kelvin and greater than zero."

        sigma = 5.670374419e-8

        result = (
            emissivity
            * sigma
            * area
            * (
                surface_temperature**4
                - surrounding_temperature**4
            )
        )

        self.history.append(
            f"Heat Radiation = {result:.3f} W"
        )

        return round(result, 3)

    # ------------------------------------
    # Overall Heat Transfer Coefficient
    # U = Q / (A ΔT)
    # ------------------------------------
    def overall_heat_transfer_coefficient(
        self,
        heat_rate,
        area,
        temperature_difference
    ):

        if area <= 0:
            return "Error: Area must be positive."

        if temperature_difference == 0:
            return "Error: Temperature difference cannot be zero."

        result = heat_rate / (
            area * temperature_difference
        )

        self.history.append(
            f"Overall Heat Transfer Coefficient = {result:.3f} W/m²·K"
        )

        return round(result, 3)

    # ------------------------------------
    # Log Mean Temperature Difference (LMTD)
    # ------------------------------------
    def lmtd(self, delta_t1, delta_t2):

        if delta_t1 <= 0 or delta_t2 <= 0:
            return "Error: Temperature differences must be positive."

        if delta_t1 == delta_t2:
            result = delta_t1
        else:
            result = (
                delta_t1 - delta_t2
            ) / math.log(delta_t1 / delta_t2)

        self.history.append(
            f"LMTD = {result:.3f} K"
        )

        return round(result, 3)

    # ------------------------------------
    # Heat Exchanger Effectiveness
    # ε = Q_actual / Q_max
    # ------------------------------------
    def heat_exchanger_effectiveness(
        self,
        actual_heat_transfer,
        maximum_heat_transfer
    ):

        if maximum_heat_transfer <= 0:
            return "Error: Maximum heat transfer must be positive."

        result = (
            actual_heat_transfer
            / maximum_heat_transfer
        ) * 100

        self.history.append(
            f"Heat Exchanger Effectiveness = {result:.2f}%"
        )

        return round(result, 2)    