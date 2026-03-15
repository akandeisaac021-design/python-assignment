from unittest import TestCase

#from digit_length_function import collect_two_integers


class digit_length_unittest(TestCase):
    
    def test_to_check_if_second_number_is_between_two_and_thirty_six(self):
        second_number =14

        if (second_number <2 and second_number >36):
            expected =-1

        else:
            expected =second_number

        actual =14

        self.assertEqual(expected, actual) 

        return expected

    def test_if_first_number_is_negative(self):
        first_number =0

        if (first_number <0):
            expected =0

        else:
            expected =first_number

        actual =0

        self.assertEqual(expected, actual)


        
    def test_(self):
        first_number =0

        if (first_number <0):
            expected =0

        else:
            expected =first_number

        actual =0

        self.assertEqual(expected, actual)


