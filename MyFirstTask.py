#BANK ATM
ACCOUNT_NO = 1
BALANCE = 3050
PIN = 1234
#INSERT CARD
def INSERT_CARD():
    print("INSERT YOUR CARD")
    print("A. INSERT CARD  | B.LEAVE  (TYPE 'A' OR 'B')")
    RESPONSE=input(">>")
    if RESPONSE=="A":
        INSERT_CARD = True
        print("CARD INSERTED SUCCESSFULLY")
    elif RESPONSE=="B" :
        print("THANK YOU FOR BANKING WITH US")
        exit()
#PIN
def PIN():
    INPUT_PIN= int(input("INSERT PIN:"))
    while INPUT_PIN != PIN:
        print("INCORRECT PIN")
        INPUT_PIN= int(input("RETRY PIN:"))
    else:
        print("PIN SUCCESSFUL")
# CHECK BALANCE
def CHECK_BALANCE():
    print("YOUR CURRENT BALANCE IS: ",BALANCE)

#DEPOSIT MONEY
def DEPOSIT():
    DEPOSIT = int(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT: "))
    NEWBALANCE = BALANCE + DEPOSIT
    print("TRANSACTION SUCCESSFUL")

#CASH WITHDRAWAL
def WITHDRAW():
    WITHDRAW= int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW: "))
    if WITHDRAW <= BALANCE:
        print("TRANSACTION SUCCESSFUL")
    else:
        print("TRANSACTION FAILED")
    NEWBALANCE= BALANCE-WITHDRAW
    if NEWBALANCE<=0:
        print("REMAINING BALANCE IS:",BALANCE)
    else:
        print("NEW BALANCE IS:", NEWBALANCE)
WITHDRAW= int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW: "))

print("WELCOME TO BANK ATM")
INSERT_CARD()
PIN()
while True:
    print("1. CHECK BALANCE\n2.DEPOSIT\n3. WITHDRAW\n4.EXIT")
    OPTION = input("ENTER OPTION:")
    if OPTION == "1":
        CHECK_BALANCE()
    elif OPTION == "2":
        DEPOSIT()
    elif OPTION == "3":
        WITHDRAW()
    elif OPTION == "4":
        print("THANK YOU FOR BANKING WITH US")
        exit()

