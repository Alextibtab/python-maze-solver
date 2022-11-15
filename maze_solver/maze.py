import time

from graphics import Window, Cell


class Maze:
    def __init__(
        self,
        window,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.__window = window
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self._create_cells()

    def _create_cells(self):
        self.__cells = [
            [
                Cell(
                    [True] * 4,
                    row_offset + column_offset,
                    row_offset + column_offset + self.__cell_size_x,
                    row_offset + column_offset,
                    row_offset + column_offset + self.__cell_size_y,
                )
                for row_offset in range(
                    self.__x1, self.__num_rows * self.__cell_size_y, self.__cell_size_y
                )
            ]
            for column_offset in range(
                self.__y1, self.__num_cols * self.__cell_size_x, self.__cell_size_x
            )
        ]
        for cell in self.__cells:
            self.__window.draw_cell(cell)
            self._animate()

    def _animate(self):
        self.__window.redraw()
        time.sleep(0.05)
