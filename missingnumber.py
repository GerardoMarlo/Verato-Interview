# Write a program to find the missing number in an array of positive integers from 1 to n. 
# There will always only be one number missing from the input array. 
# Array might not be a sorted array. 

# Example 1:
# Input : [3,7,1,2,8,4,5,9] 
# Result: 6

# Example 2:
# Input: [1,3]
# Result: 2

# Example 3:
# Input : [3,1,2]
# Result: 4

def solution(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if int(arr[i]+1)== arr[i+1]:
            pass
        else:
            print(int(arr[i]+1))


solution([3,7,1,2,8,4,5,9])


def solution2(arr): #optimized version without sorting
    arr_lenght=len(arr)
    newarr = list(range(1, arr_lenght+1))
    
    for number in newarr:
        if number in arr:  # Input : [3,7,1,2,8,4,5,9] 
            pass
        else:
            print(number)


solution2([3,7,1,2,8,4,5,9])
