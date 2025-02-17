
#ADD TASK
TASKS = []
ID = 1
def TASKADD():
    global ID
    TASK = input("ENTER TASK: ")
    TASKS.append({"ID":ID,"TASK":TASK,"STATUS":"PENDING"})
    print(f"TASK{ID} ADDED.")
    ID +=1

def TASKVIEW():
    if not TASKS:
        print("NO TASKS ADDED")
    else:
        for TASK in TASKS:
            print(f"[{TASK['ID']}]{TASK['TASK']} - {TASK['STATUS']}")

def TASKUPDATE():
    NUM = int(input("ENTER WHICH TASK ID TO UPDATE: "))
    for TASK in TASKS:
        if TASK["ID"] == NUM:
            NEWTASK = input("ENTER NEW TASK: ")
            TASK["TASK"] = NEWTASK
            print("TASK UPDATED.")
            return
    print("TASK NOT FOUND.")

def TASKREMOVE():
    NUM = int(input("ENTER WHICH TASK ID TO REMOVE: "))
    for TASK in TASKS:
        if TASK["ID"] == NUM:
            TASKS.remove(TASK)
            print("TASK REMOVED.")
            return
    print("TASK NOT FOUND.")

def COMPLETETASKS():
    NUM = int(input("ENTER WHICH TASK ID TO MARK AS COMPLETE: "))
    for TASK in TASKS:
        if TASK["ID"] == NUM:
            TASK["STATUS"] = "COMPLETED"
            print("TASK COMPLETED.")
            return
    print("TASK NOT FOUND.")

while True:
    print("1. ADD TASK\n2.VIEW TASKS\n3. UPDATE TASKS\n4. REMOVE TASK\n5. COMPLETED TASKS\n6. EXIT")
    OPTION = input("ENTER OPTION:")
    if OPTION == "1":
        TASKADD()
    elif OPTION == "2":
        TASKVIEW()
    elif OPTION == "3":
        TASKUPDATE()
    elif OPTION == "4":
        TASKREMOVE()
    elif OPTION == "5":
        COMPLETETASKS()
    elif OPTION == "6":
        print("EXITING...")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN.")








