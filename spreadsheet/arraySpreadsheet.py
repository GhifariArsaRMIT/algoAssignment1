from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet
import time


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):
    
    global_time = 0     

    def __init__(self):
        # print("Please enter a list of tuples of form (row,column,value) seperate dby commas: ")
        # TO BE IMPLEMENTED
        pass

    def buildSpreadsheet(self, lCells: list[Cell]):
        start_time = time.time()
        mRow = max(lCells, key=lambda c: c.row).row
        mCol = max(lCells, key=lambda c: c.col).col


        self.spreadsheet = [[None] * (mCol + 1) for _ in range(mRow + 1)]
        for cell in lCells:
            self.update(cell.row, cell.col, cell.val)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for building:", running_time, "seconds")

        pass

    def appendRow(self) -> bool:
        start_time = time.time()
        col = self.colNum()
        self.spreadsheet.append([None] * col)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for AppendingRow:", running_time, "seconds")
        
        return True

    def appendCol(self) -> bool:
        
        start_time = time.time()
        
        rows = self.rowNum()
        for row in self.spreadsheet:
            row.append(None)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for AppendCol:", running_time, "seconds")
        
        return True

    def insertRow(self, rowIndex: int) -> bool:
        start_time = time.time()
        
        if rowIndex < -1 or rowIndex >= self.rowNum():
            return False
        self.spreadsheet.insert(rowIndex + 1, [None] * self.colNum())
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for InsertRow:", running_time, "seconds")
        
        return True

    def insertCol(self, colIndex: int) -> bool:
        start_time = time.time()
        
        var = True
        if colIndex < -1 or colIndex >= self.colNum():
            var = False
        for row in self.spreadsheet:
            row.insert(colIndex + 1, None)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for InsertCol:", running_time, "seconds")
        
        return var

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        start_time = time.time()
        
        var = True
        if rowIndex < 0 or rowIndex >= self.rowNum() or colIndex < 0 or colIndex >= self.colNum():
            var =  False
        if var == True:
            self.spreadsheet[rowIndex][colIndex] = value
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for Update:", running_time, "seconds")
        
        return var

    def rowNum(self) -> int:
        start_time = time.time()
        var = len(self.spreadsheet)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for RowNum:", running_time, "seconds")
        
        return var
        pass

    def colNum(self) -> int:
        start_time = time.time()
        
        var = 0
        if len(self.spreadsheet) == 0:
            var = 0
        else:
            var = len(self.spreadsheet[0])
            
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for ColNum:", running_time, "seconds")
        
        return var
        pass

    def find(self, value: float) -> list[(int, int)]:
        start_time = time.time()
        
        cellVal = []
        for rowIndex,row in enumerate(self.spreadsheet):
            for colIndex,cell in enumerate(row):
                if cell == value:
                    cellVal.append((rowIndex,colIndex))
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for Find:", running_time, "seconds")
        
        # TO BE IMPLEMENTED
        return cellVal

    def entries(self) -> list[Cell]:
        start_time = time.time()
        cellVal = []
        for rowIndex,row in enumerate(self.spreadsheet):
            for colIndex,cell in enumerate(row):
                if cell != None:
                    cellVal.append(Cell(rowIndex,colIndex,cell))
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for Entries:", running_time, "seconds")
        
        # TO BE IMPLEMENTED
        return cellVal
