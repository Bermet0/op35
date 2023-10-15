class SavingAccount:
    pass


class CheckingAccount:
    pass


class RealEstate:
    pass


class Bond:
    pass


class Stock:
    pass


class BankAccount(SavingAccount, CheckingAccount):
    pass


class Security(Bond, Stock):
    pass


class InterestBearingItem(BankAccount, Security):
    pass


class Asset(RealEstate, BankAccount, Security):
    pass


class InsurableItem(RealEstate, BankAccount):
    pass
