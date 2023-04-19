from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
import time

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------




class CSRSpreadsheet(BaseSpreadsheet):
    
    global_time = 0

    def __init__(self):
        pass


    def buildSpreadsheet(self, lCells: list[Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        start_time = time.time()
        
        mRow = max(lCells, key=lambda c: c.row).row
        mCol = max(lCells, key=lambda c: c.col).col
        lCells = sorted(lCells, key=lambda c: (c.row, c.col))
        self.cells = lCells
        values = []
        col_indices = []
        row_ptrs = [0] * (mRow + 2)
        row_ptrs[0] = 0
        for cell in lCells:
            values.append(cell.val)
            col_indices.append(cell.col)
            row_ptrs[cell.row] += 1

        for i in range(1, mRow + 2):
            row_ptrs[i] += row_ptrs[i - 1]
        self.numCol = mCol + 2
        self.sum = row_ptrs
        self.colar = col_indices
        self.values = values
        self.spreadsheet = (values, col_indices, row_ptrs)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time



    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """ 
        start_time = time.time()
        self.sum.append(self.sum[len(self.sum) - 1])
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time

        return True
        pass


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        start_time = time.time()
        
        self.numCol + 1        
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time

        return True
        pass


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        start_time = time.time()
        val = False
        if rowIndex > -1 and rowIndex < self.rowNum(): 
            self.sum.insert(rowIndex, self.sum[rowIndex - 1])
            val = True
        else:
            val = False
            
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time

        
        return val

    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        start_time = time.time()
        colValues = self.colar
        val = True
        columnLength = self.colNum()

        if colIndex > -1 and colIndex < columnLength:
            self.numCol = columnLength + 1
            for i in range(len(colValues)):
                if colValues[i] > colIndex:
                    self.colar[i] = colValues[i] + 1
            val = True
        else:
            val = False
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time

        
        return val

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        #print("test column array: ", self.colar)

        start_time = time.time()
        val = True
        columnarray = self.colar

        if colIndex > self.numCol - 1 or rowIndex > len(self.sum) or colIndex < 0 or rowIndex < 0:
            return False
        self.cells = sorted(self.cells, key=lambda c: (c.row, c.col))
        for i in range(len(self.sum) - 1):
            for j in range(len(columnarray) - 1):
                if i == rowIndex and columnarray[j] == colIndex:
                    self.values[j] = value
                    val =  True
                elif colIndex not in columnarray and colIndex < self.numCol:
                    pos = self.sum[rowIndex]
                    self.colar.insert(pos, colIndex)
                    self.values.insert(pos, value)
                    for x in range(rowIndex, len(self.sum)):
                        self.sum[x] += 1  
                    self.cells = sorted(self.cells, key=lambda c: (c.row, c.col))
                    val =  True
                    break
                
            # Record the end time
            end_time = time.time()
            # Calculate the running time
            running_time = end_time - start_time
            self.global_time += running_time
            
            return val

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        start_time = time.time()
        
        val = len(self.sum) - 1
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time

        
        return val
        # TO BE IMPLEMENTED

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        start_time = time.time()
        
        val = 0
        if len(self.sum) - 1 == 0:
            val = 0
        else:
            val =  self.numCol
            
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time

        
        return val

    def find(self, value: float) -> list[(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        start_time = time.time()
        cellval = []

        ptrIndex = 0
        valueIndex = 0
        prevptr = 0
        while ptrIndex < len(self.sum) and valueIndex < len(self.values):
            currptr = self.sum[ptrIndex]
            rowIndex = ptrIndex
            ptrCheck = prevptr
            while ptrCheck < currptr:
                cellValue = self.values[valueIndex]
                colIndex = self.colar[valueIndex]
                if value == cellValue:
                    cellval.append((rowIndex,colIndex))
                ptrCheck += 1
                valueIndex += 1
            prevptr = currptr
            ptrIndex += 1

        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time

        
        return cellval

    def entries(self) -> list[Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        start_time = time.time()
        cellval = []
        rowValueIndexDup = []
        rowValueIndex = []

        for i in range(len(self.sum)):
            if self.sum[i-1] != self.sum[i]: 
                rowValueIndexDup.append(i)
                    
        for x in rowValueIndexDup:
            if x not in rowValueIndex and x > 0:
                rowValueIndex.append(x)
        
        for y in range(len(rowValueIndex)):
            cell = Cell(rowValueIndex[y], self.colar[y], self.values[y])
            cellval.append((cell))
            
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time

        return cellval
