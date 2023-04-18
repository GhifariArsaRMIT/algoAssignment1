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
        # TO BE IMPLEMENTED
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
            #print(row_ptrs)
            #print(cell.row, cell.col, cell.val)

        for i in range(1, mRow + 2):
            row_ptrs[i] += row_ptrs[i - 1]
        #print(row_ptrs)
        #print(col_indices)
        #print(values)
        #print(row_ptrs)
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
        #print("row to be inserted at ", rowIndex)
        #print("original rows: ", self.sum)
        start_time = time.time()
        val = False
        if rowIndex > -1 and rowIndex < self.rowNum(): 
            self.sum.insert(rowIndex, self.sum[rowIndex - 1])
            #print("modified rows: ", self.sum)
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

        #print("original column numbers: ", self.colar)
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

        #print("columnarray assigned: ", self.colar)
        #print("original values array: ", self.values)
        self.cells = sorted(self.cells, key=lambda c: (c.row, c.col))
        #print("row to be updated: ", rowIndex, "col to be updated: ", colIndex)
        for i in range(len(self.sum) - 1):
            for j in range(len(columnarray) - 1):
                if i == rowIndex and columnarray[j] == colIndex:
                    self.values[j] = value
                    #print(i,columnarray[j],self.values[j])
                    val =  True
                elif colIndex not in columnarray and colIndex < self.numCol:
                    #if the colindex is not denote din the column array we must add a value to the column array such that it will
                    #at the moment this returns false because although colum  10 exists it is not inside of the columnarray as the values represented are only ones which correlate to a value
                    #if a value does not exists in these positions yet they will not appear thus we must create these positions
                    #UPDATE A POSITION TO HOLD A VALUE HERE
                    pos = self.sum[rowIndex]
                    #self.colar.append(colIndex)
                    self.colar.insert(pos, colIndex)
                    #print("new column array: ", self.colar)
                    #self.values.append(value)
                    self.values.insert(pos, value)
                    #print("new values array: ", self.values)
                    #increment the row pointer at the new position
                    #print("old ptr array: ", self.sum) 
                    for x in range(rowIndex, len(self.sum)):
                        self.sum[x] += 1  
                    #print("new ptr array: ", self.sum)       
                    ##self.sum.pop(len(self.sum) - 1)
                    self.cells = sorted(self.cells, key=lambda c: (c.row, c.col))
                    val =  True
                    break
                
            # Record the end time
            end_time = time.time()
            # Calculate the running time
            running_time = end_time - start_time
            self.global_time += running_time
            
            return val
  
    
        # TO BE IMPLEMENTEDs


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
                    #return cellval
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
        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE




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
