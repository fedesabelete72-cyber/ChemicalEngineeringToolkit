class MaterialBalance:

    def __init__(self):
        self.history = []
    def overall_mass_balance(self, mass_in, accumulation):
    
            result = mass_in - accumulation
    
            self.history.append(
                f"Overall Mass Balance: {mass_in} - {accumulation} = {result} kg"
            )
    
            return result
    def component_balance(self, component_in, accumulation):
    
            result = component_in - accumulation
    
            self.history.append(
                f"Component Balance: {component_in} - {accumulation} = {result} kg"
            )
    
            return result
    
    def conversion(self, initial_amount, final_amount):
    
            if initial_amount == 0:
                return "Error: Initial amount cannot be zero."
    
            result = ((initial_amount - final_amount) / initial_amount) * 100
    
            self.history.append(
                f"Conversion: {result:.2f}%"
            )
    
            return round(result, 2)
    def yield_percentage(self, actual_product, theoretical_product):
    
            if theoretical_product == 0:
                return "Error: Theoretical product cannot be zero."
    
            result = (actual_product / theoretical_product) * 100
    
            self.history.append(
                f"Yield: {result:.2f}%"
            )
    
            return round(result, 2)
    def selectivity(self, desired_product, undesired_product):
    
            if undesired_product == 0:
                return "Error: Undesired product cannot be zero."
    
            result = desired_product / undesired_product
    
            self.history.append(
                f"Selectivity: {desired_product} / {undesired_product} = {result}"
            )
    
            return round(result, 3)
    
    def recycle_ratio(self, recycle_stream, fresh_feed):
    
            if fresh_feed == 0:
                return "Error: Fresh feed cannot be zero."
    
            result = recycle_stream / fresh_feed
    
            self.history.append(
                f"Recycle Ratio: {recycle_stream} / {fresh_feed} = {result}"
            )
    
            return round(result, 3)
    
    def purge_ratio(self, purge_stream, recycle_stream):
    
            if recycle_stream == 0:
                return "Error: Recycle stream cannot be zero."
    
            result = purge_stream / recycle_stream
    
            self.history.append(
                f"Purge Ratio: {purge_stream} / {recycle_stream} = {result}"
            )
    
            return round(result, 3)
    
    def mixing(self, mass1, composition1, mass2, composition2):
    
            total_mass = mass1 + mass2
    
            if total_mass == 0:
                return "Error: Total mass cannot be zero."
    
            mixed_composition = (
                (mass1 * composition1) +
                (mass2 * composition2)
            ) / total_mass
    
            self.history.append(
                f"Mixing: Total Mass = {total_mass}, Composition = {mixed_composition}"
            )
    
            return round(total_mass, 3), round(mixed_composition, 3)
    
    def separation_efficiency(self, recovered, feed):
    
            if feed == 0:
                return "Error: Feed cannot be zero."
    
            result = (recovered / feed) * 100
    
            self.history.append(
                f"Separation Efficiency: ({recovered} / {feed}) × 100 = {result}%"
            )
    
            return round(result, 2)