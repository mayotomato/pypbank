import datetime

# controls:
accept = 'y'
cancel = 'n'
goback = 'q'

current = {
    "MYR":"100",
    "USD":"20",
    "EUR":"100",
}

savings = {
    "MYR":"500",
    "USD":"150",
    "EUR":"100",
}

##Registration form and account opening##
def Registeration():
    data = []
    # Personal details
    print("Welcome to Bank of Feline registration")
    print("Personal Information")
    name = input("Name: ")
    data.append(name)
    nid = input("NID/Passport No.: ")
    data.append(nid)
    # Check valid date
    while True:
        dob = input("Date of Birth (dd/mm/yyyy): ")
        try:
            datetime.datetime.strptime(dob, "%d/%m/%Y")
        except:
            print("Invalid date, try again")
            continue
        break
    data.append(dob)
    address = input("Current Address: ")
    data.append(address)
    phone = input("Phone number: ")
    data.append(phone)

    # Account details
    print("\nAccount information")
    #username
    while True:
        with open("Usernames.txt", "r") as file:
            files = file.readlines()
            for x in files:
                z = x.strip("\n")
                files.index(x) = z
            username = input("Choose a username: ")

            print(files)
            if username in files:
                print("Username already exists choose a new username")
                continue
            else:
                with open("Usernames.txt", "a") as file:
                    file.write(username + "\n")
                break

    data.append(username)
    # Check correct account type entered
    while True:
        acc_type = input("Account type (Savings/Current): ").capitalize()
        if acc_type == "Savings":
            type = savings
            break
        elif acc_type == "Current":
            type = current
            break
        else:
            print("Invalid account type chosen, please choose (Savings/Current): ")
    data.append(acc_type)
    # Check correct currency entered
    while True:
        currency = input("Currency (MYR/USD/EUR): ").upper().strip()
        if currency == "MYR" or currency == "USD" or currency == "EUR":
            break
        else:
            print("Invalid currency chosen, please choose (MYR/USD/EUR): ")
    data.append(currency)
    # Check correct deposit entered
    while True:
        deposit = int(input("Deposit (Must be at least {} {} ): ".format(type[currency],currency)))
        if deposit >= int(type[currency]):
            break
        else:
            print("Insufficient deposit (Must be at least {} {} ): ".format(type[currency], currency))
    data.append(str(deposit))

    # Application text file creation
    with open("Applications.txt", "a") as customer:
        customer.write(",".join(data))

    return


##Account Creation function##

def OpenAcc():
    # Data processing
    with open("Applications.txt", "r") as customer:
        data = customer.readlines()
    print("\n\nAccount Approval\n")
    for z, acc in enumerate(data):
        account = acc.split("%")

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

            # Generate default passord
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
            with open("Account - " + nid + ".txt", "w") as customer:
                customer.write(
                    acc_no + "\n" + password + "\n" + account[0] + "\n" + account[1] + "\n" + account[2] + "\n" +
                    account[3] + "\n" + account[4] + "\n" + account[5] + "\n" + account[6] + "\n" + str(
                        balance) + "\n" + str(first_time_login) + "\n")

            # Delete line
            with open("Applications.txt", "r") as file:
                lines = file.readlines()
            with open("Applications.txt", "w") as file:
                for line in lines:
                    if line != acc:
                        file.write(line)
        elif process == "No":

            # Delete line
            with open("Applications.txt", "r") as file:
                lines = file.readlines()
            with open("Applications.txt", "w") as file:
                for line in lines:
                    if line != acc:
                        file.write(line)
    return


##Account report generator function##

def Statement(nid):
    try:
        # Opening transactions file
        with open("Transactions - " + nid + ".txt", "r") as customer:
            data = customer.readlines()
    except:
        # Invalid NID returned if admin user searched wrong NID. Regular users will have own NID entered automatically into function
        return "Invalid NID"

    # Statement information
    start_date = input("Starting date (dd/mm/yyyy: ")
    end_date = input("Ending date (dd/mm/yyyy: ")

    # Empty string used to signify no limit
    if start_date == "" and end_date == "":
        return "\n\n".join(data)

    # No limit on start date but specific end date with validation
    if start_date == "" and (end_date in data):
        end_index = data.index(end_date)
        report = data[:end_index]
        return "\n\n".join(report)
    else:
        return "Invalid ending date"

    # Specific start date but no limit on end date with validation
    if (start_date in data) and end_date == "":
        start_index = data.index(start_date)
        report = data[start_index:]
        return "\n\n".join(report)
    else:
        return "Invalid starting date"

    # Checking both start date and end date
    try:
        start_index = data.index(start_date)
    except:
        return "Invalid starting date"
    try:
        end_index = data.index(end_date)
    except:
        return "Invalid ending date"

    # Return statement within specified range
    report = data[start_index:end_index]
    return "\n\n".join(report)


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

# End

##Deposit funciton##

def depositPage(currency, bal):
    while True:
        print("\n\n---DEPOSIT PAGE---\n")

        # show current balance
        print("Current Balance: " + str(bal) + ' ' + currency)

        # prompt user for value to deposit
        while True:
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

                        # NEWTRANSACTION(DEPOSIT)
                        return bal
                    elif choice == cancel or choice == goback:
                        depositValue = 0
                        print("\nCancelled deposit.")
                        break
                    else:
                        # invalid choice
                        print("\nThat choice is invalid. Please try again. ")
