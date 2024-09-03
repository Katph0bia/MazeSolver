from graphics import Window, Point, Line

def main():
    win = Window(800,600)
    a_line = Line(Point(50,50), Point(400,400))
    win.draw_line(a_line, "black")
    win.wait_for_close()


main()