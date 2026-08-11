class MaterialBalance:

    def __init__(self):
        self.history = []

    def overall_mass_balance(self, mass_in, accumulation):

        if mass_in < 0:
            raise ValueError(
                "Mass entering the system cannot be negative."
            )

        if accumulation < 0:
            raise ValueError(
                "Accumulation cannot be negative."
            )

        result = mass_in - accumulation

        self.history.append(
            f"Overall Mass Balance: "
            f"{mass_in} - {accumulation} = {result} kg"
        )

        return result

    def component_balance(self, component_in, accumulation):

        if component_in < 0:
            raise ValueError(
                "Component entering the system cannot be negative."
            )

        if accumulation < 0:
            raise ValueError(
                "Accumulation cannot be negative."
            )

        result = component_in - accumulation

        self.history.append(
            f"Component Balance: "
            f"{component_in} - {accumulation} = {result} kg"
        )

        return result

    def conversion(self, initial_amount, final_amount):

        if initial_amount <= 0:
            raise ValueError(
                "Initial amount must be greater than zero."
            )

        if final_amount < 0:
            raise ValueError(
                "Final amount cannot be negative."
            )

        if final_amount > initial_amount:
            raise ValueError(
                "Final amount cannot exceed initial amount "
                "for this conversion calculation."
            )

        result = (
            (initial_amount - final_amount)
            / initial_amount
        ) * 100

        self.history.append(
            f"Conversion: {result:.2f}%"
        )

        return round(result, 2)

    def yield_percentage(
        self,
        actual_product,
        theoretical_product
    ):

        if actual_product < 0:
            raise ValueError(
                "Actual product cannot be negative."
            )

        if theoretical_product <= 0:
            raise ValueError(
                "Theoretical product must be greater than zero."
            )

        if actual_product > theoretical_product:
            raise ValueError(
                "Actual product cannot exceed "
                "theoretical product."
            )

        result = (
            actual_product
            / theoretical_product
        ) * 100

        self.history.append(
            f"Yield: {result:.2f}%"
        )

        return round(result, 2)

    def selectivity(
        self,
        desired_product,
        undesired_product
    ):

        if desired_product < 0:
            raise ValueError(
                "Desired product cannot be negative."
            )

        if undesired_product <= 0:
            raise ValueError(
                "Undesired product must be greater than zero."
            )

        result = (
            desired_product
            / undesired_product
        )

        self.history.append(
            f"Selectivity: "
            f"{desired_product} / "
            f"{undesired_product} = {result}"
        )

        return round(result, 3)

    def recycle_ratio(
        self,
        recycle_stream,
        fresh_feed
    ):

        if recycle_stream < 0:
            raise ValueError(
                "Recycle stream cannot be negative."
            )

        if fresh_feed <= 0:
            raise ValueError(
                "Fresh feed must be greater than zero."
            )

        result = recycle_stream / fresh_feed

        self.history.append(
            f"Recycle Ratio: "
            f"{recycle_stream} / "
            f"{fresh_feed} = {result}"
        )

        return round(result, 3)

    def purge_ratio(
        self,
        purge_stream,
        recycle_stream
    ):

        if purge_stream < 0:
            raise ValueError(
                "Purge stream cannot be negative."
            )

        if recycle_stream <= 0:
            raise ValueError(
                "Recycle stream must be greater than zero."
            )

        result = purge_stream / recycle_stream

        self.history.append(
            f"Purge Ratio: "
            f"{purge_stream} / "
            f"{recycle_stream} = {result}"
        )

        return round(result, 3)

    def mixing(
        self,
        mass1,
        composition1,
        mass2,
        composition2
    ):

        if mass1 < 0 or mass2 < 0:
            raise ValueError(
                "Mass values cannot be negative."
            )

        if not 0 <= composition1 <= 1:
            raise ValueError(
                "Composition 1 must be between 0 and 1."
            )

        if not 0 <= composition2 <= 1:
            raise ValueError(
                "Composition 2 must be between 0 and 1."
            )

        total_mass = mass1 + mass2

        if total_mass <= 0:
            raise ValueError(
                "Total mass must be greater than zero."
            )

        mixed_composition = (
            (mass1 * composition1)
            + (mass2 * composition2)
        ) / total_mass

        self.history.append(
            f"Mixing: Total Mass = {total_mass}, "
            f"Composition = {mixed_composition}"
        )

        return (
            round(total_mass, 3),
            round(mixed_composition, 3)
        )

    def separation_efficiency(
        self,
        recovered,
        feed
    ):

        if recovered < 0:
            raise ValueError(
                "Recovered amount cannot be negative."
            )

        if feed <= 0:
            raise ValueError(
                "Feed must be greater than zero."
            )

        if recovered > feed:
            raise ValueError(
                "Recovered amount cannot exceed feed."
            )

        result = (recovered / feed) * 100

        self.history.append(
            f"Separation Efficiency: "
            f"({recovered} / {feed}) × 100 = {result}%"
        )

        return round(result, 2)