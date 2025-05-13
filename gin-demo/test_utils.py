import unittest
from datetime import datetime

class TestUtils(unittest.TestCase):
    def test_date_format(self):
        """测试日期格式化"""
        date = datetime(2024, 3, 15, 10, 30, 0)
        formatted = date.strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(formatted, "2024-03-15 10:30:00")

    def test_validate_todo_data(self):
        """测试待办事项数据验证"""
        todo_data = {
            "title": "测试",
            "completed": False
        }
        self.assertIn("title", todo_data)
        self.assertIn("completed", todo_data)
        self.assertIsInstance(todo_data["title"], str)
        self.assertIsInstance(todo_data["completed"], bool)

if __name__ == '__main__':
    unittest.main()