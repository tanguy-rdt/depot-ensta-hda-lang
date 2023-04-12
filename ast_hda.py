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


class Kitchen:
    def __init__(self, lenght, width, name):
        self.lenght = lenght
        self.width = width
        self.name = name

    def accept(self, visitor):
        visitor.visit_kitchen(self)


class Lounge:
    def __init__(self, lenght, width, name):
        self.lenght = lenght
        self.width = width
        self.name = name

    def accept(self, visitor):
        visitor.visit_lounge(self)


class Bedroom:
    def __init__(self, lenght, width, name):
        self.lenght = lenght
        self.width = width
        self.name = name

    def accept(self, visitor):
        visitor.visit_bedroom(self)


class Bathroom:
    def __init__(self, lenght, width, name):
        self.lenght = lenght
        self.width = width
        self.name = name

    def accept(self, visitor):
        visitor.visit_bathroom(self)
