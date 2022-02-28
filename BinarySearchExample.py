#By Hasan Mustafabayli
#Binary Search

Found = False
SearchFailed = False
First = 1
List = [2, 3, 4, 10, 40]
Last = 5
SearchItem = int(input("Please input the item that you are looking for: "))

while not Found and not SearchFailed:
    Middle = (First + Last)//2
    if SearchItem == List[Middle]:
        Found = True
    elif First >= Last:
        SearchFailed = True
    elif List[Middle] > SearchItem:
        Last = Middle - 1
    else:
        First = Middle + 1

if Found == True:
    print(Middle)
else:
    print("Item not present in array")
