class House:
    def __init__(self, floor):
        self.floor = floor

    def accept(self, visitor):
        visitor.visit_house(self)

class Floor:
    def __init__(self, lenght, width, room):
        self.lenght = lenght
        self.width = width
        self.room = room

    def accept(self, visitor):
        visitor.visit_floor(self)

class Room:
    def __init__(self, room):
        self.room = room

    def accept(self, visitor):
        visitor.visit_room(self)

class Kitchen:
    def __init__(self, lenght, width, name):
        self.lenght = lenght
        self.width = width
        self.name = name

    def accept(self, visitor):
        visitor.visit_kitchen(self)