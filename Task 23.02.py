#By Hasan Mustafabayli
#Task 23.02
#Part2

def InsertionSort(List):
    for i in range(1, len(List)):
        ExistingValue = List[i]
        ExistingPosition = i
        while ExistingPosition > 0 and List[ExistingPosition-1] > ExistingValue:
            List[ExistingPosition] = List[ExistingPosition-1]
            ExistingPosition -= 1
        List[ExistingPosition] = ExistingValue
    print(List)

    
List = []
List.append(53)
List.append(21)
List.append(60)
List.append(18)
List.append(42)
List.append(19)

InsertionSort(List)