USER_A = {"NAME": "ZENITH BANK",    
    "LOCATION": "LAGOS, NIGERIA",  
    "ACCOUNTS": {  
        "001": {"HOLDER": "JOHN DOE", "BALANCE": 5000.00, "TYPE": "SAVINGS", "PIN": 1234},  
        "002": {"HOLDER": "JANE SMITH", "BALANCE": 12000.50, "TYPE": "CHECKING","PIN":2345 }  }
}
USER_B = {"NAME": "FIRST BANK",    
    "LOCATION": "ABUJA, NIGERIA",  
    "ACCOUNTS": {  
        "001": {"HOLDER": "JACK DeVON", "BALANCE": 53000.00, "TYPE": "SAVINGS", "PIN": 1234},  
        "002": {"HOLDER": "JADE RUSHER", "BALANCE": 22000.50, "TYPE": "CHECKING","PIN": 3456}  }
}
#ADDACCOUNT
def ADDACCOUNT(BANK):
    USERBANK = BANK["NAME"]
    print(f"ADD ACCOUNT TO {USERBANK}")
    HOLDER = input("ENTER ACCOUNT HOLDER: ").upper()
    print("ENTER ACCOUNT TYPE: \n1.SAVINGS\n2.CHECKING")
    TYPE = input(">>").upper()
    if TYPE == "1":
        TYPE = "SAVINGS"
    elif TYPE == "2":
        TYPE = "CHECKING"
    if TYPE not in ["SAVINGS", "CHECKING"]:
        print("INVALID ACCOUNT TYPE")
        return ADDACCOUNT(BANK)
    PIN = int(input("ENTER ACCOUNT PIN: "))
    DEPOSIT = float(input("ENTER INITIAL DEPOSIT: "))
    BALANCE = DEPOSIT if DEPOSIT > 0 else 0
    ACC_NO = str(len(BANK["ACCOUNTS"]) + 1).zfill(3)
    BANK["ACCOUNTS"][ACC_NO] = {"HOLDER": HOLDER, "BALANCE": BALANCE, "TYPE": TYPE, "PIN": PIN}
    print("ACCOUNT ADDED SUCCESSFULLY")
    print(f"ACCOUNT NUMBER: {ACC_NO}")


#INSERT CARD
def INSERT_CARD():
    print("INSERT YOUR CARD")
    print("A. INSERT CARD  | B.LEAVE  (TYPE 'A' OR 'B')")
    RESPONSE=input(">>").upper()
    if RESPONSE=="A":
        print("CARD INSERTED SUCCESSFULLY")
        return True
    elif RESPONSE=="B" :
        print("THANK YOU FOR BANKING WITH US")
        exit()
    else:
        print("INVALID OPTION")
        return INSERT_CARD()

def BANK():
    print("SELECT YOUR BANK:")
    print("1. ZENITH BANK\n2. FIRST BANK")
    choice = input(">> ")
    if choice == "1":
        return USER_A
    elif choice == "2":
        return USER_B
    else:
        print("INVALID CHOICE. TRY AGAIN.")
        return BANK()
    
def ACCOUNT(BANK):
    print("SELECT ACCOUNT NUMBER:")
    for ACC_NO, DETAILS in BANK["ACCOUNTS"].items():
        print(f"{ACC_NO}. {DETAILS['HOLDER']} ({DETAILS['TYPE']})")
    
    CHOICE = input(">> ")
    if CHOICE in BANK["ACCOUNTS"]:
        return CHOICE
    else:
        print("INVALID ACCOUNT. TRY AGAIN.")
        return ACCOUNT(BANK)
#PIN
def PIN(ACCOUNT):
    ATTEMPTS = 3
    while ATTEMPTS > 0:
        INPUT_PIN= int(input("INSERT PIN:"))
        if INPUT_PIN == ACCOUNT["PIN"]:
            print("PIN SUCCESSFUL")
            return True
        else:
            ATTEMPTS -= 1
            print(f"INCORRECT PIN. {ATTEMPTS} ATTEMPTS LEFT.")
    else:
        print("TOO MANY INCORRECT ATTEMPTS. CARD BLOCKED.")
        exit()

# CHECK BALANCE
def CHECK_BALANCE(ACCOUNT):
    print(f"YOUR CURRENT BALANCE IS: {ACCOUNT['BALANCE']}")

