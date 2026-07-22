


from datetime import datetime
from typing import List, Optional

class Category:
    def __init__(self, name: str):
        self.name = name
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            'name': self.name,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        category = cls(data['name'])
        category.created_at = datetime.fromisoformat(data['created_at'])
        return category

class Movement:
    def __init__(self, title: str, amount: float, category: str, movement_type: str):
        self.title = title
        self.amount = amount
        self.category = category
        self.movement_type = movement_type  # 'income' or 'expense'
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            'title': self.title,
            'amount': self.amount,
            'category': self.category,
            'movement_type': self.movement_type,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        movement = cls(data['title'], data['amount'], data['category'], data['movement_type'])
        movement.created_at = datetime.fromisoformat(data['created_at'])
        return movement

class FinanceManager:
    def __init__(self):
        self.categories: List[Category] = []
        self.movements: List[Movement] = []
    
    def add_category(self, name: str) -> bool:
        if not name or not name.strip():
            return False
        
        name = name.strip()
        if any(cat.name.lower() == name.lower() for cat in self.categories):
            return False
        
        self.categories.append(Category(name))
        return True
    
    def add_movement(self, title: str, amount: float, category: str, movement_type: str) -> bool:
        if not title or not title.strip():
            return False
        
        if amount <= 0:
            return False
        
        if not any(cat.name == category for cat in self.categories):
            return False
        
        title = title.strip()
        self.movements.append(Movement(title, amount, category, movement_type))
        return True
    
    def delete_movement(self, index: int) -> bool:
        if 0 <= index < len(self.movements):
            del self.movements[index]
            return True
        return False
    
    def delete_movements_by_indices(self, indices: List[int]) -> bool:
        if not indices:
            return False
        
        for index in sorted(indices, reverse=True):
            if 0 <= index < len(self.movements):
                del self.movements[index]
        
        return True
    
    def get_categories_names(self) -> List[str]:
        return [cat.name for cat in self.categories]
    
    def get_movements_table(self) -> List[List[str]]:
        table_data = []
        for movement in self.movements:
            table_data.append([
                movement.title,
                f"${movement.amount:.2f}",
                movement.category,
                movement.movement_type.capitalize(),
                movement.created_at.strftime("%Y-%m-%d %H:%M")
            ])
        return table_data
    
    def get_balance(self) -> float:
        balance = 0.0
        for movement in self.movements:
            if movement.movement_type == 'income':
                balance += movement.amount
            else:
                balance -= movement.amount
        return balance
    
    def get_movements_by_category(self, category: str) -> List[Movement]:
        return [mov for mov in self.movements if mov.category == category]
    
    def to_dict(self):
        return {
            'categories': [cat.to_dict() for cat in self.categories],
            'movements': [mov.to_dict() for mov in self.movements]
        }
    
    @classmethod
    def from_dict(cls, data):
        manager = cls()
        manager.categories = [Category.from_dict(cat_data) for cat_data in data.get('categories', [])]
        manager.movements = [Movement.from_dict(mov_data) for mov_data in data.get('movements', [])]
        return manager