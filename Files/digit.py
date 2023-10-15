'''digit4.txt contains 4 digit number.
M=1st two digits,N=next two digits
Method to generate M number of random numbers with maximum magnitude of N.
Update file with digits generated by method.
Handle Exceptions.
'''

import random
l=[]
m=0;n=0

# digit4.txt initially stores 1096
with open("digit4.txt",'w') as f:
    f.write("1096")
    
try:
    f=open("digit4.txt",'r')
    M=int(f.read(2))
    N=int(f.read(2))
    print(f"m={M},n={N}")
    f.close()
except FileNotFoundError:
    print("File not found")

def genMwithmaxN(M,N):
    for i in range(M):
        l.append(random.randint(1,N))
    print("Digits generated : ",l)
    return l

try:
    f=open("digit4.txt",'a')
    l=genMwithmaxN(M,N)
    for i in l:
        digit='\n'+str(i)
        f.write(digit)
    print("File is updated successfully")
    f.close()
except Exception:
    f.write('1234')