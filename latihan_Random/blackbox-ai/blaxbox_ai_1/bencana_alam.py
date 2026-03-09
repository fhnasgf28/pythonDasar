class Donor:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.amount_donated = 0

    def donate(self, amount):
        self.amount_donated += amount
        print(f"{self.name} has donated ${amount}. Total donations: ${self.amount_donated}")


class Campaign:
    def __init__(self, title, description, goal_amount):
        self.title = title
        self.description = description
        self.goal_amount = goal_amount
        self.donors = []

    def add_donor(self, donor, amount):
        donor.donate(amount)
        self.donors.append(donor)

    def total_donations(self):
        return sum(donor.amount_donated for donor in self.donors)

    def is_goal_reached(self):
        return self.total_donations() >= self.goal_amount


class Fundraiser:
    def __init__(self):
        self.campaigns = []

    def create_campaign(self, title, description, goal_amount):
        campaign = Campaign(title, description, goal_amount)
        self.campaigns.append(campaign)
        print(f"Campaign '{title}' created with goal of ${goal_amount}.")

    def show_campaigns(self):
        for campaign in self.campaigns:
            print(f"Title: {campaign.title}, Description: {campaign.description}, Goal: ${campaign.goal_amount}, Total Donations: ${campaign.total_donations()}")


# Contoh penggunaan
if __name__ == "__main__":
    fundraiser = Fundraiser()

    # Membuat kampanye
    fundraiser.create_campaign("Bantuan Bencana Alam", "Penggalangan dana untuk korban bencana alam.", 10000)

    # Menambahkan donatur
    donor1 = Donor("Alice", "alice@example.com")
    donor2 = Donor("Bob", "bob@example.com")

    # Menambahkan donasi ke kampanye
    campaign = fundraiser.campaigns[0]
    campaign.add_donor(donor1, 500)
    campaign.add_donor(donor2, 300)

    # Menampilkan semua kampanye
    fundraiser.show_campaigns()

    # Memeriksa apakah tujuan tercapai
    if campaign.is_goal_reached():
        print("Goal reached!")
    else:
        print("Goal not reached yet.")