import numpy
import math as m

class Cell:
    def __init__(self, name, x, y):
        self.name=name
        self.x=x
        self.y=y

    def __str__(self):
        return("hello I'm an instance of cell")
    
    def cell_distance(self,othercell):
        distance = m.sqrt((self.x - othercell.x)**2 + (self.y - othercell.y)**2)
        return distance


cell1=Cell("cell 1",10,20)
cell2=Cell("cell 2", 90, 100)


print (cell1)

print(cell1.name)

print(cell1.cell_distance(cell2))
