

import json
import os
from typing import Optional
from logic import FinanceManager

class DataPersistence:
    def __init__(self, data_file: str = 'finance_data.json'):
        self.data_file = data_file
    
    def save_data(self, manager: FinanceManager) -> bool:

        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(manager.to_dict(), f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self) -> Optional[FinanceManager]:
        if not os.path.exists(self.data_file):
            return FinanceManager()
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return FinanceManager.from_dict(data)
        except Exception as e:
            print(f"Error loading data: {e}")
            return FinanceManager()