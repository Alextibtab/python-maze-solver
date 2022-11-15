from maze_solver.graphics import Window, Point, Line


if __name__ == "__main__":
    a = Point(10, 10)
    b = Point(100, 100)
    line = Line(a, b)

    win = Window(800, 600, "Maze Solver!")
    win.draw_line(line, "black")
    win.wait_for_close()
