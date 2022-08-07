#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# PMoy, 2022-Aug-04, Changed to dicts from lists
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dicts to hold data
dictRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        lstTbl.clear() # Clear table, otherwise repeated loads will duplicate
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',') 
            dictRow = {'id': int(lstRow[0]), 'cd': lstRow[1], 'artist': lstRow[2] }
            lstTbl.append(dictRow)
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (list of dicts) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {'id': intID, 'cd': strTitle, 'artist': strArtist }
        lstTbl.append(dictRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:  
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {'id': intID, 'cd': strTitle, 'artist': strArtist }
        for row in lstTbl:
            if row == dictRow:
                lstTbl.remove(row)
                break
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        # Since we can load data, allow both overwrite and append modes
        saveMode = None
        while True:
            print('[r] Replace file contents\n[a] Append to file contents\n[c] Cancel')
            saveMode = input('r, a, or c: ').lower()  # convert choice to lower case at time of input
            print()
            if saveMode == 'c' or saveMode == 'r' or saveMode == 'a':
                if saveMode == 'r':
                    saveMode = 'w' # Map user choice letter to correct mode
                break
        if saveMode != 'c': # Only save to file if cancel not selected    
            objFile = open(strFileName, saveMode)
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

