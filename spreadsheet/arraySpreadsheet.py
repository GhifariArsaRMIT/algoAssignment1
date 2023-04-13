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
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        mRow = max(lCells, key=lambda c: c.row).row
        mCol = max(lCells, key=lambda c: c.col).col


        self.spreadsheet = [[None] * (mCol + 1) for _ in range(mRow + 1)]
        for cell in lCells:
            self.update(cell.row, cell.col, cell.val)

    # TO BE IMPLEMENTED
    pass

    def appendRow(self) -> bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        col = self.colNum()
        self.spreadsheet.append([None] * col)

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def appendCol(self) -> bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        rows = self.rowNum()
        for row in self.spreadsheet:
            row.append(None)
        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex < -1 or rowIndex >= self.rowNum():
            return False
        self.spreadsheet.insert(rowIndex + 1, [None] * self.colNum())
        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        if colIndex < -1 or colIndex >= self.colNum():
            return False
        for row in self.spreadsheet:
            row.insert(colIndex + 1, None)
        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        if rowIndex < 0 or rowIndex >= self.rowNum() or colIndex < 0 or colIndex >= self.colNum():
            return False
        self.spreadsheet[rowIndex][colIndex] = value
        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def rowNum(self) -> int:
        """
        @return Number of rows the spreadsheet has.
        """
        return len(self.spreadsheet)
        pass

    def colNum(self) -> int:
        """
        @return Number of column the spreadsheet has.
        """
        if len(self.spreadsheet) == 0:
            return 0
        else:
            return len(self.spreadsheet[0])
        pass

    def find(self, value: float) -> list[(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
            """
        cellVal = []
        for rowIndex,row in enumerate(self.spreadsheet):
            for colIndex,cell in enumerate(row):
                if cell == value:
                    cellVal.append((rowIndex,colIndex))
                    
        # TO BE IMPLEMENTED
        return cellVal
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []

    def entries(self) -> list[Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        cellVal = []
        for rowIndex,row in enumerate(self.spreadsheet):
            for colIndex,cell in enumerate(row):
                if cell != None:
                    cellVal.append(Cell(rowIndex,colIndex,cell))
        # TO BE IMPLEMENTED
        return cellVal
        pass

        # TO BE IMPLEMENTED
        return []
