import unittest
from project1 import *

class Project1Tests(unittest.TestCase):
    def test_condensePageName(self):
        self.assertEqual(condense_page_name("Ball State University"), "Ball_State_University")
        self.assertEqual(condense_page_name("  Ball State University      "), "Ball_State_University")


if __name__ == "__main__":
    unittest.main()