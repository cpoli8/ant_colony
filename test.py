from tkinter import *
from grid import *
from constant import *
from drawing_manager import *
from ant import *
from random import randint
from time import sleep

fenetre = Tk()
fenetre.geometry("1200x800")
# fenetre.resizable(0, 0)

DM = Drawer(fenetre)

test_grid = Grid()

test_grid.set_interaction_points()

test_grid.print_grid()

for i in range(20):
    Ant(randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1), DM.canvas)

DM.draw_grid(test_grid.grid)

for i in range(100):
    for ant in Ant.List:
        ant.update_position()
        DM.canvas.update()
    sleep(1)

fenetre.mainloop()
# while True:

# grid.update_odour()
# ant.update_position()
# grid.check_interaction_point()
