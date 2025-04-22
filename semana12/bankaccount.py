# Cree una clase de BankAccount que:
# 1. Tenga un atributo de `balance`.
# 2. Tenga un método para ingresar dinero.
# 3. Tengo un método para retirar dinero.

# Cree otra clase que herede de esta llamada `SavingsAccount` que:

# 1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.

# 2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`.
# Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.

class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def balance(self):
        return self.balance

    def invoice(self,invoice):
        invoice=invoice
        self.balance=self.balance+invoice
        return self.balance

    def withdraw(self,withdraw):
        withdraw=withdraw
        self.balance=self.balance-withdraw
        return self.balance


class SavingsAccounts(BankAccount):
    def __init__(self, min_balance):
        self.min_balance=min_balance

    def saving_withdraw(self,amount):
        BankAccount.withdraw(amount)
            

#CLASS BANK ACCOUNT TESTING
operation=BankAccount(balance=50000)
invoice=operation.invoice(50000)
withdraw=operation.withdraw(80000)
print(operation.balance)

# CLASS SAVINGS
withdraw=SavingsAccounts(60000)

withdraw.saving_withdraw(50000)
