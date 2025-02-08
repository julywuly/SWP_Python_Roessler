class Room:
    def __init__(self, name, room_type):
        self.name = name
        self.room_type = room_type
        self.available = True

    def book(self):
        if self.available:
            self.available = False
            return f"Room {self.name} has been booked."
        return f"Room {self.name} is already occupied."

    def cancel(self):
        if not self.available:
            self.available = True
            return f"Booking for Room {self.name} has been canceled."
        return f"Room {self.name} was not booked."

    def __str__(self):
        status = "available" if self.available else "occupied"
        return f"Room {self.name} ({self.room_type}) - {status}"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, name):
        for room in self.rooms:
            if room.name == name:
                return room.book()
        return "Room not found."

    def cancel_room(self, name):
        for room in self.rooms:
            if room.name == name:
                return room.cancel()
        return "Room not found."

    def count_available_rooms(self):
        return sum(1 for room in self.rooms if room.available)

    def __str__(self):
        return f"Hotel {self.name} with {len(self.rooms)} rooms. Available rooms: {self.count_available_rooms()}"


# Example usage:
hotel = Hotel("Grand Plaza")
hotel.add_room(Room("101", "Single"))
hotel.add_room(Room("102", "Double"))
hotel.add_room(Room("103", "Single"))

print(hotel)
print(hotel.book_room("101"))
print(hotel.book_room("102"))
print(hotel)
print(hotel.cancel_room("101"))
print(hotel)
