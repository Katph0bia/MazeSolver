from graphics import Window
from cell_base import Cell

def main():
    win = Window(800,600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    t = Cell(win)
    t.has_right_wall = False
    t.draw(125, 125, 200, 200)

    j = Cell(win)
    j.has_bottom_wall = False
    j.draw(225, 225, 250, 250)

    h = Cell(win)
    h.has_top_wall = False
    h.draw(300, 300, 500, 500)

    f = Cell(win)
    f.has_top_wall = False
    f.has_bottom_wall = False
    f.draw(75, 75, 300, 300)

    win.wait_for_close()


main()