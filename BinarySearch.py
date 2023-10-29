#Binary Search

def binarySearch(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high :
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1

arr = list(map(int,input("Enter the elements of array :").split()))
target = int(input("Enter target element :"))
print("Element found at position ",binarySearch(arr,target))
