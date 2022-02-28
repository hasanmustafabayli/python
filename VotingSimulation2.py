total = 0
count = 1
votes = 0 
names = ["Fabio", "Hasan", "Gozde", "He Heon", "Ryan"]
WinnerExists = False


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
    arr = percentage(CA, CB, CC, CD, CE, votes)
    n = len(arr)
    for i in range(n):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for z in arr:
        if z > 50.0:
            v = z

    u = -1
    DeterminingName = percentage(CA, CB, CC, CD, CE, votes)
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
                global FirstQualifier
                FirstQualifier = names[u]
                del names[u]
                break
        u = -1
        qualifier2 = arr[4]
        names2 = ["Fabio", "Hasan", "Gozde", "He Heon", "Ryan"]
        for s in DeterminingName:
            u += 1
            if qualifier2 == s:
                global SecondQualifier
                SecondQualifier = names2[u]
                break
        Qualifiers = [FirstQualifier, SecondQualifier]
        gfu = Qualifiers
        return gfu
        WinnerExists = False

for x in names:
    print(count, x)
    count += 1
ch = "yes"

CA = 0
CB = 0
CC = 0
CD = 0
CE = 0
while ch == "yes":
    votes += 1
    choice = int(input("Please input your choice: "))
    if choice == 1:
        CA += 1
    elif choice == 2:
        CB += 1
    elif choice == 3:
        CC += 1
    elif choice == 4:
        CD += 1
    elif choice == 5:
        CE += 1
    else:
        print("Invalid choice")
        votes -=1
    ch = input("Is there anybody else left to vote?:  ")
    ch = ch.lower()


percentage(CA, CB, CC, CD, CE, votes)
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
    print("The following two names earned a place in the next round:")
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