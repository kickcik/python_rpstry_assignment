from services.banking_service import BankingService

def main() -> None:
    bs = BankingService()
    bs.add_user(username:=input('사용자명: '))
    bs.user_menu(username)
    print('--시스템 종료--')

if __name__ == '__main__':
    main()