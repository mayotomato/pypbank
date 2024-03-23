import datetime

# controls:
accept = 'y'
cancel = 'n'
goback = 'q'

superuser = ["YNAYNA", "IS EPIC"]


def overwrite(accountName, password, id, type, passportNID, DOB, phoneNumber, address, currency,  bal, first_time_login):
    accountDetails = ["PASSWORD: " + password + '\n',
                      "ACCOUNT ID: " + id + '\n',
                      "ACCOUNT TYPE: " + type + '\n',
                      "PASSPORT ID: " + passportNID + '\n',
                      "DATE OF BIRTH: " + DOB + "\n",
                      "PHONE NUMBER: " + phoneNumber + "\n",
                      "ADDRESS: " + address + "\n",
                      "CURRENCY: " + currency + '\n',
                      "CURRENT BALANCE: " + str(bal) + '\n'
                      "\nfirst time login: " + first_time_login + "\n"
                      
                      "\n----------TRANSACTION HISTORY-----------"]

    with open('CUSTOMERINFO_' + accountName + ".txt", "w") as file:
        for i in accountDetails:
            file.write(i)
    return accountDetails


def loginPage():
    print("\n\n---LOGIN PAGE---\n")
    while True:

        # [Login or create account]

        # prompt user
        print("Please login to continue... ")
        usernameInput = input("USERNAME: ")
        passwordInput = input("PASSWORD: ")

        # check if the account exists. if it doesn't raise error
        try:
            file = open('CUSTOMERINFO_' + usernameInput + ".txt", "r")
            accountDetails = file.readlines()

            # check if password matches
            if passwordInput == accountDetails[0].strip('\nPASSWORD: '):
                print("\n\n ~Successfully logged in!~")
                return usernameInput

            # if it doesn't, raise error
            else:
                raise NameError()
        except:
            print("\nSorry, your credentials are invalid.")


def mainMenu(account, details):
    mainMenuOptions = {
        '1': "Deposit",
        '2': "Withdrawal",
        '3': "Generate Account Report",
        '4': "Settings",
        '5': "Support",
        '6': "Logout"
    }

    print("\n\n---MAIN MENU PAGE---\n")
    print("Welcome, " + account + ". How may we help you?\n")

    # spits out all account details
    for i in details[1:10]:
        print(i.strip("\n"))
    print()

    while True:
        # prints out the list of options
        for i in mainMenuOptions:
            print(i + ". " + mainMenuOptions[i])
        print()

        # prompt user
        choice = input("Please select from the menu: ")

        # validation check
        try:
            if choice in mainMenuOptions:
                return choice
            else:
                raise ValueError()
        except:
            print("\nThat choice is invalid. Please try again. ")


def depositPage(currency, bal):
    while True:
        print("\n\n---DEPOSIT PAGE---\n")

        # show current balance
        print("Current Balance: " + str(bal) + ' ' + currency)

        # prompt user for value to deposit
        while True:
            choice = '0'
            while True:
                try:
                    choice = input("\nHow much would you like to deposit?\nPlease enter a value: ")
                    if choice == goback:
                        print("\nGoing back to main menu...")
                        return bal
                    intchoice = int(choice)
                    if intchoice <= 0:
                        print("\nThat value is below zero. Please try again")
                        break
                    else:
                        depositValue = choice
                except:
                    print("\nThat value is invalid. Please try again")
                    break

                while True:
                    choice = input("\nConfirm the deposit (y/n): ")
                    if choice == accept:
                        # go and add balance
                        bal += int(depositValue)
                        print("\nDEPOSIT CONFIRMED.")
                        print("Current Balance: " + str(bal) + ' ' + currency)
                        # [the transaction history gets recorded with a function ehre]
                        # NEWTRANSACTION(DEPOSIT)
                        return bal
                    elif choice == cancel or choice == goback:
                        depositValue = 0
                        print("\nCancelled deposit.")
                        break
                    else:
                        # invalid choice
                        print("\nThat choice is invalid. Please try again. ")


def withdrawalPage(currency, bal, minBalance):
    while True:
        print("\n\n---WITHDRAWAL PAGE---\n")

        # show current balance
        print("Current Balance: " + str(bal) + ' ' + currency)

        # prompt user for value to deposit
        while True:
            choice = '0'
            while True:
                try:
                    choice = input("\nHow much would you like to withdraw?\nPlease enter a value: ")
                    if choice == goback:
                        print("\nGoing back to main menu...")
                        return bal
                    intchoice = int(choice)
                    if intchoice <= 0:
                        print("\nThat value is below zero. Please try again")
                        break
                    if (bal - intchoice) < minBalance:
                        print("\nYou cannot withdraw more than the minimum balance. Please try again")
                        break
                    else:
                        withdrawValue = choice
                except:
                    print("\nThat value is invalid. Please try again")
                    break

                while True:
                    choice = input("\nConfirm the withdrawal (y/n): ")
                    if choice == accept:
                        # go and add balance
                        bal -= int(withdrawValue)
                        print("\nWITHDRAWAL CONFIRMED.")
                        print("Current Balance: " + str(bal) + ' ' + currency)
                        # [the transaction history part goes here too]
                        return bal
                    elif choice == cancel or choice == goback:
                        withdrawValue = 0
                        print("\nCancelled withdrawal.")
                        break
                    else:
                        # invalid choice
                        print("\nThat choice is invalid. Please try again. ")


def reportPage():
    # ur stuff goes here
    print("[ur stuff goes here]")


