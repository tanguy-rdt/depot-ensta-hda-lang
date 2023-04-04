from matplotlib import pyplot as plt
import numpy as np

class DesignerTools:
    def setup_design(ax):
        ax.set_aspect('equal')
        
    def draw_rectangle(ax, lenght, width, x=0, y=0, label=""):
        ax.plot([x, x+lenght], [y, y], 'k')
        ax.plot([x, x+lenght], [y+width, y+width], 'k')
        ax.plot([x, x], [y, y+width], 'k')
        ax.plot([x+lenght, x+lenght], [y, y+width], 'k')
        ax.text(x+(lenght/2), y+(width/2), label, horizontalalignment='center', verticalalignment='center')


class HouseDesigner:
    def __init__(self) -> None:
        self.ax = None
        self.fig = None
        
    def design(self, ast):
        ast.accept(self)
        plt.show()
            
    def visit_house(self, house):
        house.floor.accept(self)
            
    def visit_floor(self, floor):
        self.fig, self.ax = plt.subplots()
        DesignerTools.setup_design(self.ax)
        DesignerTools.draw_rectangle(self.ax, int(floor.lenght.value), int(floor.width.value))
        for room in floor.room:
            room.accept(self)      
        
    def visit_room(self, room):
        room.room.accept(self)
    
    def visit_kitchen(self, kitchen):
        DesignerTools.draw_rectangle(self.ax, int(kitchen.lenght.value), int(kitchen.width.value), label="kitchen")