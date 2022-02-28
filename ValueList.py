#By Hasan Mustafabayli
#Task 23.04
NullPointer= -1

class ListNode :

    def __init__(self) :
        self.Data = " "
        self.Pointer = NullPointer

def InitialiseList() :
     List = [ListNode() for i in range(8)]
     StartPointer = NullPointer
     FreeListPtr = 0
     for Index in range(7) :
         List[Index].Pointer = Index + 1
     List[7].Pointer = NullPointer
     return(List, StartPointer, FreeListPtr)
    
def InsertNode(List, StartPointer, FreeListPtr, NewItem) :
    if FreeListPtr != NullPointer :
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer
        PreviousNodePtr = NullPointer
        ThisNodePtr = StartPointer
        while ThisNodePtr != NullPointer and List[ThisNodePtr].Data < NewItem:
            PreviousNodePtr = ThisNodePtr
            ThisNodePtr = List[ThisNodePtr].Pointer
        if PreviousNodePtr == NullPointer :
            List[NewNodePtr].Pointer = StartPointer
            StartPointer = NewNodePtr
        else :
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr
    else :
        print("no space for more data")
    return(List, StartPointer, FreeListPtr)

def FindNode(List, StartPointer, DataItem) :
    CurrentNodePtr = StartPointer
    while CurrentNodePtr != NullPointer and List[CurrentNodePtr].Data != DataItem:
        CurrentNodePtr = List[CurrentNodePtr].Pointer
    return(CurrentNodePtr)

def DeleteNode(List, StartPointer, FreeListPtr, DataItem) :
    ThisNodePtr = StartPointer
    while ThisNodePtr != NullPointer and List[ThisNodePtr].Data != DataItem :
        PreviousNodePtr = ThisNodePtr
        ThisNodePtr = List[ThisNodePtr].Pointer
    if ThisNodePtr != NullPointer :
        if ThisNodePtr == StartPointer :
            StartPointer = List[StartPointer].Pointer
        else :
            List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer
        List[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr
    else :
        print("data does not exist in list")
    return(List, StartPointer, FreeListPtr)
def OutputAllNodes(List, StartPointer) :
    CurrentNodePtr = StartPointer
    if StartPointer == NullPointer :
        print("No data in list")
    while CurrentNodePtr != NullPointer:
        print(CurrentNodePtr, " ",List[CurrentNodePtr].Data)
        CurrentNodePtr = List[CurrentNodePtr].Pointer

def GetOption() :
    print("1: insert a value")
    print("2: delete a value")
    print("3: find a value")
    print("4: output list")
    print("5: end program")
    option = input("Enter your choice: ")
    return(option)

List, StartPointer, FreeListPtr = InitialiseList()
Option = GetOption()
while Option != "5" :
    if Option == "1" :
        Data = input("Enter the value: ")
        List, StartPointer, FreeListPtr = InsertNode(List, StartPointer, FreeListPtr, Data)
        OutputAllNodes(List, StartPointer)
    elif Option == "2" :
        Data = input("Enter the value: ")
        List, StartPointer, FreeListPtr = DeleteNode(List, StartPointer, FreeListPtr, Data)
        OutputAllNodes(List, StartPointer)
    elif Option == "3" :
        Data = input("Enter the value: ")
        CurrentNodePtr = FindNode(List, StartPointer, Data)
        if CurrentNodePtr == NullPointer :
            print("data not found")
        print(StartPointer, FreeListPtr)
        for i in range(8) :
            print(i, " ", List[i].Data, " ", List[i].Pointer)
    elif Option == "4" :
        OutputAllNodes(List, StartPointer)
    Option = GetOption()