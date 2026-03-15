from unittest import TestCase

from list_begining import *

class test_for_pseudo_range_functions(TestCase):

    def test_for_second_highest_number_in_a_list(self):

        integer_list_sorter(numbers)
        second_highest_actual_value =numbers[-2]

        second_highest_expected_value =7


        self.assertEqual(second_highest_actual_value, second_highest_expected_value)
        
        return second_highest_actual_value

    def test_for_second_lowest_number_in_a_list(self):

        integer_list_sorter(numbers)

        second_lowest_actual_value =numbers[1]

        second_lowest_expected_value =2

        self.assertEqual(second_lowest_actual_value, second_lowest_expected_value)

        return second_lowest_actual_value

    def test_for_pseudo_range(self):

        integer_list_sorter(numbers)

        second_highest_actual_value =numbers[-2]

        second_lowest_actual_value =numbers[1]

        actual_pseudo_range =second_highest_actual_value - second_lowest_actual_value

        expected_pseudo_range =5
        
        self.assertEqual(actual_pseudo_range,expected_pseudo_range)
