''' A class named custoemr with three attributes namely name,date of birth,mobile.
2 methods to get and print details
calculating age and dob is date with private scope'''

from datetime import datetime
class Customer:
    def __init__(self):
        self.name=''
        self.__date_of_birth='' #private data member
        self.mobile=''

    def getDetails(self):
        self.name=input("Enter name : ")
        self.__date_of_birth=input("Enter date of birth (MM/DD/YYYY) : ")
        self.mobile=input("Enter mobile number : ")
        self.__date_of_birth=datetime.strptime(self.__date_of_birth,"%m/%d/%Y")

    def displayDetails(self):
        now=datetime.now()
        age=now.year-self.__date_of_birth.year#to calculate the age in years
        print("Name : ",self.name)
        print("Date of birth : ",self.__date_of_birth.strftime("%d-%m-%Y"))
        print("Age : ",age)
        print("Mobile : ",self.mobile)

c=Customer()
c.getDetails()
print("\n\n-----Customer details------")
c.displayDetails()
