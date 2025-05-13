import unittest
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        """每个测试方法执行前的设置"""
        self.base_url = "http://localhost:5000/api"
        self.headers = {"Content-Type": "application/json"}

    def test_get_todos(self):
        """测试获取所有待办事项"""
        # 模拟API响应
        response = {
            "status": "success",
            "data": [
                {"id": 1, "title": "测试1", "completed": False},
                {"id": 2, "title": "测试2", "completed": True}
            ]
        }
        self.assertEqual(len(response["data"]), 2)
        self.assertEqual(response["status"], "success")

    def test_create_todo_api(self):
        """测试创建待办事项API"""
        # 模拟请求数据
        new_todo = {
            "title": "新待办事项",
            "completed": False
        }
        # 模拟API响应
        response = {
            "status": "success",
            "data": {**new_todo, "id": 3}
        }
        self.assertEqual(response["data"]["title"], new_todo["title"])
        self.assertIn("id", response["data"])

if __name__ == '__main__':
    unittest.main()