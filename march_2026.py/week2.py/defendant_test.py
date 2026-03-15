import unittest
import defendant

class TestDefendantFunctions(unittest.TestCase):

    def test_random_integer_list_function(self):
        result = defendant.random_integer_list_function()
        self.assertEqual(len(result), 10)


    def test_list_of_sequential_integers_from_one_to_fifteen(self):
        result = defendant.list_of_sequential_integers_from_one_to_fifteen()
        self.assertEqual(len(result), 10)

    def test_length_function(self):
        self.assertEqual(defendant.length_function(self.sample_numbers), 5)

    def test_sum_of_even_indexes(self):
        self.assertEqual(defendant.sum_of_even_indexes(self.sample_numbers), 10 + 30 + 50)

    def test_sum_of_odd_indexes(self):
        self.assertEqual(defendant.sum_of_odd_indexes(self.sample_numbers), 20 + 40)

    def test_sum_of_every_third_index(self):
        self.assertEqual(defendant.sum_of_every_third_index(self.sample_numbers), 40)

    def test_multiple_of_every_third_index(self):
        self.assertEqual(defendant.multiple_of_every_third_index(self.sample_numbers), 40)

    def test_sum_of_first_last_and_middle(self):
        self.assertEqual(defendant.sum_of_first_last_and_middle(self.sample_numbers), 10 + 50 + 30)

    def test_integer_list_sorter(self):
        unsorted_list = [5, 3, 9, 1]
        sorted_list = defendant.integer_list_sorter(unsorted_list)
        self.assertEqual(sorted_list, [1, 3, 5, 9])

    def test_highest_number_in_a_list(self):
        sorted_list = [1, 3, 5, 9]
        self.assertEqual(defendant.highest_number_in_a_list(sorted_list), 9)

    def test_lowest_number_in_a_list(self):
        sorted_list = [1, 3, 5, 9]
        self.assertEqual(defendant.lowest_number_in_a_list(sorted_list), 1)

    def test_average_of_a_list(self):
        self.assertEqual(defendant.average_of_a_list(self.sample_numbers), sum(self.sample_numbers) / len(self.sample_numbers))

