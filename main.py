# Gabriel Perez 6/11/2023
import unittest


# Function to test
def is_healthy(food):
    healthy_foods = ["apple", "orange", "banana", "grapes"]
    return food.lower() in healthy_foods


# Unit test class
class FoodTestCase(unittest.TestCase):
    def test_is_healthy(self):
        self.assertTrue(is_healthy(""), "Apple is healthy")
        self.assertTrue(is_healthy("grapes"), "grapes is healthy")
        self.assertFalse(is_healthy("pizza"), "Pizza is not healthy")
        self.assertFalse(is_healthy("ice cream"), "Ice cream is not healthy")

    def test_empty_food(self):
        self.assertFalse(is_healthy(""), "No food is not healthy")


# Running the tests
unittest.main()
