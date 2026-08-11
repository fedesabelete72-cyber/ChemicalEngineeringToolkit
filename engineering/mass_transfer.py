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
            return "Error: Diffusion coefficient must be positive."

        if distance <= 0:
            return "Error: Distance must be positive."

        result = (
            -diffusion_coefficient
            * (concentration_difference / distance)
        )

        self.history.append(
            f"Fick's First Law: J = {result:.6f} mol/m²·s"
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
            return "Error: Concentration difference cannot be zero."

        if distance <= 0:
            return "Error: Distance must be positive."

        result = (
            -mass_flux
            * distance
            / concentration_difference
        )

        self.history.append(
            f"Diffusion Coefficient: D = {result:.8f} m²/s"
        )

        return round(result, 8)

    # ----------------------------------
    # Mass Flux
    # J = ṁ/A
    # ----------------------------------
    def mass_flux(self, mass_flow_rate, area):

        if area <= 0:
            return "Error: Area must be positive."

        result = mass_flow_rate / area

        self.history.append(
            f"Mass Flux: {result:.6f} kg/m²·s"
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
            return "Error: Mass transfer coefficient must be positive."

        result = (
            mass_transfer_coefficient
            * (surface_concentration - bulk_concentration)
        )

        self.history.append(
            f"Convective Mass Transfer = {result:.6f}"
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
            return "Error: Mass transfer coefficient must be positive."

        if characteristic_length <= 0:
            return "Error: Characteristic length must be positive."

        if diffusion_coefficient <= 0:
            return "Error: Diffusion coefficient must be positive."

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
            return "Error: Viscosity must be positive."

        if density <= 0:
            return "Error: Density must be positive."

        if diffusion_coefficient <= 0:
            return "Error: Diffusion coefficient must be positive."

        result = viscosity / (
            density * diffusion_coefficient
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
            return "Error: Thermal diffusivity must be positive."

        if diffusion_coefficient <= 0:
            return "Error: Diffusion coefficient must be positive."

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
            return "Error: Reynolds number must be positive."

        if schmidt_number <= 0:
            return "Error: Schmidt number must be positive."

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
            return "Error: Concentration difference cannot be zero."

        result = (
            mass_flux
            / concentration_difference
        )

        self.history.append(
            f"Overall Mass Transfer Coefficient: {result:.6f}"
        )

        return round(result, 6) 