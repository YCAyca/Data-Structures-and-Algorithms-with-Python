""" Basic Tests to use with main code (Just Copy and Paste it under the "SparseMatrix_med.py if you want to try!) """
            
Sparse_Matrix = SparseMatrix(5,5,0) # 5x5 sparse matrix with default value 0 
Sparse_Matrix.set(0,1,3)
Sparse_Matrix.set(0,1,4) # check if the value is updated for a column having already a non default value
Sparse_Matrix.get(0,1)


Sparse_Matrix = SparseMatrix(5,5,0) # 5x5 sparse matrix with default value 0 
Sparse_Matrix.set(0,1,4)
Sparse_Matrix.set(0,2,4)
Sparse_Matrix.set(0,4,2)
Sparse_Matrix.set(1,2,23)
Sparse_Matrix.set(3,3,1)
Sparse_Matrix.set(3,4,1)

print("The Whole Sparse Matrix")
Sparse_Matrix.__str__() # see the Sparse Matrix

print("A spesific part of the Sparse Matrix")
Sparse_Matrix.__str__(2,3,2,2) # see the Sparse Matrix


gen1 = Sparse_Matrix.get_row(0)

list1 = []
try:
    while True:
        list1.append(next(gen1))
except StopIteration:
    pass   

print("row 0")
print(list1)

gen2 = Sparse_Matrix.get_row(3)  
list2 = []
try:
    while True:
        list2.append(next(gen2))
except StopIteration:
    pass 

print("row 3")
print(list2)


gen1 = Sparse_Matrix.get_col(2)
gen2 = Sparse_Matrix.get_col(4)  
list1 = []
try:
    while True:
        list1.append(next(gen1))
except StopIteration:
    pass   

list2 = []
try:
    while True:
        list2.append(next(gen2))
except StopIteration:
    pass  

print("column 0")
print(list1)    

print("column 4")
print(list2) 