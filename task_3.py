class Cell:

    def __init__(self, cells):
        self.cells = int(cells)

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return self.cells - other.cells
        else:
            return other.cells - self.cells

    def __mul__(self, other):
        return self.cells * other.cells

    def __floordiv__(self, other):
        try:
            return self.cells // other.cells
        except ZeroDivisionError:
            return 0

    def make_oder(self, cells_row):
        row = ''
        for i in range(self.cells // cells_row):
            row += '*' * cells_row + '\n'

        if self.cells % cells_row == 0:
            return row[:-1]
        else:
            return row + '*' * (self.cells % cells_row)


cell1 = Cell(20)
cell2 = Cell(15)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)

print(cell1.make_oder(5))
print()
print(cell2.make_oder(7))
