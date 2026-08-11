class UnitConverter:

    # =========================
    # Temperature
    # =========================

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def kelvin_to_celsius(self, kelvin):
        if kelvin < 0:
            return "Error: Temperature in Kelvin cannot be below absolute zero."

        return kelvin - 273.15

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    # =========================
    # Mass
    # =========================

    def kg_to_gram(self, kg):
        return kg * 1000

    def gram_to_kg(self, gram):
        return gram / 1000

    # =========================
    # Length
    # =========================

    def meter_to_cm(self, meter):
        return meter * 100

    def cm_to_meter(self, cm):
        return cm / 100

    def meter_to_mm(self, meter):
        return meter * 1000

    def mm_to_meter(self, mm):
        return mm / 1000

    # =========================
    # Pressure
    # =========================

    def pa_to_kpa(self, pa):
        return pa / 1000

    def kpa_to_pa(self, kpa):
        return kpa * 1000

    def pa_to_bar(self, pa):
        return pa / 100000

    def bar_to_pa(self, bar):
        return bar * 100000

    def pa_to_atm(self, pa):
        return pa / 101325

    def atm_to_pa(self, atm):
        return atm * 101325

    # =========================
    # Volume
    # =========================

    def cubic_meter_to_liter(self, cubic_meter):
        return cubic_meter * 1000

    def liter_to_cubic_meter(self, liter):
        return liter / 1000

    def liter_to_milliliter(self, liter):
        return liter * 1000

    def milliliter_to_liter(self, milliliter):
        return milliliter / 1000

    # =========================
    # Energy
    # =========================

    def joule_to_kilojoule(self, joule):
        return joule / 1000

    def kilojoule_to_joule(self, kilojoule):
        return kilojoule * 1000

    # =========================
    # Power
    # =========================

    def watt_to_kilowatt(self, watt):
        return watt / 1000

    def kilowatt_to_watt(self, kilowatt):
        return kilowatt * 1000

    # =========================
    # Time
    # =========================

    def second_to_minute(self, second):
        return second / 60

    def minute_to_second(self, minute):
        return minute * 60

    def minute_to_hour(self, minute):
        return minute / 60

    def hour_to_minute(self, hour):
        return hour * 60