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
