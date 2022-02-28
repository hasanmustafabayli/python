def InitialiseBoard():
    global Board
    Board=[[" ◌"for row in range(7)] for column in range(6)]
    print("                                                ---------------")
    for x in Board:
        print("                                               |", *x," |", sep='')
    print("                                                ---------------\n                                                 1 2 3 4 5 6 7")

def checkAndPlace(symbol):
    variable = symbol
    columnUser = int(input("\n                                          Which column do you choose?"))
    print ("\n")
    global boardFull
    boardFull = False
    if Board[0][0]!=" ◌" and Board[0][1]!=" ◌" and Board[0][2]!=" ◌" and Board[0][3]!=" ◌" and Board[0][4]!=" ◌" and Board[0][5]!=" ◌" and Board[0][6]!=" ◌":
        boardFull = True
        print ("                                        \nIt's a tie")
        print ("\n")
    if boardFull == False:
        while columnUser<1 or columnUser>7 or Board[0][columnUser-1]!=" ◌":    
            columnUser =int(input("\n                                       This column is full or invalid --> "))
            print("\n")
        i = 5
        while Board[i][columnUser-1] != " ◌":
            i = i-1
        AvailableRow = i
        Board[AvailableRow][columnUser-1]= variable
        print("                                                ---------------")
        for x in Board:
            print("                                               |", *x," |", sep='')
        print("                                                ---------------\n                                                 1 2 3 4 5 6 7")
    

