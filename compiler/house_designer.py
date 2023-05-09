from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
    def __init__(self, mode=None) -> None:
        self.mode = mode
        
        plt.close('all')
        if self.mode == 'i':
            plt.ion()
        
        self.ax = None
        self.fig = []
        self.floor = []
        self.rooms = []
        
    def design(self, ast):
        ast.accept(self)
        
        if self.mode == 'i':
            plt.draw()
        else:
            plt.show()
             
            pdf = PdfPages("house_design.pdf")
            for fig in self.fig:
                pdf.savefig(fig)
                fig.savefig(".img/fig" + str(self.fig.index(fig)) + ".png") 
            pdf.close()
            
            
    def visit_house(self, house):
        for floor in house.floor:
            floor.accept(self)
            
    def visit_floor(self, floor):
        fig, self.ax = plt.subplots()
        self.fig.append(fig)
        DesignerTools.setup_design(self.ax)
        DesignerTools.draw_rectangle(self.ax, 
                                     int(floor.lenght.value.split('m')[0]), 
                                     int(floor.width.value.split('m')[0]))
        for room in floor.room:
            room.accept(self)  

    def visit_room(self, room):
        x = 0
        y = 0
        if room.position:
            for r in self.rooms:
                if r["name"] == room.position[1].value:
                    if room.position[0].tag == "RIGHT":
                        x = r["x"]+r["lenght"]
                        y = r["y"]
                    if room.position[0].tag == "LEFT":
                        x = r["x"]-int(room.lenght.value.split('m')[0])
                        y = r["y"]
                    if room.position[0].tag == "TOP":
                        x = r["x"]
                        y = r["y"]+r["width"]
                    if room.position[0].tag == "BOTTOM":
                        x = r["x"]-int(room.width.value.split('m')[0])
                        y = r["y"]

        this_room = {"name": room.name.value, 
                     "lenght": int(room.lenght.value.split('m')[0]),
                     "width": int(room.width.value.split('m')[0]), 
                     "x": x,
                     "y": y}

        self.rooms.append(this_room)

        DesignerTools.draw_rectangle(self.ax, 
                                     this_room["lenght"], 
                                     this_room["width"], 
                                     x=this_room["x"],
                                     y=this_room["y"],
                                     label=room.name.value)


class HouseDesigner3D:
    def __init__(self):
        plt.close('all')
        
        self.ax = None
        self.fig = None
        self.axes = [0, 0, 0]
        self.floor = []
      
        
    def design(self, ast):
        ast.accept(self)
        self.build_house()
    
    def visit_house(self, house):
        for floor in house.floor:
            floor.accept(self)
            
    def visit_floor(self, floor):
        lenght = int(floor.lenght.value.split('m')[0])
        width = int(floor.width.value.split('m')[0])

        if self.axes[0] < lenght:
            self.axes[0] = lenght
        if self.axes[1] < width:
            self.axes[1] = width
        self.axes[2] = len(self.floor)*3+3

        self.floor.append([lenght, width, 3])

    def build_house(self):
        data_floor = 0

        for n_floor, floor in enumerate(self.floor):
            data = np.zeros(self.axes, dtype=np.bool_)
            data[0:floor[0], 0:floor[1], n_floor*3:(n_floor*3)+3] = True

            data_floor |= data

        color = np.empty(self.axes + [4], dtype=np.float32)
        color[:] = [1, 0.992, 0.816, 1] 

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.voxels(data_floor, facecolors=color)
        plt.show()

