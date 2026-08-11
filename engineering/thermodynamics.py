class Thermodynamics:

    def __init__(self):
        self.history = []


    def ideal_gas_law(self, pressure, volume, temperature):

        R = 8.314

        if temperature == 0:
            return "Error: Temperature cannot be zero."

        result = (pressure * volume) / (R * temperature)

        self.history.append(
            f"Ideal Gas Law: {result}"
        )

        return result


    def boyles_law(self, pressure1, volume1, volume2):

        if volume2 == 0:
            return "Error: Final volume cannot be zero."

        result = (pressure1 * volume1) / volume2

        self.history.append(
            f"Boyle's Law: {result}"
        )

        return result


    def charles_law(self, volume1, temperature1, temperature2):

        if temperature1 == 0:
            return "Error: Initial temperature cannot be zero."

        result = (volume1 * temperature2) / temperature1

        self.history.append(
            f"Charles's Law: {result}"
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

        if temperature1 == 0:
            return "Error: Initial temperature cannot be zero."

        if volume2 == 0:
            return "Error: Final volume cannot be zero."

        result = (
            pressure1
            * volume1
            * temperature2
            /
            (temperature1 * volume2)
        )

        self.history.append(
            f"Combined Gas Law: {result}"
        )

        return result


    def specific_heat(
        self,
        mass,
        specific_heat_capacity,
        temperature_change
    ):

        result = (
            mass
            * specific_heat_capacity
            * temperature_change
        )

        self.history.append(
            f"Specific Heat: {result}"
        )

        return result


    def enthalpy_change(
        self,
        mass,
        cp,
        temperature_change
    ):

        result = mass * cp * temperature_change

        self.history.append(
            f"Enthalpy Change: {result}"
        )

        return result