




import FreeSimpleGUI as fsg
from typing import Callable, Any

class FinanceGUI:
    def __init__(self):
        self.theme = 'LightBlue2'
        fsg.theme(self.theme)
    
    def create_main_window(self, movements_data: list, balance: float) -> fsg.Window:
        layout = [
            [fsg.Text('Personal Finance Manager', font=('Arial', 16, 'bold'))],
            [fsg.Text(f'Current Balance: ${balance:.2f}', font=('Arial', 12), text_color='green' if balance >= 0 else 'red', key='-BALANCE-')],
            [fsg.HorizontalSeparator()],
            [
                fsg.Button('Add Category', size=12),
                fsg.Button('Add Expense', size=12),
                fsg.Button('Add Income', size=12),
                fsg.Button('Delete item(s)', size=12, button_color=('white', 'red')),
                fsg.Button('Refresh', size=12),
                fsg.Button('Exit', size=12)
            ],
            [fsg.HorizontalSeparator()],
            [
                fsg.Table(
                    values=movements_data,
                    headings=['Title', 'Amount', 'Category', 'Type', 'Date'],
                    auto_size_columns=False,
                    col_widths=[20, 10, 15, 10, 16],
                    justification='left',
                    key='-TABLE-',
                    enable_events=True,
                    expand_x=True,
                    expand_y=True,
                    num_rows=20,
                    select_mode=fsg.TABLE_SELECT_MODE_BROWSE
                )
            ],
            [fsg.Text('Select a transaction to delete', key='-SELECTION_INFO-', text_color='blue')]
        ]
        
        return fsg.Window(
            'Finance Manager',
            layout,
            size=(800, 600),
            resizable=True,
            finalize=True
        )
    
    def create_category_window(self) -> fsg.Window:
        layout = [
            [fsg.Text('Add New Category', font=('Arial', 12, 'bold'))],
            [fsg.Text('Category Name:'), fsg.Input(key='-CATEGORY_NAME-')],
            [
                fsg.Button('Save', size=10),
                fsg.Button('Cancel', size=10)
            ]
        ]
        
        return fsg.Window(
            'Add Category',
            layout,
            modal=True,
            finalize=True
        )
    
    def create_movement_window(self, movement_type: str, categories: list) -> fsg.Window:
        layout = [
            [fsg.Text(f'Add {movement_type.capitalize()}', font=('Arial', 12, 'bold'))],
            [fsg.Text('Title:'), fsg.Input(key='-TITLE-')],
            [fsg.Text('Amount:'), fsg.Input(key='-AMOUNT-')],
            [fsg.Text('Category:'), fsg.Combo(categories, key='-CATEGORY-', readonly=True)],
            [
                fsg.Button('Save', size=10),
                fsg.Button('Cancel', size=10)
            ]
        ]
        
        return fsg.Window(
            f'Add {movement_type.capitalize()}',
            layout,
            modal=True,
            finalize=True
        )
    
    def show_error(self, message: str):
        fsg.popup_error(message, title='Error')
    
    def show_info(self, message: str):
        fsg.popup_ok(message, title='Information')
    
    def show_confirm(self, message: str) -> bool:
        response = fsg.popup_yes_no(message, title='Confirm Deletion')
        return response == 'Yes'
    
    def validate_number_input(self, value: str) -> bool:
        try:
            num = float(value)
            return num > 0
        except ValueError:
            return False