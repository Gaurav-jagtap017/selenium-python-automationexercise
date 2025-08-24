import json
import os

class TestData:
    def __init__(self):
        self.test_data_dir = os.path.dirname(os.path.abspath(__file__))
        
    def load_test_data(self, file_name='test_users.json'):
        file_path = os.path.join(self.test_data_dir, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Test data file not found: {file_path}")
        with open(file_path, 'r') as file:
            return json.load(file)
    
    def get_user_data(self, user_key):
        data = self.load_test_data()
        print(data)
        return data.get(user_key, {})

