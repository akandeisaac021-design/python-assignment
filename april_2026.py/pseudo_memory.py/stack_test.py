from CustomStack import *

import unittest

class TestCustomStack(unittest.TestCase):

    def setUp(self):

        self.stack = CustomStack()

    def test_initial_state(self):

        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.length(), 0)

    def test_push_increases_length(self):

        self.stack.push(10)
        self.assertEqual(self.stack.length(), 1)
        self.assertFalse(self.stack.is_empty())

        self.stack.push(20)
        self.assertEqual(self.stack.length(), 2)

    def test_peek_returns_top_element(self):

        self.stack.push("apple")
        self.stack.push("banana")
        
        self.assertEqual(self.stack.peek(), "banana")

        self.assertEqual(self.stack.length(), 2) 

    def test_pop_removes_and_returns_top_element(self):

        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.length(), 1)

        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_peek_empty_stack_raises_error(self):

        with self.assertRaises(AttributeError) as error_message:
            self.stack.peek()
        self.assertEqual(str(context.exception), "Stack is empty")

    def test_pop_empty_stack_raises_error(self):

        with self.assertRaises(AttributeError) as error_message:
            self.stack.pop()
        self.assertEqual(str(context.exception), "Stack is empty")

if __name__ == '__main__':
    unittest.main()

