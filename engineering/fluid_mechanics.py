class FluidMechanics:

    def __init__(self):
        self.history = []

    def density(self, mass, volume):

        if mass < 0:
            raise ValueError("Mass cannot be negative.")

        if volume <= 0:
            raise ValueError("Volume must be greater than zero.")

        result = mass / volume

        self.history.append(
            f"Density: {mass} / {volume} = {result} kg/m³"
        )

        return result

    def reynolds_number(
        self,
        density,
        velocity,
        diameter,
        viscosity
    ):

        if density <= 0:
            raise ValueError(
                "Density must be greater than zero."
            )

        if velocity < 0:
            raise ValueError(
                "Velocity cannot be negative."
            )

        if diameter <= 0:
            raise ValueError(
                "Diameter must be greater than zero."
            )

        if viscosity <= 0:
            raise ValueError(
                "Viscosity must be greater than zero."
            )

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

        if area <= 0:
            raise ValueError(
                "Area must be greater than zero."
            )

        if velocity < 0:
            raise ValueError(
                "Velocity cannot be negative."
            )

        result = area * velocity

        self.history.append(
            f"Flow Rate: {area} × {velocity} = {result} m³/s"
        )

        return result

    def velocity(self, flow_rate, area):

        if flow_rate < 0:
            raise ValueError(
                "Flow rate cannot be negative."
            )

        if area <= 0:
            raise ValueError(
                "Area must be greater than zero."
            )

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

        if friction_factor < 0:
            raise ValueError(
                "Friction factor cannot be negative."
            )

        if length < 0:
            raise ValueError(
                "Length cannot be negative."
            )

        if diameter <= 0:
            raise ValueError(
                "Diameter must be greater than zero."
            )

        if density <= 0:
            raise ValueError(
                "Density must be greater than zero."
            )

        if velocity < 0:
            raise ValueError(
                "Velocity cannot be negative."
            )

        result = (
            friction_factor
            * (length / diameter)
            * ((density * velocity ** 2) / 2)
        )

        self.history.append(
            f"Pressure Drop: {result} Pa"
        )

        return result