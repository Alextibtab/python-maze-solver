from maze_solver.graphics import Window, Point, Line, Cell
from maze_solver.maze import Maze


if __name__ == "__main__":
    # a = Point(10, 10)
    # b = Point(100, 100)
    # line = Line(a, b)

    # cell_a = Cell([True, True, True, True], 10, 20, 10, 20, "black", False)
    # cell_b = Cell([True, False, True, True], 30, 40, 10, 20, "red", False)
    # cell_c = Cell([True, True, False, True], 50, 60, 10, 20, "blue", False)
    # cell_d = Cell([True, True, True, False], 70, 80, 10, 20, "green", False)

    # win.draw_line(line, "black")
    # win.draw_cell(cell_a)
    # win.draw_cell(cell_b)
    # win.draw_cell(cell_c)
    # win.draw_cell(cell_d)

    # win.draw_move(cell_a, cell_b)
    # win.draw_move(cell_b, cell_c)
    # win.draw_move(cell_c, cell_d)
    win = Window(1920, 1080, "Maze Solver!")
    maze = Maze(win, 3, 3, 25, 25, 30, 30, False)


    win.wait_for_close()
