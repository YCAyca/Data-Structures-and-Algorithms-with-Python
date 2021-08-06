import unittest 
from unittest import TestCase
import subsetsum_med
import itunes

class Test(TestCase):
    def test(self):
        with self.assertRaises(ValueError) : subsetsum_med.subset_sum(List1,8)
        self.assertEqual(subsetsum_med.subset_sum(List2,12), (10, 2)) 
        self.assertEqual(subsetsum_med.subset_sum(List2,50), {8, 10, 2, 4})
        self.assertEqual(subsetsum_med.subset_sum(List2,3), (2,)) 
        with self.assertRaises(ValueError) : subsetsum_med.subset_sum(List3,3)
        with self.assertRaises(ValueError) : subsetsum_med.subset_sum(List4,3)
        with self.assertRaises(ValueError) : subsetsum_med.subset_sum(List5,3)
        with self.assertRaises(ValueError) : subsetsum_med.subset_sum(List6,3)
        self.assertEqual(subsetsum_med.subset_sum(List6,10), {10})
        self.assertEqual(subsetsum_med.subset_sum(List6,15), {10})
        self.assertEqual(subsetsum_med.subset_sum(List7,200),(20, 12, 22, 15, 25, 19, 29, 18, 13, 17)) 
        self.assertEqual(subsetsum_med.subset_sum(List8,50), (25, 6, 19))
        reader = itunes.iTunesEntryReader("itunes_file.txt")
        itunes_subset = subsetsum_med.subset_sum(reader, 3600)
        for song in itunes_subset:
            print(song)
        self.assertEqual(sum(itunes_subset), 3600)
        
    

List1 = [10,2,8,8]
List2 = {10,2,8,4}    # 12 , 50, 3
List3 = [ ]  
List4 = { }
List5 = set() 
List6 = {10}    # 3, 10, 15
List7 = [20, 12, 22, 15, 25, 19, 29, 18, 11, 13, 17]  #200
List8 = [25, 27, 3, 12, 6, 15, 9, 30, 21, 19] # 50


if __name__=='__main__':
    unittest.main()
    
   

