from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height, title):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell):
        cell.draw(self.__canvas)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Line:
    def __init__(self, start_point, end_point):
        self.__start = start_point
        self.__end = end_point

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__start.get_x(),
            self.__start.get_y(),
            self.__end.get_x(),
            self.__end.get_y(),
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(self, walls, x1, x2, y1, y2, color, win):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__wall_color = color
        self.__win = win

        self.__walls = {
            "top": {
                "visible": walls[0],
                "line": Line(Point(x1, y1), Point(x2, y1))
            },
            "right": {
                "visible": walls[1],
                "line": Line(Point(x2, y1), Point(x2, y2))
            },
            "bottom": {
                "visible": walls[2],
                "line": Line(Point(x1, y2), Point(x2, y2))
            },
            "left": {
                "visible": walls[3],
                "line": Line(Point(x1, y1), Point(x1, y2))
            }   
        }

    def draw(self, canvas):
        if self.__walls["top"]["visible"]:
            self.__walls["top"]["line"].draw(canvas, self.__wall_color)

        if self.__walls["right"]["visible"]:
            self.__walls["right"]["line"].draw(canvas, self.__wall_color)

        if self.__walls["bottom"]["visible"]:
            self.__walls["bottom"]["line"].draw(canvas, self.__wall_color)

        if self.__walls["left"]["visible"]:
            self.__walls["left"]["line"].draw(canvas, self.__wall_color)

