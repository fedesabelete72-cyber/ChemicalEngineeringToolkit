class UnitConverter:

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def kg_to_gram(self, kg):
        return kg * 1000

    def gram_to_kg(self, gram):
        return gram / 1000

    def meter_to_cm(self, meter):
        return meter * 100

    def cm_to_meter(self, cm):
        return cm / 100