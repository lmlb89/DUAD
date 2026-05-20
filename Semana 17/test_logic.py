

import unittest
from logic import FinanceManager, Category, Movement

class TestFinanceManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = FinanceManager()
    
    def test_add_category_success(self):
        result = self.manager.add_category("Food")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.categories), 1)
        self.assertEqual(self.manager.categories[0].name, "Food")
    
    def test_add_category_duplicate(self):
        self.manager.add_category("Food")
        result = self.manager.add_category("Food")
        self.assertFalse(result)
        self.assertEqual(len(self.manager.categories), 1)
    
    def test_add_category_empty(self):
        result = self.manager.add_category("")
        self.assertFalse(result)
        result = self.manager.add_category("   ")
        self.assertFalse(result)
    
    def test_add_movement_success(self):
        self.manager.add_category("Salary")
        result = self.manager.add_movement("Monthly Salary", 1000.0, "Salary", "income")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.movements), 1)
    
    def test_add_movement_invalid_category(self):
        result = self.manager.add_movement("Test", 100.0, "NonExistent", "income")
        self.assertFalse(result)
        self.assertEqual(len(self.manager.movements), 0)
    
    def test_add_movement_invalid_amount(self):
        self.manager.add_category("Test")
        result = self.manager.add_movement("Test", -100.0, "Test", "income")
        self.assertFalse(result)
        result = self.manager.add_movement("Test", 0.0, "Test", "income")
        self.assertFalse(result)
    
    def test_get_balance_calculation(self):
        self.manager.add_category("Salary")
        self.manager.add_category("Food")
        
        self.manager.add_movement("Salary", 1000.0, "Salary", "income")
        self.manager.add_movement("Groceries", 150.0, "Food", "expense")
        self.manager.add_movement("Bonus", 200.0, "Salary", "income")
        
        balance = self.manager.get_balance()
        expected_balance = 1000.0 - 150.0 + 200.0
        self.assertEqual(balance, expected_balance)
    
    def test_get_categories_names(self):
        self.manager.add_category("Food")
        self.manager.add_category("Transportation")
        self.manager.add_category("Entertainment")
        
        names = self.manager.get_categories_names()
        self.assertEqual(len(names), 3)
        self.assertIn("Food", names)
        self.assertIn("Transportation", names)
        self.assertIn("Entertainment", names)
    
if __name__ == '__main__':
    unittest.main()