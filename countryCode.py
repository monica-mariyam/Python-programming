'''Separate country code from mobile number in the form of a string S. 
Criteria:
1. The number must start with a two-digit country code in the start
2. The number should be separated with a hyphen (-) from the country code and the 10-digit number.
The machine returns the country code of the number in the form of a string. In case if it is not a valid number then the software returns 'NF'.
Find and return the output that the software can generate
'''

cc = "91-9899898989"
l = cc.split('-')
lg = len(l[0])
cnt = 0
if lg==2:
    for i in l[0]:
        if i.isdigit():
            cnt+=1
if cnt==2 and len(l[1])==10:
    print(l[0])
else:
    print("NF")
