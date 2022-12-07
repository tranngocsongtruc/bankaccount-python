##This is BankAccount Module that contains both the BankAccount and Financial classes
class Financial:
    def percentOf(interestRate, balance):
        return balance * interestRate


class BankAccount:
    _lastAccNum = 1000

    def __init__(self, newAName, newAType, newBa, newIRate=0.03):
        self._balance = newBa
        self._accName = newAName
        BankAccount._lastAccNum = BankAccount._lastAccNum + 1
        self._accNum = BankAccount._lastAccNum
        self._accountType = newAType
        self._interestRate = newIRate

    def getBalance(self):
        return self._balance

    def getName(self):
        return self._accName

    def getAccountType(self):
        return self._accountType

    def getAccNum(self):
        return self._accNum

    def withdraw(self, amount):
        try:
            if amount <= self._balance:
                self._balance -= amount
            else:
                raise ValueError

        except ValueError:
            print(self._accName, "has insufficient funds\n")

    def deposit(self, amount):
        self._balance += amount

    def transfer(self, other, amount):
        try:
            if amount <= other._balance:
                self._balance += amount
                other._balance -= amount
            else:
                raise ValueError

        except ValueError:
            print(other._accName, "has insufficient funds\n")

    def displayAccountInfo(self):
        print("The account name:", self._accName)
        print("The account num:", self._accNum)
        print("The account type:", self._accountType)
        print(f"The account balance: ${(self._balance):.2f}")

    def addInterest(self):
        if self._accountType == "saving":
            self._balance += Financial.percentOf(self._interestRate,
                                                 self._balance)
