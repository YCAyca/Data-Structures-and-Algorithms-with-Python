import unittest 
from unittest import TestCase
from SparseMatrix_med import SparseMatrix 
import SparseMatrix_med

class Test(TestCase):
    def test(self):
        Sparse_Matrix = SparseMatrix(5,5,0)  #5x5 sparse matrix with default value 0 
        self.assertEqual(Sparse_Matrix.get(0,0), 0) 
        Sparse_Matrix.set(0,1,3)
        self.assertEqual(Sparse_Matrix.get(0,1), 3)
        Sparse_Matrix.set(0,1,4)
        self.assertEqual(Sparse_Matrix.get(0,1), 4)
        with self.assertRaises(IndexError) : Sparse_Matrix.get(5,6)
        with self.assertRaises(IndexError) : Sparse_Matrix.set(5,6,3)
        with self.assertRaises(IndexError) : Sparse_Matrix.set(6,5,3)
        with self.assertRaises(TypeError) : Sparse_Matrix.set(2.3,1,3)
        with self.assertRaises(TypeError) : Sparse_Matrix.set(1,4.5,3)
        """ 
            After adding different values at the same (rox,col) 
            we see the length of that LinkedList is 1. So its true, we remove the node and then add the new one 
        """
        self.assertEqual(len(Sparse_Matrix.top_list[0]), 1) 
        """ 
            On the other hand, if we add replace the node with default value, the s
            the size of LL decrease, so we dont keep a Matrix Entry having default value
        """
        Sparse_Matrix.set(0,1,0)
        self.assertEqual(len(Sparse_Matrix.top_list[0]), 0) 
        Sparse_Matrix.clear()
        """ After clear() function, the length of all LinkedLists in top_list 
            is 0 and all the values are 0 (default valus)
        """
        for i in Sparse_Matrix.top_list:
            for k in i:
                self.assertEqual(k,0)
            self.assertEqual(len(i),0)    
        """ get_row testing """  
        Sparse_Matrix.set(0,2,4)
        Sparse_Matrix.set(0,4,2)
        Sparse_Matrix.set(1,2,23)
        Sparse_Matrix.set(3,3,1)
        Sparse_Matrix.set(3,4,1)
        gen1 = Sparse_Matrix.get_row(2.3)
        gen2 = Sparse_Matrix.get_row(7)  
        with self.assertRaises(TypeError) : print(next(gen1)) 
        with self.assertRaises(IndexError) : print(next(gen2))
        gen1 = Sparse_Matrix.get_row(0)
        gen2 = Sparse_Matrix.get_row(3)  
        list1 = []
        try:
            while True:
                list1.append(next(gen1))
        except StopIteration:
            pass   
        self.assertEqual(list1, [0,0,4,0,2])
        list2 = []
        try:
            while True:
                list2.append(next(gen2))
        except StopIteration:
            pass    
        self.assertEqual(list2, [0,0,0,1,1])
        
        """ get_col testing """
        gen1 = Sparse_Matrix.get_col(2.3)
        gen2 = Sparse_Matrix.get_col(7)  
        with self.assertRaises(TypeError) : print(next(gen1)) 
        with self.assertRaises(IndexError) : print(next(gen2))
        gen1 = Sparse_Matrix.get_col(2)
        gen2 = Sparse_Matrix.get_col(4)  
        list1 = []
        try:
            while True:
                list1.append(next(gen1))
        except StopIteration:
            pass   
        self.assertEqual(list1, [4,23,0,0,0])
        list2 = []
        try:
            while True:
                list2.append(next(gen2))
        except StopIteration:
            pass    
        self.assertEqual(list2, [2,0,0,1,0])
        
        """__str__ testing  """
        Sparse_Matrix.set(2,1,5)
        Sparse_Matrix.set(4,0,8)
        Sparse_Matrix.set(4,4,15)
        
        print("__str__() output")
        Sparse_Matrix.__str__()
        expected_str = str('0 0 4 0 2' + "\n" + '0 0 23 0 0'  + "\n" + '0 5 0 0 0' + "\n" + '0 0 0 1 1' + "\n" + '8 0 0 0 15')
        print("expected output")
        print(expected_str)
        
        print("__str__() output")
        Sparse_Matrix.__str__(2,3,2,2)
        expected_str = str('0 0' + "\n" + '1 1')
        print("expected output")
        print(expected_str)
        
        print("__str__() output")
        Sparse_Matrix.__str__(2,3,2,2)
        expected_str = str('0 0' + "\n" + '1 1')
        print("expected output")
        print(expected_str)
        
        print("__str__() output")
        Sparse_Matrix.__str__(1,2,1,1)
        expected_str = str('23')
        print("expected output")
        print(expected_str)
        
        with self.assertRaises(IndexError) : Sparse_Matrix.__str__(1,2,6,3)

if __name__=='__main__':
    unittest.main()
    
   