#DEPOSIT MONEY
def DEPOSIT(ACCOUNT):
    DEPOSIT = float(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT: "))
    if DEPOSIT > 0:
        ACCOUNT["BALANCE"] += DEPOSIT
        print("TRANSACTION SUCCESSFUL")
        print(f"NEW BALANCE: {ACCOUNT['BALANCE']}")

#CASH WITHDRAWAL
def WITHDRAW(ACCOUNT):
    WITHDRAW= float(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW: "))
    if WITHDRAW >0 and WITHDRAW <= ACCOUNT["BALANCE"]:
        ACCOUNT["BALANCE"] -= WITHDRAW
        print("TRANSACTION SUCCESSFUL")
        print(f"NEW BALANCE: {ACCOUNT['BALANCE']}")
    elif WITHDRAW > ACCOUNT["BALANCE"]:
        print("INSUFFICIENT FUNDS")
    else:
        print("TRANSACTION FAILED")


#TRANSFER MONEY(SAME BANK)
def SAMEBANKTRANSFER(ACCOUNT,BANK):
    RECIEVER = input("ENTER RECIEVER'S ACCOUNT NUMBER: ")
    if RECIEVER not in BANK["ACCOUNTS"]:
        print("ACCOUNT DOES NOT EXIST")
        return
    RECIEVER_ACCOUNT = BANK["ACCOUNTS"][RECIEVER]
    AMOUNT = float(input("ENTER AMOUNT: "))
    if AMOUNT > 0 and AMOUNT <= ACCOUNT["BALANCE"]:
        ACCOUNT["BALANCE"] -= AMOUNT
        RECIEVER_ACCOUNT["BALANCE"] += AMOUNT
        print("TRANSACTION SUCCESSFUL")
        print(f"NEW BALANCE: {ACCOUNT['BALANCE']}")
    elif AMOUNT > ACCOUNT["BALANCE"]:
        print("INSUFFICIENT FUNDS")
    else:
        print("TRANSACTION FAILED")

#TRANSFER MONEY(DIFFERENT BANK)
def DIFFBANKTRANSFER(ACCOUNT,SENDERBANK):
    print("SELECT BANK:")
    print("1. ZENITH BANK\n2. FIRST BANK")
    choice = input(">> ")
    if choice == "1":
        RECIEVER_BANK = USER_A if SENDERBANK == USER_B else USER_B
    elif choice == "2":
        RECIEVER_BANK = USER_B if SENDERBANK == USER_A else USER_A
    else:
        print("INVALID CHOICE. TRY AGAIN.")
        return DIFFBANKTRANSFER(ACCOUNT,SENDERBANK)
    RECIEVER = input("ENTER RECIEVER'S ACCOUNT NUMBER: ")
    if RECIEVER not in RECIEVER_BANK["ACCOUNTS"]:
        print("ACCOUNT DOES NOT EXIST")
        return
    RECIEVER_ACCOUNT = RECIEVER_BANK["ACCOUNTS"][RECIEVER]
    AMOUNT = float(input("ENTER AMOUNT: "))
    if AMOUNT > 0 and AMOUNT <= ACCOUNT["BALANCE"]:
        ACCOUNT["BALANCE"] -= AMOUNT
        RECIEVER_ACCOUNT["BALANCE"] += AMOUNT
        print("TRANSACTION SUCCESSFUL")
        print(f"NEW BALANCE: {ACCOUNT['BALANCE']}")
    elif AMOUNT > ACCOUNT["BALANCE"]:
        print("INSUFFICIENT FUNDS")
    else:
        print("TRANSACTION FAILED")
# TRANSFER MONEY
def TRANSFER_MENU(ACCOUNT, BANK):
    while True:
        print("\nTRANSFER MENU ")
        print("1. SAME BANK TRANSFER")
        print("2. INTER-BANK TRANSFER")
        print("3. BACK TO MAIN MENU")

        CHOICE = input(">> ")

        if CHOICE == "1":
            SAMEBANKTRANSFER(ACCOUNT, BANK)
        elif CHOICE == "2":
            DIFFBANKTRANSFER(ACCOUNT, BANK)
        elif CHOICE == "3":
            return
        else:
            print("INVALID OPTION. TRY AGAIN.")


#ATM
def ATM():
    print("WELCOME TO BANK ATM")
    print("1. CREATE ACCOUNT \n2. PLEASE INSERT YOUR CARD")
    OPTION = input("ENTER OPTION:")
    if OPTION == "1":
        BANK_NAME = BANK()
        ADDACCOUNT(BANK_NAME)
        return ATM()
    elif OPTION == "2":
        pass

    if not INSERT_CARD():
        return
    BANK_NAME = BANK()
    ACCOUNT_NO = ACCOUNT(BANK_NAME)
    ACCOUNT_DETAILS = BANK_NAME["ACCOUNTS"][ACCOUNT_NO]
    PIN(ACCOUNT_DETAILS)
    while True:
        print("1. CHECK BALANCE\n2. DEPOSIT\n3. WITHDRAW\n4.TRANSFER\n5.EXIT")
        OPTION = input("ENTER OPTION:")
        if OPTION == "1":
            CHECK_BALANCE(ACCOUNT_DETAILS)
        elif OPTION == "2":
            DEPOSIT(ACCOUNT_DETAILS)
        elif OPTION == "3":
            WITHDRAW(ACCOUNT_DETAILS)
        elif OPTION == "4":
            TRANSFER_MENU(ACCOUNT_DETAILS, BANK_NAME)
        elif OPTION == "5":
            print("THANK YOU FOR BANKING WITH US")
            exit()
        else:
            print("INVALID OPTION")
        
ATM()