def checkWinRows4(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
    for countRow in range (0,6):
        for cellIndex in range (0,4):
            if Board[countRow][cellIndex] == ThisPlay and Board[countRow][cellIndex+1] == ThisPlay and Board[countRow][cellIndex+2] == ThisPlay and Board[countRow][cellIndex+3] == ThisPlay:
                global winner
                winner = True     
def checkWinColumns4(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
    for countColumn in range (0,7):
        for cellIndex in range (0,3):
            if Board[cellIndex][countColumn] == ThisPlay and Board[cellIndex+1][countColumn] == ThisPlay and Board[cellIndex+2][countColumn] == ThisPlay and Board[cellIndex+3][countColumn] == ThisPlay:
                global winner
                winner = True      
def checkWinDiagonal4(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
            #positive gradient#
    for x in range(3, 6):
        for y in range(0, 4):
            if Board[x][y] == ThisPlay and Board[x-1][y+1] == ThisPlay and Board[x-2][y+2] == ThisPlay and Board[x-3][y+3] == ThisPlay:
                global winner
                winner = True
                
            #negative gradeint#
    for x in range(3, 6):
        for y in range(3, 7):
            if Board[x][y] == ThisPlay and Board[x-1][y-1] == ThisPlay and Board[x-2][y-2] == ThisPlay and Board[x-3][y-3] == ThisPlay:
                winner = True

def checkWinRows3(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
    for countRow in range (0,6):
        for cellIndex in range (0,4):
            if Board[countRow][cellIndex] == ThisPlay and Board[countRow][cellIndex+1] == ThisPlay and Board[countRow][cellIndex+2] == ThisPlay:
                global winner
                winner = True     
def checkWinColumns3(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
    for countColumn in range (0,7):
        for cellIndex in range (0,3):
            if Board[cellIndex][countColumn] == ThisPlay and Board[cellIndex+1][countColumn] == ThisPlay and Board[cellIndex+2][countColumn] == ThisPlay:
                global winner
                winner = True      
def checkWinDiagonal3(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
            #positive gradient#
    for x in range(3, 6):
        for y in range(0, 4):
            if Board[x][y] == ThisPlay and Board[x-1][y+1] == ThisPlay and Board[x-2][y+2] == ThisPlay:
                global winner
                winner = True
                
            #negative gradeint#
    for x in range(3, 6):
        for y in range(3, 7):
            if Board[x][y] == ThisPlay and Board[x-1][y-1] == ThisPlay and Board[x-2][y-2] == ThisPlay:
                winner = True
                
def checkWinRows5(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
    for countRow in range (0,6):
        for cellIndex in range (0,4):
            if Board[countRow][cellIndex] == ThisPlay and Board[countRow][cellIndex+1] == ThisPlay and Board[countRow][cellIndex+2] == ThisPlay and Board[countRow][cellIndex+3] == ThisPlay and Board[countRow][cellIndex+4] == ThisPlay:
                global winner
                winner = True     
def checkWinColumns5(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
    for countColumn in range (0,7):
        for cellIndex in range (0,3):
            if Board[cellIndex][countColumn] == ThisPlay and Board[cellIndex+1][countColumn] == ThisPlay and Board[cellIndex+2][countColumn] == ThisPlay and Board[cellIndex+3][countColumn] == ThisPlay and Board[cellIndex+4][countColumn] == ThisPlay:
                global winner
                winner = True      
def checkWinDiagonal5(ThisPlay):
    global player
    if ThisPlay == " ●":
        player = "Player 1"
    else:
        player = "Player 2"
            #positive gradient#
    for x in range(3, 6):
        for y in range(0, 4):
            if Board[x][y] == ThisPlay and Board[x-1][y+1] == ThisPlay and Board[x-2][y+2] == ThisPlay and Board[x-3][y+3] == ThisPlay and Board[x-4][y+4] == ThisPlay:
                global winner
                winner = True
                
            #negative gradeint#
    for x in range(3, 6):
        for y in range(3, 7):
            if Board[x][y] == ThisPlay and Board[x-1][y-1] == ThisPlay and Board[x-2][y-2] == ThisPlay and Board[x-3][y-3] == ThisPlay and Board[x-4][y-4] == ThisPlay:
                winner = True
                
                

                   
    
print("""\n
   ░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗░█████╗░████████╗  ░░██╗██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
   ██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗╚══██╔══╝  ░██╔╝██║  ██╔════╝░██╔══██╗████╗░████║██╔════╝
   ██║░░╚═╝██║░░██║██╔██╗██║██╔██╗██║█████╗░░██║░░╚═╝░░░██║░░░  ██╔╝░██║  ██║░░██╗░███████║██╔████╔██║█████╗░░
   ██║░░██╗██║░░██║██║╚████║██║╚████║██╔══╝░░██║░░██╗░░░██║░░░  ███████║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
   ╚█████╔╝╚█████╔╝██║░╚███║██║░╚███║███████╗╚█████╔╝░░░██║░░░  ╚════██║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
   ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝░╚════╝░░░░╚═╝░░░  ░░░░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")
print("""\n \n")
                          The rules of the game are simple; just connect your tiles\n
                                    Connect3 on easy 4 on medium 5 on hard\n
                       Just remember to only press numbers on your keyboard, NO LETTERS!\n\n""")

winner = False
print("""                                               CHOOSE DIFFICULTY\n
                                                    1) Easy\n
                                                   2) Medium\n
                                                    3) Hard\n""")
difficulty = str(input("                                            Select Difficulty here -->"))
print("\n")
                                                       
InitialiseBoard()


if difficulty == "1":
    while winner == False:
        checkAndPlace(" ●")
        if boardFull == False:
            checkWinRows3(" ●")
            if winner == False:  
                checkWinColumns3(" ●")
                if winner == False:
                    checkWinDiagonal3(" ●")
                    if winner == False:
                            checkAndPlace(" ○")
                            if boardFull == False:
                                checkWinRows3(" ○")
                                if winner == False:
                                        checkWinColumns3(" ○")
                                        if winner == False:
                                                checkWinDiagonal3(" ○")
    print("\n                                             The winner is", player, "\n")
elif difficulty == "2":
    while winner == False:
        checkAndPlace(" ●")
        if boardFull == False:
            checkWinRows4(" ●")
            if winner == False:  
                checkWinColumns4(" ●")
                if winner == False:
                    checkWinDiagonal4(" ●")
                    if winner == False:
                            checkAndPlace(" ○")
                            if boardFull == False:
                                checkWinRows4(" ○")
                                if winner == False:
                                        checkWinColumns4(" ○")
                                        if winner == False:
                                                checkWinDiagonal4(" ○")
    print("\n                                             The winner is", player, "\n")

elif difficulty == "3":
    while winner == False:
        checkAndPlace(" ●")
        if boardFull == False:
            checkWinRows5(" ●")
            if winner == False:  
                checkWinColumns5(" ●")
                if winner == False:
                    checkWinDiagonal5(" ●")
                    if winner == False:
                            checkAndPlace(" ○")
                            if boardFull == False:
                                checkWinRows5(" ○")
                                if winner == False:
                                        checkWinColumns5(" ○")
                                        if winner == False:
                                                checkWinDiagonal5(" ○")
    print("\n                                             The winner is", player, "\n")
