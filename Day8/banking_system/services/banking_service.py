from banking_system.models.user import User

class BankingService:
    def __init__(self) -> None:
        self.users = []

    def add_user(self, username: str) -> None:
        user = User(username)
        self.users.append(user)

    def find_user(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        raise NotImplementedError
    
    def user_menu(self, username: str) -> None:
        user = self.find_user(username)
        while True:
            try:
                cmd = int(input('(0)종료 (1)입금 (2)출금 (3)잔고확인 (4)거래내역 : '))
                if cmd == 0:
                    break

                actions = {
                    1: lambda: user.account.deposit(int(input('입금액을 입력하세요 : '))),
                    2: lambda: user.account.withdraw(int(input('출금액을 입력하세요: '))),
                    3: lambda: print(f'현재 잔액: {user.account.get_balance()}원'),
                    4: lambda: print(*user.account.get_transactions(), sep='\n')
                }
                
                actions.get(cmd, lambda: print('표시된 작업을 선택해주세요.'))()
            except ValueError as e:
                print('숫자를 입력해주세요.')