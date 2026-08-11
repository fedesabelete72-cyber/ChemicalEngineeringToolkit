class Chemistry:

    def __init__(self):
        self.history = []

    def molar_mass(self, formula):

        atomic_masses = {
            "H": 1.008,
            "C": 12.011,
            "N": 14.007,
            "O": 15.999,
            "F": 18.998,
            "Na": 22.990,
            "Mg": 24.305,
            "Al": 26.982,
            "Si": 28.085,
            "P": 30.974,
            "S": 32.06,
            "Cl": 35.45,
            "K": 39.098,
            "Ca": 40.078,
            "Fe": 55.845
        }

        total_mass = 0

        element = ""
        number = ""

        for char in formula:

            if char.isupper():

                if element:
                    count = int(number) if number else 1

                    if element not in atomic_masses:
                        return f"Unknown element: {element}"

                    total_mass += atomic_masses[element] * count

                element = char
                number = ""

            elif char.islower():

                element += char

            elif char.isdigit():

                number += char


        if element:

            count = int(number) if number else 1

            if element not in atomic_masses:
                return f"Unknown element: {element}"

            total_mass += atomic_masses[element] * count


        self.history.append(
            f"Molar Mass: {formula} = {total_mass:.3f} g/mol"
        )

        return round(total_mass, 3)