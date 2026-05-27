# 1. Cree una clase de `BankAccount` que:
#    1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#    3. Tengo un método para retirar dinero.
#    
#    Cree otra clase que herede de esta llamada `SavingsAccount` que:
#    
#    1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#    2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`. Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0, minimum_balance=100):
        super().__init__(initial_balance)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if (self.balance - amount) < self.minimum_balance:
            raise ValueError(f"Cannot withdraw. Account must maintain minimum balance of {self.minimum_balance}")
        self.balance -= amount
        return self.balance



account = BankAccount(1000)
account.deposit(500)  
account.withdraw(200)  

savings = SavingsAccount(1000, 500)
savings.deposit(300)   
savings.withdraw(700)  
savings.withdraw(100)  