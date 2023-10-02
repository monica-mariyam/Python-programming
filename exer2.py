'''
This is a program that returns the no. of words, vowels and lines in a paragraph
'''

p="Now is the time to make real the promises of democracy. Now is the time to \nrise from the dark and desolate valley of segregation to the sunlit path of racial justice.\nNow is the time to lift our nation from the quicksands of racial injustice to the \nsolid rock of brotherhood. Now is the time to make justice a reality for all of God's children"

print("No. of words = ",len(p.split()))
vcount=0
for i in p:
    for j in i:
        if j in'aeiouAEIOU':
            vcount+=1
ncount=0
for i in p:
    if i=='\n':
        ncount+=1
print("No. of vowels = ",vcount)
print("No. of lines = ",ncount+1)
