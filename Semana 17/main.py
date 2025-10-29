


import FreeSimpleGUI as fsg
from logic import FinanceManager
from persistence import DataPersistence
from interfaces import FinanceGUI

class FinanceApp:
    def __init__(self):
        self.gui = FinanceGUI()
        self.persistence = DataPersistence()
        self.manager = self.persistence.load_data()
        self.selected_rows = []  # 
    
    def run(self):
        window = self.gui.create_main_window(
            self.manager.get_movements_table(),
            self.manager.get_balance()
        )
        
        while True:
            event, values = window.read()
            
            if event in (fsg.WIN_CLOSED, 'Exit'):
                break
            
            elif event == 'Add Category':
                self._handle_add_category()
                self._refresh_main_window(window)
            
            elif event == 'Add Expense':
                self._handle_add_movement('expense', window)
            
            elif event == 'Add Income':
                self._handle_add_movement('income', window)
            
            elif event == 'Delete Selected':
                self._handle_delete_movements(window)
            
            elif event == 'Refresh':
                self._refresh_main_window(window)
            
            elif event == '-TABLE-':
                self.selected_rows = values['-TABLE-']
                self._update_selection_info(window)
        
        self.persistence.save_data(self.manager)
        window.close()
    
    def _handle_add_category(self):
        category_window = self.gui.create_category_window()
        
        while True:
            event, values = category_window.read()
            
            if event in (fsg.WIN_CLOSED, 'Cancel'):
                break
            
            elif event == 'Save':
                category_name = values['-CATEGORY_NAME-']
                if not category_name:
                    self.gui.show_error('Category name cannot be empty')
                    continue
                
                if self.manager.add_category(category_name):
                    self.gui.show_info(f'Category "{category_name}" added successfully')
                    self.persistence.save_data(self.manager)
                    break
                else:
                    self.gui.show_error('Category already exists or name is invalid')
        
        category_window.close()
    
    def _handle_add_movement(self, movement_type: str, main_window):
        categories = self.manager.get_categories_names()
        
        if not categories:
            self.gui.show_error('No categories available. Please add a category first.')
            return
        
        movement_window = self.gui.create_movement_window(movement_type, categories)
        
        while True:
            event, values = movement_window.read()
            
            if event in (fsg.WIN_CLOSED, 'Cancel'):
                break
            
            elif event == 'Save':
                title = values['-TITLE-']
                amount_str = values['-AMOUNT-']
                category = values['-CATEGORY-']
                
                if not title:
                    self.gui.show_error('Title cannot be empty')
                    continue
                
                if not self.gui.validate_number_input(amount_str):
                    self.gui.show_error('Amount must be a positive number')
                    continue
                
                if not category:
                    self.gui.show_error('Please select a category')
                    continue
                
                amount = float(amount_str)
                
                if self.manager.add_movement(title, amount, category, movement_type):
                    self.gui.show_info(f'{movement_type.capitalize()} added successfully')
                    self.persistence.save_data(self.manager)
                    self._refresh_main_window(main_window)
                    break
                else:
                    self.gui.show_error('Error adding movement. Please check your inputs.')
        
        movement_window.close()
    
    def _handle_delete_movements(self, window):
        if not self.selected_rows:
            self.gui.show_error('Please select one or more transactions to delete.')
            return
        
        selected_movements = []
        for row_index in self.selected_rows:
            if row_index < len(self.manager.movements):
                movement = self.manager.movements[row_index]
                selected_movements.append(f"{movement.title} - ${movement.amount:.2f}")
        
        if not selected_movements:
            self.gui.show_error('No valid transactions selected.')
            return
        
        if len(selected_movements) == 1:
            message = f"Are you sure you want to delete this transaction?\n\n{selected_movements[0]}"
        else:
            message = f"Are you sure you want to delete these {len(selected_movements)} transactions?\n\n" + "\n".join(selected_movements)
        
        if self.gui.show_confirm(message):
            if self.manager.delete_movements_by_indices(self.selected_rows):
                self.gui.show_info(f'Successfully deleted {len(self.selected_rows)} transaction(s)')
                self.persistence.save_data(self.manager)
                self.selected_rows = []  
                self._refresh_main_window(window)
            else:
                self.gui.show_error('Error deleting transactions.')
    
    def _update_selection_info(self, window):
        if self.selected_rows:
            count = len(self.selected_rows)
            window['-SELECTION_INFO-'].update(f'{count} transaction(s) selected for deletion')
        else:
            window['-SELECTION_INFO-'].update('Select a transaction to delete')
    
    def _refresh_main_window(self, window):
        window['-TABLE-'].update(self.manager.get_movements_table())
        
        balance = self.manager.get_balance()
        window['-BALANCE-'].update(f'Current Balance: ${balance:.2f}')
        
        text_color = 'green' if balance >= 0 else 'red'
        window['-BALANCE-'].update(text_color=text_color)
        
        self.selected_rows = []
        self._update_selection_info(window)

if __name__ == '__main__':
    app = FinanceApp()
    app.run()