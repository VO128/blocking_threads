import threading


class BankAccount:
    def __init__(self):
        self.balance = 100  # начальный баланс
        self.lock = threading.Lock()  # создаем объект блокировки

    def deposit(self, amount):
        with self.lock:  # блокировка
            self.balance += amount
            print(f"Взнос {amount}, новый баланс - {self.balance}")

    def withdraw(self, amount):
        with self.lock:  # блокировка
            if self.balance >= amount:
                self.balance -= amount
                print(f"Вывод -{amount}, новый баланс - {self.balance}")
            else:
                print("Недостаточно средств")


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
