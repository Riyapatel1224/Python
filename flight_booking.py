class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)


Flight = Flight(3)

people = ["harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if Flight.add_passanger(person):
        print(f"added {person} to flight successfully.")
    else:
        print(f"no available seats for {person}")