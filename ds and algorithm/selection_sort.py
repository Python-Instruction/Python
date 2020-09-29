

def SelectionSort(array):
    for j in range(len(array)-1):
        place=j
        temp=array[j]
        for i in range(j+1,len(array)):
            if temp > array[i]:
                place = i
                temp=array[i] 
            else:
                i=i+1
        #Swap
        array[j],array[place] =array[place],array[j]
        print("Step {}: ".format(j+1),array)
    print("Finally Sorted List:",array)

array=[7, 5, 4, 2]
SelectionSort(array)


