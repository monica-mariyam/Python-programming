'''
Pangram is a sentence that uses every alphabet
'''

class toCheck:
    def isPangram(self,s):
        alp='abcdefghijklmnopqrstuvwxyz'
        for i in alp:
            if i not in s:
                return False
        return True

s=input("Enter a string to check for pangram : ")
ob=toCheck()
if(ob.isPangram(s)==True):
    print("It is a pangram")
else:
    print("It is not a pangram")
    
