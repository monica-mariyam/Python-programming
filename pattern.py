'''
Given n = 4, generate the pyramid pattern as shown below and calculate its sum.
      1
    2 1 2
  3 2 1 2 3
4 3 2 1 2 3 4

Sum = 36
'''

n = int(input()) #eg: 4
sum = 0
for i in range(1,n+1):
    sum += 1
    for j in range(2,i+1):
        sum += 2*j
print(sum) #36
