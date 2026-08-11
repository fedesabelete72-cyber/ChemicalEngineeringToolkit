class MassTransfer:

    def __init__(self):
        self.history = []

    # ----------------------------------
    # Fick's First Law
    # J = -D(ΔC/Δx)
    # ----------------------------------
    def ficks_first_law(
        self,
        diffusion_coefficient,
        concentration_difference,
        distance,
    ):

        if diffusion_coefficient <= 0:
            raise ValueError(
                "Diffusion coefficient must be greater than zero."
            )

        if distance <= 0:
            raise ValueError(
                "Distance must be greater than zero."
            )

        result = (
            -diffusion_coefficient
            * (
                concentration_difference
                / distance
            )
        )

        self.history.append(
            f"Fick's First Law: "
            f"J = {result:.6f} mol/m²·s"
        )

        return round(result, 6)

    # ----------------------------------
    # Calculate Diffusion Coefficient
    # D = -JΔx/ΔC
    # ----------------------------------
    def calculate_diffusion_coefficient(
        self,
        mass_flux,
        concentration_difference,
        distance,
    ):

        if concentration_difference == 0:
            raise ValueError(
                "Concentration difference cannot be zero."
            )

        if distance <= 0:
            raise ValueError(
                "Distance must be greater than zero."
            )

        result = (
            -mass_flux
            * distance
            / concentration_difference
        )

        if result <= 0:
            raise ValueError(
                "Calculated diffusion coefficient must "
                "be greater than zero. Check the signs "
                "of mass flux and concentration difference."
            )

        self.history.append(
            f"Diffusion Coefficient: "
            f"D = {result:.8f} m²/s"
        )

        return round(result, 8)

    # ----------------------------------
    # Mass Flux
    # J = ṁ/A
    # ----------------------------------
    def mass_flux(
        self,
        mass_flow_rate,
        area
    ):

        if area <= 0:
            raise ValueError(
                "Area must be greater than zero."
            )

        # Mass flow rate may be negative because
        # mass flux has a direction.

        result = mass_flow_rate / area

        self.history.append(
            f"Mass Flux: "
            f"{result:.6f} kg/m²·s"
        )

        return round(result, 6)

    # ----------------------------------
    # Convective Mass Transfer
    # N = k(Cₛ - Cᵦ)
    # ----------------------------------
    def convective_mass_transfer(
        self,
        mass_transfer_coefficient,
        surface_concentration,
        bulk_concentration,
    ):

        if mass_transfer_coefficient <= 0:
            raise ValueError(
                "Mass transfer coefficient must "
                "be greater than zero."
            )

        result = (
            mass_transfer_coefficient
            * (
                surface_concentration
                - bulk_concentration
            )
        )

        self.history.append(
            f"Convective Mass Transfer: "
            f"N = {result:.6f}"
        )

        return round(result, 6)

    # ----------------------------------
    # Sherwood Number
    # Sh = kL/D
    # ----------------------------------
    def sherwood_number(
        self,
        mass_transfer_coefficient,
        characteristic_length,
        diffusion_coefficient,
    ):

        if mass_transfer_coefficient <= 0:
            raise ValueError(
                "Mass transfer coefficient must "
                "be greater than zero."
            )

        if characteristic_length <= 0:
            raise ValueError(
                "Characteristic length must "
                "be greater than zero."
            )

        if diffusion_coefficient <= 0:
            raise ValueError(
                "Diffusion coefficient must "
                "be greater than zero."
            )

        result = (
            mass_transfer_coefficient
            * characteristic_length
            / diffusion_coefficient
        )

        self.history.append(
            f"Sherwood Number: {result:.6f}"
        )

        return round(result, 6)

    # ----------------------------------
    # Schmidt Number
    # Sc = μ/(ρD)
    # ----------------------------------
    def schmidt_number(
        self,
        viscosity,
        density,
        diffusion_coefficient
    ):

        if viscosity <= 0:
            raise ValueError(
                "Viscosity must be greater than zero."
            )

        if density <= 0:
            raise ValueError(
                "Density must be greater than zero."
            )

        if diffusion_coefficient <= 0:
            raise ValueError(
                "Diffusion coefficient must "
                "be greater than zero."
            )

        result = (
            viscosity
            / (
                density
                * diffusion_coefficient
            )
        )

        self.history.append(
            f"Schmidt Number: {result:.6f}"
        )

        return round(result, 6)

    # ----------------------------------
    # Lewis Number
    # Le = α/D
    # ----------------------------------
    def lewis_number(
        self,
        thermal_diffusivity,
        diffusion_coefficient
    ):

        if thermal_diffusivity <= 0:
            raise ValueError(
                "Thermal diffusivity must "
                "be greater than zero."
            )

        if diffusion_coefficient <= 0:
            raise ValueError(
                "Diffusion coefficient must "
                "be greater than zero."
            )

        result = (
            thermal_diffusivity
            / diffusion_coefficient
        )

        self.history.append(
            f"Lewis Number: {result:.6f}"
        )

        return round(result, 6)

    # ----------------------------------
    # Peclet Number
    # Pe = Re × Sc
    # ----------------------------------
    def peclet_number(
        self,
        reynolds_number,
        schmidt_number
    ):

        if reynolds_number <= 0:
            raise ValueError(
                "Reynolds number must "
                "be greater than zero."
            )

        if schmidt_number <= 0:
            raise ValueError(
                "Schmidt number must "
                "be greater than zero."
            )

        result = (
            reynolds_number
            * schmidt_number
        )

        self.history.append(
            f"Peclet Number: {result:.6f}"
        )

        return round(result, 6)

    # ----------------------------------
    # Overall Mass Transfer Coefficient
    # K = N/ΔC
    # ----------------------------------
    def overall_mass_transfer_coefficient(
        self,
        mass_flux,
        concentration_difference
    ):

        if concentration_difference == 0:
            raise ValueError(
                "Concentration difference cannot be zero."
            )

        result = (
            mass_flux
            / concentration_difference
        )

        self.history.append(
            f"Overall Mass Transfer Coefficient: "
            f"{result:.6f}"
        )

        return round(result, 6)