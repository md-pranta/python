from random import randint
class Bank:
    _allUser = []
    _totalBalance = 0
    _totalLoan = 0
    _loanFeature= False
    def userAccount(self, accID):
        for user in self._allUser:
            if accID==user._accountID:
                return user
        return 0
    def generateNumber(self):
        return randint(1,99)
    def createAccount(self,name, email, address, t):
        if t not in ['savings','current']:
            print('invalid type')
            return
        accID = self.generateNumber()
        while True:
            if self.userAccount(accID):
                accID = self.generateNumber()
            else: break

        user = User(accID,name, email, address,t)
        self._allUser.append(user)
        print(f'\nYour account Number is:{accID}\n')
    def userSection(self):
        while True:
            print("\n/////User Menu//////")
            print("1:create an account")
            print("2:Deposit")
            print("3:Withdraw")
            print("4:Check balance")
            print("5:Transaction history")
            print("6:Take a loan")
            print("7:Transfer money")
            print("8:Back to main menu")

            option = int(input('select a option 1 to 8:'))
            print()
            match option:
                case 1:
                    name = input('give name: ')
                    email = input('give email: ')
                    address = input('give address: ')
                    typ = input('give type(savings/current): ')
                    self.createAccount(name, email, address, typ)
                case 2:
                    acc = int(input('give account number:'))
                    user = self.userAccount(acc)
                    if user:
                        money = int(input('enter amount:'))
                        self._totalBalance+=money
                        user.deposit(money)
                    else:print('account is not valid')
                case 3:
                    acc = int(input('give account number:'))
                    user = self.userAccount(acc)
                    if self._loanFeature:
                        print('the bank is bankrupt')
                    elif user:
                        withdraw  = int(input('Give amount to withdraw :'))
                        user.withdraw(withdraw,self)
                    else:print('account is not valid')
                case 4:
                    acc = int(input('give account number:'))
                    user = self.userAccount(acc)
                    if user:
                        print(f'your account balance is {user._balance}taka')
                    else:print('account is not valid')
                case 5:
                    acc = int(input('give account number:'))
                    user = self.userAccount(acc)
                    if user:
                        for hist in user._history:
                            print(hist)
                    else:print('account is not valid')
                case 6:
                    acc = int(input('give account number:'))
                    user = self.userAccount(acc)
                    if self._loanFeature:
                        print('the bank is bankrupt')
                    elif user:
                        loan = int(input('enter loan amount:'))
                        user.takeLoan(self, loan)
                    else:print('account is not valid')
                case 7:
                    acc = int(input('give account number:'))
                    user = self.userAccount(acc)
                    if self._loanFeature:
                        print('the bank is bankrupt')
                    elif user:
                        targetACC = int(input('give  target account number:'))
                        targetUser = self.userAccount(targetACC)
                        if targetUser:
                            transf = int(input('enter transfer amount:'))
                            user.transfer(targetUser,transf)
                        else:print('target account ID is invalid')
                    else:print('account is not valid')
                case 8:
                    break
                case default:
                    print("select right option")
    def delete(self):
        acc = int(input('five id to delete the account:'))
        user = self.userAccount(acc)
        if user:
            self._allUser.remove(user)
            print('account deleted succesfully')
        else:print('account id is invalid')
    def view(self):
        for userobj in self._allUser:
            print('accountID: ',userobj._accountID)
            print('UserName: ',userobj._userName)
            print('Email: ',userobj._email)
            print('Address: ',userobj._address)
            print('type: ',userobj._accountType)
    def loanUser(self):
        acc = int(input('five id to delete the account:'))
        user = self.userAccount(acc)
        if user:
            user.__canTakeLoan = False
        else:print('account id is invalid')
class User():
    def __init__(self,accountID, userName, email, address, accountType) -> None:
        self._accountID = accountID
        self._userName = userName
        self._email = email
        self._address = address
        self._accountType = accountType
        self._balance = 0
        self._history = []
        self._loanCount = 0
        self._canTakeLoan = True
    def deposit(self, m):
        self._balance+=m
        self._history.append(f'deposit {m} taka')
    def withdraw (self, m,bank):
        if self._balance >= m:
            bank._totalBalance -= m
            self._balance -= m
            self._history.append(f'withdraw  {m} taka')
        else:print('can not withdraw \n')
    def takeLoan(self,bankObj, loan):
        if not self._canTakeLoan:
            print('administrator shutoff your loan system')
        elif self._loanCount >= 2:
            print('you already take maximum number loan')
        else:
            bank._totalLoan += loan
            self._balance += loan
            self._history.append(f'Loan {loan}taka')
    def transfer(self,target, amount):
        if self._balance >= amount:
            self._balance -= amount
            target._balance += amount
            self._history.append(f'transfer  {amount}taka')
            target._history.append(f'received  {amount}taka')

class Admin:
    def adminSection(self,bank):
        while True:
            print('////\nADMIN SECTION/////')
            print('1:create an account')
            print('2:delete any user account')
            print('3:see all user accounts list')
            print('4:check the total available balance of the bank')
            print('5:check the total loan amount')
            print('6:on or off the loan feature of the bank')
            print('6:on or off the loan feature for any user')
            print('8:return main section')

            option = int(input('select a option from 1 to 6:'))
            match option:
                case 1:
                    name = input('give name: ')
                    email = input('give email: ')
                    address = input('give address: ')
                    typ = input('give type(savings/current): ')
                    bank.createAccount(name, email, address, typ)
                case 2:
                    bank.delete()
                case 3:
                    bank.view()
                case 4:
                    print(f'total Balance of the Bank is {bank._totalBalance}tk')
                case 5:
                    print(f'total Loan of the Bank is {bank._totalLoan}tk')
                case 6:
                    bank._loanFeature = True
                case 7:
                    bank.loanUser()
                case 8:
                    break
                case default:
                    print('select right option')
        

bank = Bank()
admin = Admin()
while True:
    print('\n\\\\HOME\\\\\n1:user section')
    print('2:admin section')
    print('3:exit')

    option = int(input('select a option 1 to 3:'))

    match option:
        case 1:
            bank.userSection()
        case 2:
            admin.adminSection(bank)
        case 3:
            break
        case default:
            print('select right option')
        