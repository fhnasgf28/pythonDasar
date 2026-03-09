class TravelNotes:
    def __init__(self):
        self.entries = []

    def add_entry(self, date, place, note):
        self.entries.append({"date": date, "place": place, "note": note})

    def show_entries(self):
        if not self.entries:
            print("Tidak ada catatan perjalanan.")
            return

        for entry in self.entries:
            print(f"Tanggal: {entry['date']}")
            print(f"Tempat: {entry['place']}")
            print(f"Catatan: {entry['note']}")
            print()
