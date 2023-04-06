from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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
        self.fig = []
        self.floor = []
        self.room = []
        
    def design(self, ast):
        ast.accept(self)
        plt.show()
        
        pdf = PdfPages("house_design.pdf")
        for fig in self.fig:
            pdf.savefig(fig)
        pdf.close()
            
            
    def visit_house(self, house):
        for floor in house.floor:
            floor.accept(self)
            
    def visit_floor(self, floor):
        fig, self.ax = plt.subplots()
        self.fig.append(fig)
        DesignerTools.setup_design(self.ax)
        DesignerTools.draw_rectangle(self.ax, int(floor.lenght.value), int(floor.width.value))
        for room in floor.room:
            room.accept(self)  
    
    def visit_kitchen(self, kitchen):
        self.room.append(kitchen)
        DesignerTools.draw_rectangle(self.ax, int(kitchen.lenght.value), int(kitchen.width.value), label=kitchen.name.value)
        
    def visit_lounge(self, lounge):
        self.room.append(lounge)
        DesignerTools.draw_rectangle(self.ax, int(lounge.lenght.value), int(lounge.width.value), label=lounge.name.value)
        
    def visit_bedroom(self, bedroom):
        self.room.append(bedroom)
        DesignerTools.draw_rectangle(self.ax, int(bedroom.lenght.value), int(bedroom.width.value), label=bedroom.name.value)
        
    def visit_bathroom(self, bathroom):
        self.room.append(bathroom)
        DesignerTools.draw_rectangle(self.ax, int(bathroom.lenght.value), int(bathroom.width.value), label=bathroom.name.value)