class House:
    def __init__(self, declarations, statements):
        self.declarations = declarations
        self.statements = statements

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
