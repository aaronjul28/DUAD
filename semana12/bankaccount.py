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

    # def balance(self):
    #     return self.balance

    def invoice(self,invoice):
        invoice=invoice
        self.balance=self.balance+invoice
        return self.balance

    def withdraw(self,withdraw):
        withdraw=withdraw
        self.balance=self.balance-withdraw
        return self.balance


class SavingsAccounts(BankAccount):
    def __init__(self,balance,min_balance):
        self.min_balance=min_balance
        super().__init__(balance)

    def savings_withdraw(self,amount):
        #CHECK ALL ATRIBUTES ARE POPULATING PROPERLY
        #print(self.balance, amount, self.min_balance)
        if self.withdraw(amount) < self.min_balance:
            print('The remaining would be lower than the minimum balance allowed')

        else:
            self.withdraw(amount)
            print(f'New balance is {self.balance}')

#CLASS BANK ACCOUNT TESTING
# operation=BankAccount(balance=50000)
# invoice=operation.invoice(50000)
# withdraw=operation.withdraw(80000)
# print(operation.balance)

# CLASS SAVINGS lower than minimum
withdraw=SavingsAccounts(balance=100000,min_balance=60000)
withdraw.savings_withdraw(amount=50000)

# CLASS SAVINGS higher than minimum
withdraw=SavingsAccounts(balance=100000,min_balance=60000)
withdraw.savings_withdraw(amount=1000)
