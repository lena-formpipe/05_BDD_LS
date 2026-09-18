class BankAccount:
    def __init__(self, customer_name: str, balance=0):
        self._name = customer_name
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            return
        elif amount > 0:
            self._balance += amount

    def get_amount(self):
        return self._balance

    def withdraw(self, amount: float):
        # gör uttag om pengar finns
        if self._balance >= amount:
            self._balance -= amount
            return True
        else:
            return False


class Transaction:
    # Transaction har ingen __init__ för att inget sparas
    # just nu en statisk metod
    @staticmethod
    def transfer(
            amount: float, from_account: BankAccount, to_account: BankAccount
    ):
        # Överför pengar från ett konto till ett annat,
        # med hjälp av (bank_account) deposit och withdraw,
        if from_account.withdraw(amount):
            to_account.deposit(amount)
