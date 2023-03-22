import math

def solution(arr):
    
    arrlenght = len(arr)
    if arrlenght % 2 == 0:
        #odd 
        halfArr = math.floor((arrlenght/2))
        #print(halfArr)
        arr1=arr[0:halfArr]
        arr2=arr[halfArr:]
        #print(arr1)
        #print(arr2)
        arr2=(arr2[::-1])
        resultingArr=[0]*(len(arr1))
        for i in range(len(arr1)):
            resultingArr[i]=int(arr1[i]+arr2[i])
        print(resultingArr)
    else:
        
        #even 
        halfArr = math.floor((arrlenght/2))
        #print(halfArr)
        arr1=arr[0:halfArr]
        arr2=arr[halfArr+1:]
        arr2=(arr2[::-1])
        resultingArr=[0]*(len(arr1))
        for i in range(len(arr1)):
            resultingArr[i]=int(arr1[i]+arr2[i])
        print(resultingArr)
        



solution([4,12,5,21,9,3,6,12,20,18,7,1])
solution([4,12,5,21,9,3,89,6,12,20,18,7,1])