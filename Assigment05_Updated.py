# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SSimpers,5.15.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # A string that contains the file name
objFile = None  # An object that represents a file
strData = ""    # A row of text data from the file
dicRow = {}     # A row of data separated into elements of a dictionary {Task,Priority}
lstRow = []     # A list representing a row of data
lstTable = []   # A list that acts as a 'table' of rows
strMenu = ""    # A menu of user options
strChoice = ""  # A capture of the user option selection
strInput1 = ""  # A capture of the user task name to add
strInput2 = ""  # A capture of the user task priority to add
strRemove = ""  # A capture of the user task to remove
intBreak = 0    # An integer that acts as a flag within a nested loop to initiate a break from an outer loop

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")  # open file in read mode
for row in objFile:
    lstRow = row.split(",")  # row list
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}  # row dictionary (strip \n off)
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input(" Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == "1"):
        print(" " + "="*20)  # header line
        print(" Task" + "," + "Priority")  # header text
        print(" " + "="*20)  # header line
        for dicRow in lstTable:
            print(" " + dicRow["Task"] + "," + dicRow["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == "2"):
        print(" Enter a task name and its priority...")
        strInput1 = input(" Enter task name: ")
        strInput2 = input(" Enter priority: ")
        dicRow = {"Task": strInput1, "Priority": strInput2}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == "3"):
        strRemove = input(" Enter a task name that you would like to remove or type 'c' to cancel: ")
        while (True):
            if strRemove.lower() == "c":
                break
            intBreak = 0  # reset flag
            for dicRow in lstTable:
                if strRemove.lower() == dicRow["Task"].lower():
                    lstTable.remove(dicRow)
                    intBreak = 1  # flag to break out of outer 'while' loop
            if intBreak == 1:
                break
            strRemove = input(" Task not found, enter a task name to remove or type 'c' to cancel: ")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == "4"):
        objFile = open(strFile, "w")  # open file in write mode
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print(" Data saved to file!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == "5"):
        print(" Exiting...")
        break  # and Exit the program
