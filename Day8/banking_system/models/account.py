from banking_system.models.transaction import Transaction
from banking_system.utils.decorator import validate_transaction

class Account:
    bank_name = ''
    def __init__(self) -> None:
        self.__balance = 0
        self.transactions = []

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount
            print(f'입금액: {amount:,}원')
            self.transactions.append(Transaction('입금',amount, self.__balance))
            print(f'현재 잔액: {self.__balance:,}원')

    @validate_transaction
    def withdraw(self, amount: int) -> None:
        amount = min(self.__balance, amount)
        self.__balance -= amount
        print(f'출금액: {amount:,}원')
        self.transactions.append(Transaction('출금',amount, self.__balance))
        print(f'현재 잔액: {self.__balance:,}원')

    def get_balance(self) -> int:
        return self.__balance
    
    def get_transactions(self) -> list:
        print('--거래내역--')
        return self.transactions
    
    def get_bank_name(cls) -> str:
        return cls.bank_name
    
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name