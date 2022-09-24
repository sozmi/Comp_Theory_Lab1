import unittest
import main

class TestSort(unittest.TestCase):
    #тест сортировки пузырьком-нечёт
    def test_bubble_sort_odd(self):    
        self.assertEqual([1,2,3,4,5,6,7], main.bubble_sort([7,6,5,4,3,2,1]))

    #тест сортировки пузырьком-чёт
    def test_bubble_sort_even(self):    
        self.assertEqual([1,2,3,4,5,6], main.bubble_sort([6,5,4,3,2,1]))

    #тест сортировки слиянием-нечёт
    def test_merge_sort_odd(self):    
        self.assertEqual([1,2,3,4,5,6,7], main.merge_sort([7,6,5,4,3,2,1]))

    #тест сортировки слиянием-чёт
    def test_merge_sort_even(self):    
        self.assertEqual([1,2,3,4,5,6], main.merge_sort([6,5,4,3,2,1]))

    #тест перевода массива в строку
    def test_composition(self):    
        self.assertEqual("1, 2, 3", main.array_to_string([1,2,3]))