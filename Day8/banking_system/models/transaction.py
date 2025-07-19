class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str:
        return f'거래 유형: {self.transaction_type}, 금액: {self.amount:,}원, 잔액: {self.balance:,}원'
    
    def to_tuple(self) -> tuple:
        return (self.transaction_type, f'{self.amount:,}원', f'잔액: {self.balance:,}원')