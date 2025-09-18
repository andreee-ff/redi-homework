from banking.src.v2.database import DatabaseConnection


class Account:
    def __init__(self, account_number: str, initial_balance: float = 0.0) -> None:
        self.db_connection = DatabaseConnection("db_url")
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.db_connection.save_account(self.account_number, self.balance)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.db_connection.save_account(self.account_number, self.balance)

    def get_balance(self) -> float:
        db_balance = self.db_connection.save_account(self.account_number)
        return db_balance
