

def BubbleSort(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1-j):
            # Swap two number
            if array[i]>array[i+1]:
                (array[i], array[i+1]) = (array[i+1], array[i])
            else:
                i=i+1 
    print("Sorted Array : ",array)

array =[7, 4, 5, 2]

BubbleSort(array)






