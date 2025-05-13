import unittest
from datetime import datetime

class TestTodo(unittest.TestCase):
    def setUp(self):
        """每个测试方法执行前的设置"""
        self.todo_data = {
            "id": 1,
            "title": "测试待办事项",
            "completed": False,
            "created_at": datetime.now()
        }

    def test_create_todo(self):
        """测试创建待办事项"""
        self.assertEqual(self.todo_data["title"], "测试待办事项")
        self.assertFalse(self.todo_data["completed"])

    def test_update_todo(self):
        """测试更新待办事项"""
        self.todo_data["completed"] = True
        self.assertTrue(self.todo_data["completed"])

    def test_delete_todo(self):
        """测试删除待办事项"""
        self.todo_data = None
        self.assertIsNone(self.todo_data)

if __name__ == '__main__':
    unittest.main()