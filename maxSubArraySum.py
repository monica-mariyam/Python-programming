#maximum subarray problem
#brute force approach - O(n^2)

def maxSubArraySum(arr):
    maxsum = 0
    n = len(arr)
    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum > maxsum:
                maxsum = sum
    return maxsum

arr = list(map(int,input("Enter an array of integers : ").split()))
print("Maximum sum : ",maxSubArraySum(arr))
