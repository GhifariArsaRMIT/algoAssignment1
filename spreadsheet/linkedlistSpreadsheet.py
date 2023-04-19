from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
import math
import time
class Node:
    def __init__(self, value: Cell):
        self.m_value = value
        self.m_next = None
        self.m_prev = None

    def get_value(self):
        return self.m_value

    def get_next(self):
        return self.m_next
    
    def get_prev(self):
        return self.m_prev

    def set_value(self, value):
        self.m_value = value

    def set_next(self, next):
        self.m_next = next

    def set_prev(self, prev):
        self.m_prev = prev

class DoubleLinkedList:
    """ 
    Double linked list that implements interface MyList.

    """
    def __init__(self):
    
        self.m_head = None
        self.m_tail = None
        self.m_length = 0
   
    def add(self, new_value):
        new_node = Node(new_value)

        # If head is empty, then list is empty and head and tail references need to be initialised.
        if self.m_head is None:
            self.m_head = new_node
            self.m_tail = self.m_head
        else:
            new_node.set_prev(self.m_tail)
            self.m_tail.set_next(new_node)
            self.m_tail = new_node
            self.m_tail.set_next(None)

        self.m_length+=1

    def insert(self, index, new_value):
        if index >= self.m_length or index < 0:
            raise IndexError("Supplied index is invalid.")

        new_node = Node(new_value)

        # index == 0
        if not self.m_head:
            self.m_head = new_node
            self.m_tail = new_node
        
        # list is not empty
        else:
            # depending on where index is, we either go forward or backward in
            # list
            if index < math.ceil(self.m_length / 2):
                # go forward from head
                # if index = 0, we should replace mHead with newNode
                if index == 0:
                    new_node.set_next(self.m_head)
                    self.m_head.set_prev(new_node)
                    self.m_head = new_node
                else:
                    cur_node = self.m_head
                    for i in range(index): 
                        cur_node = cur_node.get_next()

                    # nextNode is the one being shift up
                    nextNode = cur_node.get_next()
                    nextNode.setPrev(new_node)
                    new_node.set_next(nextNode)
                    new_node.set_prev(cur_node)
                    cur_node.set_next(new_node)
            else:
                # go backward from tail
                cur_node = self.m_tail;
                for i in range(self.m_length-1, index, -1):
                    cur_node = cur_node.get_prev()

                prev_node = cur_node.get_prev()
                prev_node.set_next(new_node)
                new_node.set_prev(prev_node)
                new_node.set_next(cur_node)
                cur_node.set_prev(new_node)

        self.m_length += 1
        
    def searchRowColumn(self, row, col):
        cur_node = self.m_head
        for i in range(self.m_length):
            if cur_node.get_value().row == row and cur_node.get_value().col == col:
                return i
            cur_node = cur_node.get_next()
            
        return -1
        
    
    def max(self):
        if self.m_length == 0:
            raise ArithmeticError("Max is not defined for an empty list.")

        # traverse list, looking for the minimum valued element
        max_value = self.m_head.get_value();
        cur_node = self.m_head.get_next();

        while cur_node != None:
            if cur_node.get_value() > max_value:
                max_value = cur_node.get_value()
            cur_node = cur_node.get_next()

        return max_value
    
    def maxColumn(self):
        if self.m_length == 0:
            raise ArithmeticError("Max is not defined for an empty list.")

        # traverse list, looking for the minimum valued element
        max_value = self.m_head.get_value().col;
        cur_node = self.m_head.get_next();

        while cur_node != None:
            if cur_node.get_value().col > max_value:
                max_value = cur_node.get_value().col
            cur_node = cur_node.get_next()

        return max_value
    
    def maxRow(self):
        if self.m_length == 0:
            raise ArithmeticError("Max is not defined for an empty list.")

        # traverse list, looking for the minimum valued element
        max_value = self.m_head.get_value().row;
        cur_node = self.m_head.get_next();

        while cur_node != None:
            if cur_node.get_value().row > max_value:
                max_value = cur_node.get_value().row
            cur_node = cur_node.get_next()

        return max_value
    
    def printLL(self):
        currentNode = self.m_head
        while currentNode is not None:
            print("(",currentNode.get_value().row,currentNode.get_value().col,")", end="")
            if currentNode.m_value.val is not None:
                print("", currentNode.m_value.val)
            else:
                print("None")
            currentNode = currentNode.get_next()
    
    



# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):
    
    global_time = 0     

    def __init__(self):
        self.dll = DoubleLinkedList()


    def buildSpreadsheet(self, lCells: list[Cell]):
        
        # Record the start time
        start_time = time.time()
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        maxRow = max([cell.row for cell in lCells])
        maxCol = max([cell.col for cell in lCells])
        gang = {}
        
        for cells in lCells:
            gang[(cells.row, cells.col)] = cells.val
        
        for i in range(maxRow + 1):
            for j in range(maxCol + 1):
                cell = Cell(i,j,None)
                gangCell = (cell.row, cell.col)
                if gangCell in gang:
                    cell.val = gang[gangCell]
                self.dll.add(cell)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for building:", running_time, "seconds")

            
    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        start_time = time.time()
        maxCol = self.dll.maxColumn()
        newRow = self.dll.maxRow() + 1 
        
        for i in range(maxCol + 1):
            cell = Cell(row=newRow, col=i, val=None)
            self.dll.add(cell)
            
        end_time = time.time()
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for appendRow:", running_time, "seconds")
        return True


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        start_time = time.time()
        maxRow = self.dll.maxRow()
        newCol = self.dll.maxColumn() + 1
        
        
        for i in range(maxRow + 1):
            cell = Cell(row=i, col=newCol, val=None)
            self.dll.add(cell)
        
        end_time = time.time()
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for appendCol:", running_time, "seconds")

        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        start_time = time.time()
        maxCol = self.dll.maxColumn()
        if rowIndex < -1 or rowIndex >= self.rowNum():
            return False
        
        currentNode = self.dll.m_head
        while currentNode is not None:
            if currentNode.m_value.row > rowIndex:
                currentNode.m_value.row += 1
            currentNode = currentNode.m_next
        
        for i in range(maxCol + 1):
            cell = Cell(row=rowIndex + 1, col=i, val=None)
            self.dll.add(cell)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for Insert Row:", running_time, "seconds")
        
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        start_time = time.time()
        maxRow = self.dll.maxRow()
        if colIndex < -1 or colIndex >= self.colNum():
            return False
        
        currentNode = self.dll.m_head
        while currentNode is not None:
            if currentNode.m_value.col > colIndex:
                currentNode.m_value.col += 1
            currentNode = currentNode.m_next
        
        for i in range(maxRow + 1):
            cell = Cell(row=i, col=colIndex + 1, val=None)
            self.dll.add(cell)
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for Insert Col:", running_time, "seconds")
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

        gang = False
        start_time = time.time()
        if rowIndex < 0 or rowIndex > self.dll.maxRow() or colIndex < 0 or colIndex > self.dll.maxColumn():
            return False
        
        currentNode = self.dll.m_head
        while currentNode is not None:
            if currentNode.m_value.row == rowIndex and currentNode.m_value.col == colIndex:
                currentNode.m_value.val = value
                gang = True
                break
            currentNode = currentNode.m_next
            
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for Updating:", running_time, "seconds")
        
        return gang

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        start_time = time.time()
        var = self.dll.maxRow() + 1
        # Record the end time
        
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for Row Num:", running_time, "seconds")
        
        return var


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        start_time = time.time()
        var = self.dll.maxColumn() + 1
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for ColNum:", running_time, "seconds")
        
        return var



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        returnVar = []
        start_time = time.time()
        cur_node = self.dll.m_head
        for i in range(self.dll.m_length):
            if cur_node.get_value() is not None:
                if cur_node.get_value().val == value:
                    returnVar = [(cur_node.get_value().row, cur_node.get_value().col)]
            cur_node = cur_node.get_next()
            
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for Find:", running_time, "seconds")
            
        return returnVar
        
    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        start_time = time.time()
        returnlist = []
        
        currentNode = self.dll.m_head
        while currentNode is not None:
            if currentNode.get_value().val is not None:
                returnlist.append(currentNode.get_value())
            
            currentNode = currentNode.m_next
        
        returnlist = sorted(returnlist, key=lambda c: (c.row, c.col))
        
        # Record the end time
        end_time = time.time()
        # Calculate the running time
        running_time = end_time - start_time
        self.global_time += running_time
        print("Running time for entries:", running_time, "seconds")
        
        return returnlist
