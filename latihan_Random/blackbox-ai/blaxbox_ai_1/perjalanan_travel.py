class Travel:
    def __init__(self, destination, duration, budget):
        self.destination = destination
        self.duration = duration
        self.budget = budget

    def get_info(self):
        return f"Destination: {self.destination}, Duration: {self.duration} days, Budget: {self.budget}"

class Country(Travel):
    def __init__(self, destination, duration, budget, languange, currency):
        super().__init__(destination, duration, budget)
        self.languange = languange
        self.currency = currency

    def get_county_info(self):
        travel_info = self.get_info()
        return f"{travel_info}, Languange: {self.languange}, Currency: {self.currency}"


# contoh penggunaan
if __name__ == "__main__":
    # membuat objek dari kelas country
    country = Country("Indonesia", 5, 1000000, "Bahasa Indonesia", "Rupiah")
    print(country.get_county_info())