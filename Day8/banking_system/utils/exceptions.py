class InsufficientFundsError(Exception):
    def __init__(self, balance: int) -> None:
        super().__init__(balance)

class NegativeAmountError(Exception):
    def __init__(self) -> None:
        super().__init__()

class UserNotFoundError를(Exception):
    def __init__(self, username: str) -> None:
        super().__init__(username)