import json


# kela untuk merepresentasikan kepribadian anak
class Personality:
    def __init__(self, confidence, empathy, independence, sociability):
        self.confidence = confidence
        self.empathy = empathy
        self.independence = independence
        self.sociability = sociability

    def to_dict(self):
        return {
            "confidence": self.confidence,
            "empathy": self.empathy,
            "independence": self.independence,
            "sociability": self.sociability
        }


# kelas untuk menyimpandata anak

class Child:
    def __init__(self, name, age, personality):
        self.name = name
        self.age = age
        self.personality = personality

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "personality": self.personality.to_dict()
        }


class PersonalityManager:
    def __init__(self, data_file='personality_data.json'):
        self.data_file = data_file
        self.children_data = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                content = file.read().strip()
                self.children_data = json.loads(content) if content else []
        except (FileNotFoundError, json.JSONDecodeError):
            self.children_data = []

    def add_child(self, child):
        self.children_data.append(child.to_dict())
        self.save_data()

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.children_data, file, indent=4)

    def display_all_children(self):
        for child in self.children_data:
            print(child)

def get_user_input():
    print("======== Tambahkan Data Kepribadian Anak ========")
    name = input("Nama Anak:")
    age = int(input("Usia Anak: "))
    print("=====\nMasukan nilai kepribadian(1-10):")
    confidence = int(input(" Kepercayaan Diri:"))
    empathy = int(input(" Empati: "))
    independence = int(input(" Kemandirian: "))
    sociability = int(input(" Sosialitas: "))

    personality = Personality(confidence, empathy, independence, sociability)
    return Child(name, age, personality)

# conth penggunaan
if __name__ == "__main__":
    manager = PersonalityManager()

    while True:
        # tanyakan kepada pengguna apakah ingin menambah data
        add_data = input("Ingin menambahkan data anak ? (y/n): ").strip().lower()
        if add_data == 'y':
            child = get_user_input()
            manager.add_child(child)
            print("Data anak berhasil di tambahkan!")
        elif add_data == 'n':
            break
        else:
            print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")

 # Tampilkan semua data anak yang sudah tersimpan
    print("\nData Kepribadian Anak yang Tersimpan:")
    manager.display_all_children()