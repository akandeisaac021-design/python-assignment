from unittest import TestCase
from list_manipulator import *

class TestDefendantFunctions(unittest.TestCase):

    def test_random_integer_list_function_creates_a_list_of_ten_spaces(self):
        result = random_integer_list_function()
        self.assertEqual(len(result), 10)

    def test_list_length_function(self):
        sample_numbers =[1, 2, 3, 4, 5]
        self.assertEqual(list_length_function(sample_numbers), 5)

    def test_sum_of_even_indexes(self):
        sample_numbers =[10, 2, 30, 4, 50]
        self.assertEqual(sum_of_even_indexes(sample_numbers), 10 + 30 + 50)

    def test_sum_of_odd_indexes(self):
        sample_numbers =[10, 20, 30, 40, 50]
        self.assertEqual(sum_of_odd_indexes(sample_numbers), 20 +40)

    def test_sum_of_every_third_index(self):
        sample_numbers =[10, 20, 30, 40, 50]
        self.assertEqual(sum_of_every_third_index(sample_numbers), 30)

    def test_multiple_of_every_third_index(self):
        sample_numbers =[10, 20, 30, 40, 50, 60]
        self.assertEqual(multiple_of_every_third_index(sample_numbers), 30 *60)

    def test_sum_of_first_last_and_middle(self):
        sample_numbers =[10, 20, 30, 40, 50]
        self.assertEqual(sum_of_first_last_and_middle(sample_numbers), 10 +50 +30)

    def test_integer_list_sorter(self):
        unsorted_list = [5, 3, 9, 1]
        sorted_list = integer_list_sorter(unsorted_list)
        self.assertEqual(sorted_list, [1, 3, 5, 9])

    def test_highest_number_in_a_list(self):
        sorted_list = [1, 3, 5, 9]
        self.assertEqual(highest_number_in_a_list(sorted_list), 9)

    def test_lowest_number_in_a_list(self):
        sorted_list = [1, 3, 5, 9]
        self.assertEqual(lowest_number_in_a_list(sorted_list), 1)

    def test_average_of_a_list(self):
        sample_numbers =[10, 2, 30, 4, 50]
        self.assertEqual(average_of_a_list(sample_numbers), sum(sample_numbers) / len(sample_numbers))
