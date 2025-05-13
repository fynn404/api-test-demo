#!/usr/bin/env python3
import pprint

import requests
import json
from typing import Dict, Optional


class APITester:
    def __init__(self, base_url: str = "http://localhost:9527/api/v1"):
        self.base_url = base_url
        self.tokens = {
            'admin': None,
            'user': None,
        }
        self.test_users = {
            'admin': {'username': 'admin_test1', 'password': 'admin123', 'role': 'admin', 'nickname': 'Admin User',
                      'email': 'admin1@test.com'},
            'user': {'username': 'user_test1', 'password': 'user123', 'role': 'user', 'nickname': 'username123',
                        'email': 'student1@test.com'}
        }
        self.test_update_users = {
            'admin': {'username': 'admin_test2', 'password': 'admin234', 'role': 'admin', 'nickname': 'admin_name666',
                      'email': 'admin_new@test.com'},
            'user': {'username': 'user_test1_new', 'password': 'user666', 'role': 'user',
                        'nickname': 'username666New',
                        'email': 'student_new2@test.com'}
        }

    def make_request(self, method: str, endpoint: str, data: Optional[Dict] = None,
                     token: Optional[str] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        headers = {'Content-Type': 'application/json'}
        # Print the request details
        print(f"\nRequest: {method} {url}")

        if data:
            print(f"Request: {json.dumps(data, indent=2)}")

        if token:
            headers['Authorization'] = f'Bearer {token}'
        print(f"Headers: {headers}")
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=headers)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            print(f"\n{method} {endpoint}")
            print(f"Status Code: {response.status_code}")
            # 将 JSON 字符串解析为 Python 对象
            data = json.loads(response.text)
            pprint.pprint(data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None

    def register_user(self, user_type: str) -> bool:
        user_data = self.test_users[user_type]
        response = self.make_request('POST', '/auth/register', user_data)
        return response and response.status_code in [201, 200]

    def login_user(self, user_type: str) -> bool:
        user_data = {
            'username': self.test_users[user_type]['username'],
            'password': self.test_users[user_type]['password']
        }
        response = self.make_request('POST', '/auth/login', user_data)
        if response and response.status_code == 200:
            self.tokens[user_type] = response.json().get('data',{}).get('access_token')
            return True
        return False

    def test_user_profile(self, user_type: str) -> bool:
        response = self.make_request('GET', '/users/profile', token=self.tokens[user_type])
        return response and response.status_code == 200

    def update_user_profile(self, user_type: str) -> bool:
        user_data = {
            'nickname': self.test_update_users[user_type]['nickname'],
            'email': self.test_update_users[user_type]['email'],
            'password': self.test_update_users[user_type]['password']
        }
        response = self.make_request('PUT', '/users/profile', data=user_data, token=self.tokens[user_type])
        return response and response.status_code == 200

    def cleanup(self) -> bool:
        return True

    def run_all_tests(self):
        return

if __name__ == "__main__":
    # # Create API tester instance
    tester = APITester()
    user_type = 'user'
    # tester.register_user(user_type)
    tester.login_user(user_type)
    tester.test_user_profile(user_type)
    tester.update_user_profile(user_type)
    tester.login_user(user_type)

