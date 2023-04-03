from matplotlib import pyplot as plt

class DesignerTools:
    def draw_rectangle(ax, lenght, width, x=0, y=0):
        ax.plot([x, lenght], [y, y], 'k')
        ax.plot([x, lenght], [width, width], 'k')
        ax.plot([x, x], [y, width], 'k')
        ax.plot([lenght, lenght], [y, width], 'k')

class HouseDesigner:
    def __init__(self) -> None:
        self.ax = None
        
    def design(self, ast):
        ast.accept(self)
        plt.show()
            
    def visit_house(self, house):
        house.floor.accept(self)
            
    def visit_floor(self, floor):
        fig, self.ax = plt.subplots()
        DesignerTools.draw_rectangle(self.ax, 50, 100)
        floor.room.accept(self)
        
    def visit_room(self, room):
        pass
    
    def visit_kitchen(self, kitchen):
        DesignerTools.draw_rectangle(self.ax, 30, 20)