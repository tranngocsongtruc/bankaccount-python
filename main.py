##This is the demo class to test the BankAccount class

from BankAccount import BankAccount

#Instantiate 3 objects
samsAcc = BankAccount("Sam", "saving", 100)
leilasAcc = BankAccount("Leila", "saving", 500)
adamsAcc = BankAccount("Adam", "checking", 100)

#adding interest to all three accounts
adamsAcc.addInterest()
samsAcc.addInterest()
leilasAcc.addInterest()

#using getBalance to print
aName = adamsAcc.getName()
sName = samsAcc.getName()
lName = leilasAcc.getName()

aBalance = adamsAcc.getBalance()
sBalance = samsAcc.getBalance()
lBalance = leilasAcc.getBalance()

print(lName, f"'s balance after interest is ${lBalance:.2f}", sep="")
print(sName, f"'s balance after interest is ${sBalance:.2f}", sep="")
print(aName, f"'s balance after interest is ${aBalance:.2f}\n", sep="")

#testing exception with transfer more than balance amount
samTransferAdam = 200

adamReceivedSam = adamsAcc.transfer(samsAcc, samTransferAdam)

#testing transfer and getName/getBalance
LeilaTransferAdam = 50

adamReceivedLeila = adamsAcc.transfer(leilasAcc, LeilaTransferAdam)

print(aName,
      f"'s account balance after transfer is\
${(adamsAcc.getBalance()):.2f}",
      sep="")
print(lName,
      f"'s account balance after transfer is\
${(leilasAcc.getBalance()):.2f}",
      sep="")

#testing deposit then printing after the deposit
adamsAcc.deposit(100)
samsAcc.deposit(100)
leilasAcc.deposit(100)

print(lName,
      f"'s balance after deposit is ${(leilasAcc.getBalance()):.2f}",
      sep="")
print(sName,
      f"'s balance after deposit is ${(samsAcc.getBalance()):.2f}",
      sep="")
print(aName,
      f"'s balance after deposit is ${(adamsAcc.getBalance()):.2f}",
      sep="")
print()

#testing withdrawal of more than account balance with Adam, then with Sam and Leila THEN pringting Sam and Leila

withdrawAdam = 300
withdrawSam = 200
withdrawLeila = 200

adamsAcc.withdraw(withdrawAdam)
samsAcc.withdraw(withdrawSam)
leilasAcc.withdraw(withdrawLeila)

print(lName,
      f"'s balance after withdrawal is ${(leilasAcc.getBalance()):.2f}",
      sep="")
print(sName,
      f"'s balance after withdrawal is ${(samsAcc.getBalance()):.2f}",
      sep="")

#testing getAccNum and getAccountType
aAccNum = adamsAcc.getAccNum()
aAccType = adamsAcc.getAccountType()

print("Adam account num:", aAccNum)
print("Adam account type:", aAccType)

print()
#display all account information after alterations for all 3 accounts
samsAcc.displayAccountInfo()
print()
leilasAcc.displayAccountInfo()
print()
adamsAcc.displayAccountInfo()

##
