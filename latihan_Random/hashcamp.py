from collections import defaultdict

class HashmicroCamp:
    def __init__(self):
        self.schedule = defaultdict(list)

    def add_activity(self, date, name, time, pic, participants):
        self.schedule[date].append({
            'name': name,
            'time': time,
            'pic': pic,
            'participants': participants
        })

    def view_schedule(self):
        for date, activities in self.schedule.items():
            print(f"\n📅 {date}")
            for act in activities:
                print(f"  - {act['time']} | {act['name']} (PIC: {act['pic']})")

    def search_activity(self, keyword):
        print(f"\n🔍 Search results for '{keyword}':")
        for date, activities in self.schedule.items():
            for act in activities:
                if keyword.lower() in act['name'].lower():
                    print(f"  - {act['name']} on {date} at {act['time']} (PIC: {act['pic']})")

    def show_statistics(self):
        pic_counter = defaultdict(int)
        total = 0
        for activities in self.schedule.values():
            for act in activities:
                pic_counter[act['pic']] += 1
                total += 1
        print(f"\n📊 Total Activities: {total}")
        if pic_counter:
            top_pic = max(pic_counter, key=pic_counter.get)
            print(f"🏅 Top PIC: {top_pic} with {pic_counter[top_pic]} activities")

# Contoh penggunaan
camp = HashmicroCamp()
camp.add_activity('2025-06-01', 'Ice Breaking', '08:00', 'Dina', ['Ari', 'Budi'])
camp.add_activity('2025-06-01', 'Workshop Python', '10:00', 'Eka', ['Citra', 'Budi'])
camp.view_schedule()
camp.search_activity('python')
camp.show_statistics()
