import datetime
import random
details = {}

def main():
    print("\t\t\t\tWelcome to PyATM v2.0")
    
    account = input("\n Existing User press 1 \n New User press 2\n \t\t\t Enter 0 or cancel to cancel operation \n")
    if (account == "1"):
        existingUser()
    elif (account == "2"):
        createUser()
    elif ((account == "0")):
        main()
    else:
        print("Invalid Entry")
        main()
        
            

def existingUser():
    
    print("\t\t\t\tLogin for Existing User\n")
    password = input("Enter password \n")
    if (password == ""):
        print("password field cannot be empty")
        existingUser()
    elif ((password == "0")):
        main()
    else:  
        for bank,user in details.items():
            if(user[3] == password):
                operation(user)
            else:
                print('\nInvalid Password')
                existingUser()

    
def createUser():
    print("\n\t\t\t\tRegistering New User \n\t\t\tlets capture some of your details\n")

    bank = input("Enter Name of your Bank \n")
    contact = input("Enter Phone Number? \n")
    first_name = input("Enter your first name? \n")
    last_name = input("Enter yourlast name? \n")
    password = input("enter desired password \n")

    acctNo = acctGenerator()

    details[acctNo] = [ first_name, last_name, contact, password, bank ]

    print(" **************************************************************")
    print("*\tYour Account Details with %s" %bank)
    
    print("*\t Your account name is: %s %s" % (first_name, last_name))
    print("*\t Phone Number linked to this account is: %s" % contact)
    print("*\t Account number is: %d" % acctNo)
    print("*\t SafeKey number is: %s" % password)
    print("*\t These are highly confidentail")
    print(" **************************************************************")

    existingUser()

def operation(customer):

    now = datetime.datetime.now()

    print ("\t\t\t\t %s" %now.strftime("%Y-%m-%d %H:%M:%S"))
            
    print("\t\t\tWelcome %s %s " % ( customer[1], customer[0] ) )

    Option = input("What action do you want to perform \n(1) deposit \n(2) withdrawal \n(3) CheckBalance \n(4) PurchaseAirtime \n(5) Logout \n(6) Exit\n")

    if(Option == "1"):
        deposit()
    elif(Option == "2"):
        withdrawal()
    elif(Option == "3"):
        checkBalance()
    elif(Option == "4"):
        airtimePurchase()
    elif(Option == "5"):
        logout()
    elif(Option == "6"):
        exit()
    else:
        print("Invalid option selected")
        operation(customer)


def withdrawal():
    
    WithCash = int(input("How Much do you want to withdrawl: \n#"))
    initalCash = 5000
    if WithCash < initalCash:
        currentBalance =  initalCash - WithCash
        print("take your cash\n")
    elif WithCash == initalCash:
        currentBalance =  initalCash - WithCash
        print("take your cash\n")
    else:
        print("Insufficent Fund")
    
    contOpt = str(input("do you want to perform another task\nYES \t\t\t\t NO? \n").upper())
    if contOpt =="YES":
        contOpt2 = str(input("Another Transaction\nYES \t\t\t\t NO? \n").upper())
        if contOpt2:
            withdrawal()
    elif contOpt == "NO":
        print("Thank you for contacting us")
        exit()
    elif contOpt == "other":
        main()
    else:
        print("Oops invalid Entry\n")
        main()

    
def airtimePurchase():
    Amount = int(input("How Much airtime do you want to purchase: \n#"))
    initalCash = 5000
    if Amount <= initalCash:
        print('These are the available network:')
        print('1. MTN')
        print('2. GLO')
        print('3. AIRTEL')
        print('4. 9MOBILE')

        selected = input('Please select an option:')
                
        if(selected == "1"):
            No = int(input("Enter Phone Number: \n#"))
            print("Purchasing # %i" % Amount + " for %i" % No)
            allow =  initalCash - Amount
            print("Available Balance %i " % allow)
            
        elif(selected == "2"):
            No = int(input("Enter Phone Number: \n#"))
            print("Purchasing # %i" % Amount + " for %i" % No)
            allow =  initalCash - Amount
            print("Available Balance %i " % allow)
                    
        elif(selected == "3"):
            No = int(input("Enter Phone Number: \n#"))
            print("Purchasing # %i" % Amount + " for %i" % No)
            allow =  initalCash - Amount
            print("Available Balance %i " % allow)
            
        elif(selected == "4"):
            No = int(input("Enter Phone Number: \n#"))
            print("Purchasing # %i" % Amount + " for %i" % No)
            allow =  initalCash - Amount
            print("Available Balance %i " % allow)
        else:
            print('Invalid Option selected, please try again')
            airtimePurchase()

        
    elif Amount > initalCash:
        print("Insufficent Fund")
    else:
        print("Inavlid Entry ")
    
    contOpt = str(input("do you want to perform another task\nYES \t\t\t\t NO? \n").upper())
    if contOpt =="YES":
        contOpt2 = str(input("Another Transaction\nYES \t\t\t\t NO? \n").upper())
        if contOpt2:
            withdrawal()
    elif contOpt == "NO":
        print("Thank you for contacting us")
        exit()
    elif contOpt == "other":
        main()
    else:
        print("Oops invalid Entry\n")
        main()


        
        
def checkBalance():
      
    currentBalance = 40000
    print("Current balance: # %i" % currentBalance)
    contOpt = str(input("do you want to perform another task\n enter YES \t\t\t\t enter NO? \n").upper())
    if contOpt =="YES":
        main()
    elif contOpt == "NO":
        print("Thank you for contacting us")
        exit()
    else:
        print("Oops invalid Entry\n")
        main()


def deposit():
    
    DepCash = int(input("How Much do you want to deposit: \n#"))
    print("Deposited Amount: # %s" % DepCash)
    initalCash = 4000
    currentBalance = DepCash + initalCash
    print("Current balance: # %i" % currentBalance)
    contOpt = str(input("do you want to perform another task\n enter YES \t\t\t\t enter NO? \n").upper())
    if contOpt =="YES":
        main()
    elif contOpt == "NO":
        print("Thank you for contacting us")
        exit()
    else:
        print("Oops invalid Entry\n")
        main()



def acctGenerator():
    return random.randrange(2000000000,9999999999)

def logout():
    existingUser()
    

main()
