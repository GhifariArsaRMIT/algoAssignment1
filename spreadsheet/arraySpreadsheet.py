from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # print("Please enter a list of tuples of form (row,column,value) seperate dby commas: ")
        # TO BE IMPLEMENTED
        pass

    def buildSpreadsheet(self, lCells: list[Cell]):
        mRow = max(lCells, key=lambda c: c.row).row
        mCol = max(lCells, key=lambda c: c.col).col


        self.spreadsheet = [[None] * (mCol + 1) for _ in range(mRow + 1)]
        for cell in lCells:
            self.update(cell.row, cell.col, cell.val)

    # TO BE IMPLEMENTED
    pass

    def appendRow(self) -> bool:
        col = self.colNum()
        self.spreadsheet.append([None] * col)
        return True

    def appendCol(self) -> bool:
        rows = self.rowNum()
        for row in self.spreadsheet:
            row.append(None)
        return True

    def insertRow(self, rowIndex: int) -> bool:
        if rowIndex < -1 or rowIndex >= self.rowNum():
            return False
        self.spreadsheet.insert(rowIndex + 1, [None] * self.colNum())
        return True

    def insertCol(self, colIndex: int) -> bool:
        if colIndex < -1 or colIndex >= self.colNum():
            return False
        for row in self.spreadsheet:
            row.insert(colIndex + 1, None)
        return True

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        if rowIndex < 0 or rowIndex >= self.rowNum() or colIndex < 0 or colIndex >= self.colNum():
            return False
        self.spreadsheet[rowIndex][colIndex] = value
        return True

    def rowNum(self) -> int:
        return len(self.spreadsheet)
        pass

    def colNum(self) -> int:
        if len(self.spreadsheet) == 0:
            return 0
        else:
            return len(self.spreadsheet[0])
        pass

    def find(self, value: float) -> list[(int, int)]:
        cellVal = []
        for rowIndex,row in enumerate(self.spreadsheet):
            for colIndex,cell in enumerate(row):
                if cell == value:
                    cellVal.append((rowIndex,colIndex))
                    
        # TO BE IMPLEMENTED
        return cellVal

    def entries(self) -> list[Cell]:
        cellVal = []
        for rowIndex,row in enumerate(self.spreadsheet):
            for colIndex,cell in enumerate(row):
                if cell != None:
                    cellVal.append(Cell(rowIndex,colIndex,cell))
        # TO BE IMPLEMENTED
        return cellVal
