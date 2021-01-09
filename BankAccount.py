# student ID 201537058 student Name: Carlotta Dipede


# Importing random modules to generate integers

import random  # importing for Cardnumber
import datetime  # importing for Cardexpire


# Designing Bank Account class


class PrimaryAccount:

    Num_BankAccounts = 0  # 0 is the intial number of accounts

    """
    A Primary account is an account type at the bank;
    It holds the holder's Name,
    account number, balance, Card Number,Card expiry date
    """

# Defining the static method

    @staticmethod
    def staticmethod():
        return ' Static Method called'
    '''
    a static method is a function
    implemented to namespace all methods within BankAccount Class

        parameters:
            no parameters

        return:
            no return
    '''


# Defining a function for the intialiser method to set the class attributes

    def _init_(self, TheName, TheBalance):
        self.name = TheName
        self.balance = TheBalance
        PrimaryAccount.Num_BankAccounts = + 1
        self.acNumb = PrimaryAccount.Num_BankAccounts
        self.cardNumb = random.randint(1000000000000000, 9999999999999999)
        todaysdate = datetime.date.today()
        issuingMonth = todaysdate.month()
        expYear = todaysdate.year
        self.cardExp = (issuingMonth, expYear)
        print("Welcome to your online Banking, {self.name}!".format(self=self))

# Designing a Documentation for each Program's Class purpose

    def __str__(self):

        '''
        Representing the instances within the PrimaryAccount Class

            parameters:
                 no parameters

            return:
                the account holders details: Account Name and Opening Balance
        '''
        return '{self.name} your balance is:€{self.balance}.'.format(self=self)

# Designing a method to Deposit currency


def Deposit(self, theDepositAmmount):

    '''
        This method, deposits a  Ammount into the person's Account and
         then adjust the remaining balance.

            parameters:
                theDepositAmmount - type(Float)

            return:
                nothing to return
    '''

    self.depositAmmount = (theDepositAmmount)

    if theDepositAmmount < 0:  # if the account holder input a negative integer
        print("Invalid Option!-please enter a positive number this time!")
    else:
        self.balance += theDepositAmmount
        print('your New balance is now:€ {self.balance}.'.format(self=self))


def Withdraw(self, WithdrawAmmount):

    '''
        Withdraws the stated amount from the account and adjusts new balance

            parameters:
                 WithdrawAmmount - type(Float)

            return:
                nothing to return
    '''

    self.Withdraw = WithdrawAmmount

    if Withdraw > self.balance:
        print(" Withdraw request: Declined - Insufficients funds ")
    else:
        self.balance -= WithdrawAmmount

        print('withdrawn Amount: €{self.withdrawAmmount}.')
        print('Your New balance is:{self.balance}'.format(self=self))

        return self.balance


def getBalanceAvailable(self):

    '''
        Withdraws the stated amount from the account and adjusts new balance

            parameters:
                 WithdrawAmmount - type(Float)

            return:
                nothing to return
    '''