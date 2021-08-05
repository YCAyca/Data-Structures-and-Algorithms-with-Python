from linkedlist_med import LinkedList

class MatrixEntry:
    def __init__(self, column_number, value):
        self.column_number = column_number
        self.value = value
              
        
class SparseMatrix():
    def __init__(self, nrows, ncols, default_value):
        self.nrows = nrows
        self.ncols = ncols
        self.default_value = default_value
        self.top_list = list()
        for i in range(nrows):
            self.top_list.append(LinkedList())
            
    def set(self, row, col, value):  
        for i, d in enumerate(self.top_list[row]):
            if d.column_number == col :
                if value == self.default_value:
                    self.top_list[row].remove(self.top_list[row].__getitem__(i))
                    return
                else:
                    self.top_list[row].__getitem__(i).value = value
                    return
        new_entry = MatrixEntry(col, value)
        self.check_row(row) 
        self.check_row(col) 
        self.top_list[row].add_to_head(new_entry)
        
    def get(self, row, col):
         self.check_row(row) 
         self.check_row(col) 
         for i, d in enumerate(self.top_list[row]):
             if d.column_number == col :
                 matrix_entry = self.top_list[row].__getitem__(i)
                 return matrix_entry.value
         return self.default_value 
     
    def clear(self):
        for k in self.top_list:
            for i in k:
                self.top_list[k].remove(i)
        
    def check_row(self,row):
        if type(row) is not int:
            raise TypeError("row should be int")
        if row < 0 or row >= self.nrows:
            raise IndexError("row number is invalid")
       
    def check_col(self,col):
        if type(col) is not int:
            raise TypeError("col should be int")
        if col < 0 or col >= self.ncols:
            raise IndexError("col number is invalid") 
            
            
    def get_row(self, row):
        self.check_row(row)
        cur_col = 0    
        for i, ll in enumerate(self.top_list):
            if i == row:   
                while cur_col < self.ncols:
                    yield self.get(row,cur_col)
                    cur_col += 1
                break        
            
    def get_col(self, col):
        self.check_col(col)
        for i, ll in enumerate(self.top_list):
            yield self.get(i,col)
            
    def __str__(self, starting_row=0, starting_col=0, nrows=None, ncols=None):
        self.check_col(starting_col)
        self.check_row(starting_row)
        if nrows == None:
            nrows = self.nrows
        if ncols == None:
            ncols = self.ncols   
        """We should be sure if start points + row-col size doesnt exceed the matrix size """    
        self.check_col(starting_col+ncols-1)
        self.check_row(starting_row+nrows-1)     
        for i, ll in enumerate(self.top_list): 
            if i >= starting_row and i < starting_row+nrows:
                k = 0
                while starting_col+k < starting_col+ncols:
                    cur_col = starting_col+k
                    print(self.get(i,cur_col)," ", end = '')
                    k += 1
                print(" ")        




