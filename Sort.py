import random
array = [random.randint(0,999) for i in range(5)]
print(array)
def bubble(array):
    for i in range(0,len(array)):
        for j in range(1,len(array)-i):
            if(array[j-1]>array[j]):
                array[j-1],array[j] = array[j],array[j-1]
def quick(array,start,end):
    if(start<end):
        flag = array[start]
        low = start
        high = end
        while(low<high):
            while(low<high and flag <array[end]):
                high = high-1
            array[low] = array[high]
            while(low<high and flag > array[low]):
                low =low+1
            array[high] = array[low]
            array[low] = flag
            quick(array,0,low)
            quick(array,low+1,end)
def quickSort(array):
    quick(array,0,len(array)-1)
def mergeSort(array,low,middle,high):
    # print("low=" + str(low) + "high" + str(high) + "middle" + str(middle))
    temp = array[low:high+1]
    i=low
    j=middle+1
    index = 0
    if(len(temp)>1):
        while(i<=middle and j<=high):
            if(array[i]<array[j]):
                temp[index] = array[i]
                i+=1
            else:
                temp[index] = array[j]
                j+=1
            index +=1

        while (j <= high):
            temp[index] = array[j]
            index += 1
            j += 1
        while(i<=middle):
            temp[index] = array[i]
            index+=1
            i+=1

    for k in range(0,len(temp)):
        array[low+k] = temp[k]
def mergeCut(array,low,high):
    if(low<high):
        middle = (low + high) // 2
        print(middle)
        mergeCut(array,low,middle)
        mergeCut(array,middle+1,high)
        mergeSort(array,low,middle,high)
def merge(array):
    mergeCut(array,0,len(array)-1)


def shell(array):
    for n in range(len(array)//2,0,-1):
        for i in range(n,len(array)):
            for j in range(i-n,-1,-1):
                if(array[j]>array[i]):
                    array[i], array[j] = array[j], array[i]

def heap(array):
    start = (len(array)-1)//2
    for i in range(start,0,-1):
        heapSort(array,len(array),i)
    for i in range(len(array)-1,0,-1):
        array[i],array[0] = array[0],array[i]
        heapSort(array,i,0)

def heapSort(array,size,index):
    max = index
    leftNode = 2*index+1
    rightNode = 2*index+2
    if(leftNode<size and array[leftNode]>array[max]):
        max = leftNode
    if(rightNode<size and array[rightNode]>array[max]):
        max = rightNode
    if(max!=index):
        array[max],array[index] = array[index],array[max]
        heapSort(array,size,max)

#heap(array)
#bubble(array)
#quickSort(array)
#merge(array)
#shell(array)
print(array)