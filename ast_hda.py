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
    def __init__(self, things):
        self.things = things

    def accept(self, visitor):
        visitor.visit_room(self)

class Kitchen:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def accept(self, visitor):
        visitor.visit_kitchen(self)