def settingsPage():
    settingsMenuOptions = {
        '1': "Change Password",
        '2': "somethinf esle???"
    }

    print("\n\n---SETTINGS PAGE---\n")

    while True:

        # prints out the list of options
        for i in settingsMenuOptions:
            print(i + ". " + settingsMenuOptions[i])
        print()

        # prompt user
        choice = input("Please select from the menu: ")

        # validation check
        try:
            if choice in settingsMenuOptions:
                return choice
            else:
                raise ValueError()
        except:
            print("\nThat choice is invalid. Please try again. ")

##Change Password Function##
def change_pass(nid):
    # Open account file
    with open("Account - " + nid + ".txt", "r") as customer:
        data = customer.readlines()
    data[-1] = "1"
    # Changing password, user not allowed to exit until password changed
    while data[-1] != "0":
        reset = input("Enter new password: ")
        confirm = input("Confirm password: ")
        if reset == confirm:
            data[1] = reset
            data[-1] = "0"
            print("Password was successfully changed!")
        else:
            print("Passwords do not match, try again")
    # Writing back updated password and first time login status to account file
    with open("Account - " + nid + ".txt", "w") as customer:
        for x in data:
            customer.write(x)


"""
    admin functions:
    ChangeCustomerDetails()
    OpenAcc()
    Statement(username)
    [check for admin before customer]

    superuser functions:

"""


def supportPage():
    print("that goeshere")


def OpenAcc():
    # Data processing
    with open("Applications.txt", "r") as customer:
        data = customer.readlines()
    print("\n\nAccount Approval\n")
    for z, acc in enumerate(data):
        account = acc.split("%")
        nid = account[1]
        print("Account number {}\n".format(z + 1))



        print("Name: ", account[0])
        print("NID: ", account[1])
        print("D.O.B: ", account[2])
        print("Current Address: ", account[3])
        print("Phone: ", account[4])
        print("Account type: ", account[5])
        print("Currency: ", account[6])
        print("Deposit: " + account[6] + account[7])
        process = input("\nApprove this application? (Yes/No): ")

        while process.strip() != "Yes" and process.strip() != "No":
            process = input("Invalid input, enter only (Yes/No): ")

        if process == "Yes":
            # Generate account number
            now = datetime.datetime.today()
            acc_no = str(now.day // 9) + str(now.hour // 9) + str(now.minute // 9) + str(now.second // 9) + str(
                now.microsecond // 9) + str(now.microsecond // 999)

            # Generate default password
            password = ""
            for x, num in enumerate(acc_no):
                if x % 2 == 0:
                    password += chr(int(num) % 26 + 64)
                else:
                    password += chr(int(num) % 26 + 97)
                if x == 3:
                    password += "!"

            # Additional account setup
            first_time_login = 1  # 1 == True, 0 == False
            balance = 0
            balance += int(account[7])

            # Approved account text file creation
            overwrite(account[0],password,acc_no,account[5],account[6],account[1],balance)
    return


# MAIN FLOW
def main():
    while True:
        # 1. show introduction screen
        print("\n\n[bank introduction screen]")

        # 2. show login page
        currentSessionAccount = loginPage()

        # if currentSessionAccount is admin, defer to admin() function
        # if currentSessionAccount is superuser, defer to superuser() function
        # if currentSessionAccount is customer, defer to customer() function

        # 3. display main menu and its options. prompt user to select.
        # all main menu options

        while True:

            # reads file, transfers info into array, then into variables (for better readability)
            with open('CUSTOMERINFO_' + currentSessionAccount + '.txt', 'r') as file:
                accountDetails = file.readlines()
            password = accountDetails[0].replace("PASSWORD: ", '')
            password = password.replace('\n', '')
            accountID = accountDetails[1].replace("ACCOUNT ID: ", '')
            accountID = accountID.replace('\n', '')
            accountType = accountDetails[2].replace("ACCOUNT TYPE: ", '')
            accountType = accountType.replace('\n', '')
            passportNID = accountDetails[3].replace("PASSPORT ID: ", '')
            passportNID = passportNID.replace('\n', '')
            DOB = accountDetails[4].replace("DATE OF BIRTH: ", '')
            DOB = DOB.replace('\n', '')
            phoneNumber = accountDetails[5].replace("PHONE NUMBER: ", '')
            phoneNumber = phoneNumber.replace('\n', '')
            address = accountDetails[6].replace("ADDRESS: ", '')
            address = address.replace('\n', '')
            currency = accountDetails[7].replace("CURRENCY: ", '')
            currency = currency.replace('\n', '')
            balance = int(accountDetails[8].replace("CURRENT BALANCE: ", ''))
            first_time_login = accountDetails[10].replace("first time login: ", '')
            first_time_login = first_time_login.replace('\n', '')

            if accountType == 'Current':
                minBalance = 100
            else:
                minBalance = 500

            # launch main menu
            choice = mainMenu(currentSessionAccount, accountDetails)

            # interpreting user choice
            match choice:
                # DEPOSIT PAGE
                case '1':
                    accountDetails = overwrite(currentSessionAccount, password, accountID, accountType,
                                               passportNID, DOB, phoneNumber, address, currency, depositPage(currency, balance), first_time_login)
                # WITHDRAWAL PAGE
                case '2':
                    accountDetails = overwrite(currentSessionAccount, password, accountID, accountType,
                                               passportNID, DOB, phoneNumber, address, currency, withdrawalPage(currency, balance, minBalance), first_time_login)
                #  GENERATE STATEMENTS
                case '3':
                    OpenAcc()

                case '4':
                    settingsPage()
                case '5':
                    supportPage()
                case '6':
                    break


if __name__ == "__main__":
    main()