from constants import ATOMIC_MASSES


class Chemistry:

    def __init__(self):
        self.history = []

    def molar_mass(self, formula):

        if not formula or not formula.strip():
            raise ValueError("Chemical formula cannot be empty.")

        formula = formula.strip()

        composition = self._parse_formula(formula)

        total_mass = 0

        for element, count in composition.items():

            if element not in ATOMIC_MASSES:
                raise ValueError(
                    f"Unknown element: {element}"
                )

            total_mass += ATOMIC_MASSES[element] * count

        result = round(total_mass, 3)

        self.history.append(
            f"Molar Mass: {formula} = {result:.3f} g/mol"
        )

        return result

    def _parse_formula(self, formula):

        stack = [{}]

        i = 0

        while i < len(formula):

            char = formula[i]

            # --------------------------------
            # Opening parenthesis
            # --------------------------------
            if char == "(":

                stack.append({})

                i += 1

            # --------------------------------
            # Closing parenthesis
            # --------------------------------
            elif char == ")":

                if len(stack) == 1:
                    raise ValueError(
                        f"Unmatched ')' in formula: {formula}"
                    )

                group = stack.pop()

                i += 1

                # Read multiplier after ')'
                number = ""

                while (
                    i < len(formula)
                    and formula[i].isdigit()
                ):
                    number += formula[i]

                    i += 1

                multiplier = int(number) if number else 1

                # Apply multiplier to the group
                for element, count in group.items():

                    stack[-1][element] = (
                        stack[-1].get(element, 0)
                        + count * multiplier
                    )

            # --------------------------------
            # Element
            # --------------------------------
            elif char.isupper():

                element = char

                i += 1

                # Check for lowercase character
                if (
                    i < len(formula)
                    and formula[i].islower()
                ):
                    element += formula[i]

                    i += 1

                # Read subscript
                number = ""

                while (
                    i < len(formula)
                    and formula[i].isdigit()
                ):
                    number += formula[i]

                    i += 1

                count = int(number) if number else 1

                stack[-1][element] = (
                    stack[-1].get(element, 0)
                    + count
                )

            # --------------------------------
            # Invalid character
            # --------------------------------
            else:

                raise ValueError(
                    f"Invalid character '{char}' in formula."
                )

        # --------------------------------
        # Check for unmatched '('
        # --------------------------------
        if len(stack) != 1:

            raise ValueError(
                f"Unmatched '(' in formula: {formula}"
            )

        return stack[0]