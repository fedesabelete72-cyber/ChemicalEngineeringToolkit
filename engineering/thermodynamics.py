from constants import R


class Thermodynamics:

    def __init__(self):
        self.history = []

    def ideal_gas_law(self, pressure, volume, temperature):

        if pressure <= 0:
            raise ValueError(
                "Pressure must be greater than zero."
            )

        if volume <= 0:
            raise ValueError(
                "Volume must be greater than zero."
            )

        if temperature <= 0:
            raise ValueError(
                "Temperature must be greater than zero Kelvin."
            )

        result = (pressure * volume) / (R * temperature)

        self.history.append(
            f"Ideal Gas Law: {result} mol"
        )

        return result

    def boyles_law(
        self,
        pressure1,
        volume1,
        volume2
    ):

        if pressure1 <= 0:
            raise ValueError(
                "Initial pressure must be greater than zero."
            )

        if volume1 <= 0:
            raise ValueError(
                "Initial volume must be greater than zero."
            )

        if volume2 <= 0:
            raise ValueError(
                "Final volume must be greater than zero."
            )

        result = (pressure1 * volume1) / volume2

        self.history.append(
            f"Boyle's Law: {result} Pa"
        )

        return result

    def charles_law(
        self,
        volume1,
        temperature1,
        temperature2
    ):

        if volume1 <= 0:
            raise ValueError(
                "Initial volume must be greater than zero."
            )

        if temperature1 <= 0:
            raise ValueError(
                "Initial temperature must be greater than zero Kelvin."
            )

        if temperature2 <= 0:
            raise ValueError(
                "Final temperature must be greater than zero Kelvin."
            )

        result = (
            volume1
            * temperature2
            / temperature1
        )

        self.history.append(
            f"Charles's Law: {result} m³"
        )

        return result

    def combined_gas_law(
        self,
        pressure1,
        volume1,
        temperature1,
        volume2,
        temperature2
    ):

        if pressure1 <= 0:
            raise ValueError(
                "Initial pressure must be greater than zero."
            )

        if volume1 <= 0:
            raise ValueError(
                "Initial volume must be greater than zero."
            )

        if temperature1 <= 0:
            raise ValueError(
                "Initial temperature must be greater than zero Kelvin."
            )

        if volume2 <= 0:
            raise ValueError(
                "Final volume must be greater than zero."
            )

        if temperature2 <= 0:
            raise ValueError(
                "Final temperature must be greater than zero Kelvin."
            )

        result = (
            pressure1
            * volume1
            * temperature2
            /
            (temperature1 * volume2)
        )

        self.history.append(
            f"Combined Gas Law: {result} Pa"
        )

        return result

    def specific_heat(
        self,
        mass,
        specific_heat_capacity,
        temperature_change
    ):

        if mass < 0:
            raise ValueError(
                "Mass cannot be negative."
            )

        if specific_heat_capacity <= 0:
            raise ValueError(
                "Specific heat capacity must be greater than zero."
            )

        result = (
            mass
            * specific_heat_capacity
            * temperature_change
        )

        self.history.append(
            f"Specific Heat: {result} J"
        )

        return result

    def enthalpy_change(
        self,
        mass,
        cp,
        temperature_change
    ):

        if mass < 0:
            raise ValueError(
                "Mass cannot be negative."
            )

        if cp <= 0:
            raise ValueError(
                "Heat capacity (Cp) must be greater than zero."
            )

        result = (
            mass
            * cp
            * temperature_change
        )

        self.history.append(
            f"Enthalpy Change: {result} J"
        )

        return result