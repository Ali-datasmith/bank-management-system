try:
    import json
    from datetime import datetime
    class AmountError(Exception):
        pass
    class InsufficientFunds(Exception):
        pass
    # the two errors are created using class
    class Account:
        def __init__(self,name,accountId,balance):
            print("***Welcome TO XYZ Bank***")
            self.transactionHistory = {}
            self.info={}
            self.report={}
            self.name = name
            self.accountId = accountId
            self.balance = balance
        # asks for information
        @property
        def name(self):
            return f"fname : {self.fname}\nlname : {self.lname}"
        @name.setter
        def name(self,value):
            parts = value.split()
            if(len(parts)<2):
                raise ValueError("**Name must be off two words***")
            self.fname = value.split()[0]
            self.lname = value.split()[1]
        # above two sets name to firstname and secondname
        def deposit(self,amount):
            self.now = datetime.now()
            self.formatted_time = self.now.strftime("%d-%b-%Y %H:%M:%S")
            match(amount):
                case amount if(amount<0):
                    raise AmountError(f"*Negative amount , current balance is ${self.getBalance()}*")
                case _:
                    print("---Deposition Successfull---")
                    self.balance+=amount
                    self.transactionHistory.update({f"Deposit at |{self.formatted_time}|" : f"|+${amount}| , Balance : |{self.getBalance()}|"})
        # above is deposition method
        def withDraw(self,amount):
            self.now = datetime.now()
            self.formatted_time = self.now.strftime("%d-%b-%Y %H:%M:%S")
            match(amount):
                case amount if(amount<0):
                    raise AmountError(f"*Negative amount , current balance is ${self.getBalance()}*")
                case amount if(amount>self.balance):
                    raise InsufficientFunds(f"*Insufficient funds, current balance is ${self.getBalance()}*")
                case _:
                    print("---Withdrawl Successful---")
                    self.balance-=amount
                    self.transactionHistory.update({f"WithDraw at |{self.formatted_time}|" : f"|-${amount}| , Balance : |{self.getBalance()}|"})
        # above is withdrawl method
        def showTransactionHistory(self):
            print("TransactionHistory : ")
            for key,values in self.transactionHistory.items():
                print(f"{key} : {values}")
            print("=======================")
        #helps to display t-history at exact time
        def saveReport(self):
            print("\nDo you Want to save the report if press yes : ")
            if(command:=(input("Enter command : ")).lower())=="yes":
                self.info={"FirstName ":self.fname,"SecondName":self.lname,"AccountId":self.accountId}
                self.report=self.info|self.transactionHistory
                file_name = input("Enter file_name : ")
                with open(file_name,"w") as f:
                    json.dump(self.report,f,indent=4)
                    print("Report saved successfully....")
        # asks if user wants to save report 
        # provides clean report in json format not txt
        def getBalance(self):
            return self.balance
        # returns balance and also helps us to make changes later...
        def __str__(self):
            return f"fname : {self.fname}\nlname : {self.lname}\nAccountId : {self.accountId}\nCurrentBalance : ${self.getBalance()}\n------------------------------------"
        #helps to display clean information
    a1 = Account("Ali Rajput","12345",200000)
    a1.deposit(2000)
    a1.withDraw(10000)
    a2 = Account("Zaid Syed","355474",130929)
    a2.deposit(100)
    a2.withDraw(3000)
except AmountError as aE:
    print(aE)
except InsufficientFunds as iF:
    print(iF)
except ValueError as v:
    print(v)
else:
    print(a1)
    a1.showTransactionHistory()
    a1.saveReport()
    print(a2)
    a2.showTransactionHistory()
    a2.saveReport()
# Note : Use of exception handling is important 
