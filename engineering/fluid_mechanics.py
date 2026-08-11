class FluidMechanics:

    def __init__(self):
        self.history = []

    def density(self, mass, volume):

        if volume == 0:
            return "Error: Volume cannot be zero."

        result = mass / volume

        self.history.append(
            f"Density: {mass} / {volume} = {result}"
        )

        return result


    def reynolds_number(
        self,
        density,
        velocity,
        diameter,
        viscosity
    ):

        if viscosity == 0:
            return "Error: Viscosity cannot be zero."

        result = (
            density
            * velocity
            * diameter
            / viscosity
        )

        self.history.append(
            f"Reynolds Number: {result}"
        )

        return result


    def flow_rate(self, area, velocity):

        if area < 0 or velocity < 0:
            return "Error: Area and velocity must be positive."

        result = area * velocity

        self.history.append(
            f"Flow Rate: {area} × {velocity} = {result} m³/s"
        )

        return result


    def velocity(self, flow_rate, area):

        if area == 0:
            return "Error: Area cannot be zero."

        result = flow_rate / area

        self.history.append(
            f"Velocity: {flow_rate} / {area} = {result} m/s"
        )

        return result


    def pressure_drop(
        self,
        friction_factor,
        length,
        diameter,
        density,
        velocity
    ):

        if diameter == 0:
            return "Error: Diameter cannot be zero."

        result = (
            friction_factor
            * (length / diameter)
            * ((density * velocity ** 2) / 2)
        )

        self.history.append(
            f"Pressure Drop: {result} Pa"
        )

        return result