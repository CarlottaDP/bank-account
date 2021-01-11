# student ID 201537058 student Name: Carlotta Dipede


# Importing random modules to generate integers

import random  # importing for Cardnumber
import datetime  # importing for Cardexpire


# Designing Bank classic Account class


class BasicAccount:

    Num_BankAccounts = 0  # 0 is the intial number of accounts

    """
    A Primary account is an account type at the bank;
    It holds the holder's Name,
    account number, balance, Card Number,Card expiry date
    """

# Defining the static method

    @staticmethod
    def staticmethod():
        print('Static Method called')
    '''
    a static method is a function
    implemented to namespace all methods within BankAccount Class

        parameters:
            no parameters

        return:
            nothing
    '''


# Defining a function for the intialiser method to set the class attributes

    def _init_(self, TheName, TheBalance):
        self.name = TheName
        self.balance = TheBalance
        BasicAccount.Num_BankAccounts = + 1
        self.acNumb = BasicAccount.Num_BankAccounts
        self.cardNumb = random.randint(1000000000000000, 9999999999999999)
        todaysdate = datetime.date.today()
        issuingMonth = todaysdate.month()
        expYear = todaysdate.year
        self.cardExp = (issuingMonth, expYear)
        print("Welcome to your online Banking, {self.name}!".format(self=self))

# Designing a Documentation for each Program's Class purpose

    def __str__(self):

        '''
        Representing the instances within the BasicAccount Class

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
                nothing
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
                nothing
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
                nothing
    '''
    return float(self.balance)


def getBalance(self):

    '''
        informs the account holder of the account current balance

            parameters:
                 no parameters

            return:
                Balance - type(float)
    '''
    return float(self.balance)


def printBalance(self):

    '''
        prints the current money balance on the screen of the account holder

            parameters:
                 no parameters

            return:
                nothing
    '''


def getName(self):

    '''
         the account holder's name is retured on screen

            parameters:
                 no parameters

            return:
                self.name - type(string)
    '''


def getAcNum(self):

    '''
        Returns the account number to the screen of the account holder

            parameters:
                 no parameters

            return:
                AcNum - type(string)
    '''
    return str(self.name)


def issueNewCard(self):

    '''
        Creates a new card number,
        with the expiry being 3 years to current month

            parameters:
                 no parameters

            return:
                nothing
    '''

    # generating a new random Card number using Module
    self.cardNumb = random.randint(1000000000000000, 9999999999999999)
    todaysdate = datetime.date.today()  # this will be the date of today
    issuingMonth = todaysdate.month  # this is the month the card is requested
    expYear = todaysdate.year + 3  # expiry being 3 years to current month
    self.cardExp = (issuingMonth, expYear)
    print('{self.name} your New Card has now been issued'.format(self=self))


def CloseAccount(self):

    '''
        Returns any balance to the customer (via the withdraw method)

            parameters:
                 none

            return:
                True or False - type(Boolean)
    '''

    # setting the conditions for the boolean to return 'TRUE' 'FALSE'

    if self.balance >= 0:  # IF the customer is in debt to the bank
        self.withdraw(self.balance)
        return True
    else:                  # if the customer IS in debt to the bank
        return False


class PremiumAccount(BasicAccount):

    '''
        This Account is a SubClass of the BasicAccount Class:
        Premium members can have an overdraft of their overdraft limit.
    '''

# Defining a static method

    @staticmethod
    def staticmethod():
        print('Static Method called')

    '''
    a static method is a function
    implemented to namespace all methods within PremiumAccount SubClass

        parameters:
            no parameters

        return:
            nothing
    '''

# Defining a function for the intialiser method to set the class attributes

    def _init_(self, TheName, TheBalance, TheOverdraftLimit):
        super()._init_(TheName, TheBalance)
        self.OverdraftLimit = TheOverdraftLimit
        self.Overdraft = bool(self.OverdraftLimit > 0)  # if argument true
        self.OverdrafAmount = TheOverdraftLimit
        self.AbsoluteavailableBalance = (TheBalance + TheOverdraftLimit)


# Designing a documentation to inform of methods purposes  Withdraws

    def __str__(self):

        '''
    Documenting the instances within the premiumAccount SubClass

        parameters:
            no parameters

        return:
            The Account Holder: Name, Balance and Overdrafts settings
        '''

        return '{self.name}, your \nBalance is :€{self.balance}, your \noverdraft is:€ {self.overdraft}'



    def Withdraw(self, withdrawAmount):

        '''
    Documenting the instances within the premiumAccount SubClass

        parameters:
            Withdrawammount - (Type) Float

        return:
            Nothing
        '''
        self.Withdraw = withdrawAmount

        # Setting condition for invalid requests of withdraw
        if withdrawAmount < self.AbsoluteavailableBalance:

            print("\ncannot withdraw €:{self.Withdraw}\n".format(self=self))

        elif withdrawAmount < 0:

            print("\ncannot withdraw €:{self.Withdraw}\n".format(self=self))

        else:  # settting condition for valid withdraw request

            self.balance -= withdrawAmount
            print("withdrawn amount: €{self.Withdraw}\n".format(self=self))

    def getBalanceAvailable(self):

        '''
        Returning the Balance available within the Account

        parameters:
            no parameters

        return:
            Overdraft Amount and the Account Balance
        '''
        return float(self.AbsoluteavailableBalance)

    def PrintBalance(self):

        '''
        prints the current money balance on the screen and,
        prints Available overdraft

            parameters:
                 no parameters

            return:
                nothing
    '''
    # Defining conditions for the Balance to be printed:

        if self.balance < 0:  # when balance is less then 0
            # calculating the remaing allowance including the overdraft
            self.outstandingBalance = (self.OverdrafAmount + self.balance)
            print("{self.name}, your account is overdrawn by :€{self.balance}, \
            \nBalance:€{self.balance},\
            \nOustanding Balance:€{self.outstandingBalance},\
            ".format(self=self))
        else:
            self.outstandingBalance = (self.OverdrafAmount + self.balance)
            print("{self.name},\
             your \nOutstanding Balance is :€ {self.outstandingBalance},\
            ".format(self=self))

    def setOverdraftLimit(self, NewLimit):

        '''
        Sets the Overdraft limit to the new stated Amount:


            parameters:
                 no parameters

            return:
                nothing
        '''
        if NewLimit == 0:          # when limit equal to 0
            self.Overdraft = False    # the condition is False

        elif NewLimit < 0:
            print(" Unvalid Option - the Overdraft limit has to be 0 or above")

        else:
            self.OverdraftLimit = float(NewLimit)
 
    def CloseAccount(self):

        '''
        Sets the Overdraft limit to the new stated Amount:


            parameters:
                 no parameters

            return:
                nothing
        '''
    # setting True and False condition under which\
    # the Premium Account can be closed

        if self.balance < 0:
            print("{self.name}'s account cannot be closed,\
            the account is overdrawn by €{self.balance}.".format(self=self))
            return True


# Creating instances of Account holders


if __name__ == "_main_":   # Calling of instance withing a class
    Acc1 = BasicAccount("kim", 2500)
    Acc2 = PremiumAccount("Matt", 2500, 2500)
    Acc3 = PremiumAccount("Sierra", 2500, 0)

    Acc2.Withdraw(2500)   # passing parameters
    Acc2.CloseAccount()
    Acc2.setOverdraftLimit(0)
    Acc2.CloseAccount
