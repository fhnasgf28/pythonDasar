class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def release(self):
        self.is_booked = False

class Reservation:
    def __init__(self, customer_name, room, duration):
        self.customer_name = customer_name
        self.room = room
        self.duration = duration
        self.total_price = room.price_per_night * duration

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_available_room(self, room_type):
        for room in self.rooms:
            if room.room_type == room_type and not room.is_booked:
                return room
        return None

    def book_room(self, customer_name, room_type, duration):
        room = self.find_available_room(room_type)
        if room:
            room.book()
            reservation = Reservation(customer_name, room, duration)
            self.reservations.append(reservation)
            print(f"Room {room.room_number} has been reserved for {customer_name} for {duration} nights.")
            return reservation
        else:
            print(f"No available {room_type} room found.")
            return None

    def generate_report(self):
        for reservation in self.reservations:
            print(f"Customer: {reservation.customer_name}")
            print(f"Room: {reservation.room.room_number}")
            print(f"Duration: {reservation.duration} nights")
            print(f"Total Price: {reservation.total_price}")
            print()

# Contoh penggunaan
if __name__ == "__main__":
    hotel = Hotel("My Hotel")
    room1 = Room(101, "Single", 100)
    room2 = Room(102, "Double", 150)
    hotel.add_room(room1)
    hotel.add_room(room2)

    reservation1 = hotel.book_room("John Doe", "Single", 3)
    reservation2 = hotel.book_room("Jane Doe", "Double", 2)

    hotel.generate_report()