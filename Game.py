grid1 = [0,0,0,0,0,0,0]
grid2 = [0,0,0,0,0,0,0]
grid3 = [0,0,0,0,0,0,0]
grid4 = [0,0,0,0,0,0,0]
grid5 = [0,0,0,0,0,0,0]
grid6 = [0,0,0,0,0,0,0]

lines = [grid1,grid2,grid3,grid4,grid5,grid6]

check = []

user = 1

class fullSlot_error (Exception):
    pass
def Winner_def():
    print ("player "+str(user)+" has won")
    

def lines_def():
    print (grid6,"\n",grid5,"\n",grid4,"\n",grid3,"\n",grid2,"\n", grid1)

def user_def():
    global user
    if user < 2:
        user = 2
    else:
        user = 1
    return user

def Full_def():
   while True:
        try:
            if grid4[userInput -1] != 0:
                raise fullSlot_error
            else:
                break
        except fullSlot_error:
            print ("slot is full try again")
            confirm_def()

def confirm_def():
    looop= True
    while looop== True:
        try:
            global userInput
            userInput = int(input("\ninput the number of the position "+str(user)+"(1,7)\n"))
            if userInput < 8 and 0 < userInput:   
                looop = False
            else:
                print ("invalid int")
        except ValueError:
            print ("invalid input")

def placement_def():
    counter = 0
    for i in range (0,6):
        Full_def()
        if (lines[i][userInput -1] == 0):
            lines [i][userInput - 1] = int(user)
            lines_def()
            break


def check_def():
    global loop
    global check
    for i in range(0,6):
        for a in range(0,6):
            check.append(lines[i][a])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            Winner_def()
            loop = False
            return loop
            break
        else:
            check = []
    for i in range(0,6):
        for a in range(0,6):
            check.append(lines[a][i])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            Winner_def()
            loop = False
            return loop
            break
        else:
            check = []

def checkEmpty_def():
    global check
    for i in range (0,6):
        for a in range (0,6):
            check.append(lines[i][a])
    if 0 not in check:
        print ("full")

def checks_def():
    check_def()
    checkEmpty_def()
    diagcheck_def()

def diagcheck_def():
    global loop
    global check
    check = []
    diag = 0
    for i in range (0,6):
        check.append (lines[diag][diag])
        diag = diag +1
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            Winner_def()
            loop = False
            return loop
            break
    check = []
    diag = 3
    diag2 = 0
    for i in range (0,6):
        check.append (lines[diag][diag2])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            Winner_def()
            loop = False
            return loop
            break


loop = True

while loop == True:
    check_def()
    confirm_def()
    placement_def()
    checks_def()
    if loop == False:
        break
    user_def()