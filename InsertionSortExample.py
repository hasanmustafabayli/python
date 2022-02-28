
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

for i in range(7):
   List.append(int(input("Please enter a number into the list: ")))
InsertionSort(List)

    
