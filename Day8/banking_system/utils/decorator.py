from banking_system.utils.exceptions import NegativeAmountError

def validate_transaction(func: callable) -> callable:
    def wrapper(self, amount, *args, **kwarg):
        if amount <= 0:
            raise NegativeAmountError("금액은 0보다 커야 합니다.")
        return func(self, amount, *args, **kwarg)
    return wrapper