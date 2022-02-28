total = 0
count = 1
numvotes = 0 
names = ["Fabio", "Hasan", "Gozde", "He Heon", "Ryan"]


def percentage(a, b, c, d, e,numvotes):
    apercent= a/numvotes * 100
    bpercent= b/numvotes * 100
    cpercent= c/numvotes * 100
    dpercent= d/numvotes * 100
    epercent= e/numvotes * 100
    percentages = [apercent, bpercent, cpercent, dpercent, epercent]
    return percentages

def BubbleSort():
    v = 0
    arr = percentage(a,b,c,d,e,numvotes)
    n = len(arr)
    for i in range(n):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for z in arr:
        if z > 50.0:
            v = z

    u = -1
    DeterminingName = percentage(a,b,c,d,e,numvotes)
    if v > 50:
        for i in DeterminingName:
            u += 1
            if v == i:
                print("The winner is", names[u])
                global WinnerExists
                WinnerExists = True
    else:
     qualifier1 = arr[3]
     qualifier2 = arr[4]
     u = -1
     for i in DeterminingName:
        u += 1
        if qualifier1 == i:
            FirstQualifier = names[u]
            del names[u]
            break
    
    u = -1
    qualifier2 = arr[4]
    names2 = ["Fabio", "Hasan", "Gozde", "He Heon", "Ryan"]
    for s in DeterminingName:
        u += 1
        if qualifier2 == s:
            SecondQualifier = names2[u]
            break
    Qualifiers = [FirstQualifier, SecondQualifier]
    print("The first qualifier is:", FirstQualifier, ".The second qualifier is:",SecondQualifier)
    print("The qualifiers for the next round have the following votes", qualifier1,"and",
    qualifier2)
    WinnerExists = False
    return Qualifiers

for x in names:
    print(count, x)
    count += 1
ch = "yes"

a = 0
b = 0
c = 0
d = 0
e = 0
while ch == "yes":
    numvotes += 1
    choice = int(input("Please input your choice: "))
    if choice == 1:
        a += 1
    elif choice == 2:
        b += 1
    elif choice == 3:
        c += 1
    elif choice == 4:
        d += 1
    elif choice == 5:
        e += 1
    else:
        print("Invalid choice")
        numvotes -=1
    ch = input("Is there anybody else left to vote?:  ")
    ch = ch.lower()


percentage(a, b, c, d, e, numvotes)
BubbleSort()

def SecondVoteCalculation(Fqualifier, Squalifier, votesnum):
    Fresult = Fqualifier/votesnum * 100
    Sresult = Squalifier/votesnum * 100
    Qualifiers = BubbleSort()
    w = 0
    if Fresult > Sresult:
        for p in Qualifiers:
            print("The winner is", Qualifiers[w])
    else:
        for p in Qualifiers:
            print("The winner is", Qualifiers[w+1])

if WinnerExists == False:
    Fqualifier = 0
    Squalifier = 0
    count2 = 1
    votesnum = 0
    co = "yes"
    qualifiers = BubbleSort()
    for m in qualifiers:
        print(count2, m)
        count2 += 1
    while co == "yes":
        votesnum += 1
        choi = int(input("Please input your choice: "))
        if choi == 1:
            Fqualifier += 1
        elif choi == 2:
            Squalifier += 1
        else:
            print("Invalid choice")
            votesnum -=1
        co = input("Is there anybody else left to vote?:  ")
        co = co.lower()
    if co == "no":
        if (votesnum % 2) == 0:
            choi = int(input("""In order to determine the winner you need to enter one
            more vote.Please input your choice: """))
            SecondVoteCalculation(Fqualifier, Squalifier, votesnum)
        else:
            SecondVoteCalculation(Fqualifier, Squalifier, votesnum)

