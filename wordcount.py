print("The word counter program")
p="Now is the time to make real the promises of democracy. Now is the time to \
rise from the dark and desolate valley of segregation to the sunlit path of racial justice.\
Now is the time to lift our nation from the quicksands of racial injustice to the \
solid rock of brotherhood. Now is the time to make justice a reality for all of God's children"

w=p.split()
new=[]
print("Number of words = ",len(w))
c=0
for i in w:
    if w.count(i)==1:
        c+=1
print("Number of unique words = ",c)
print("Word occurrences : ")
for i in w:
    if i in new:
        continue
    print(i," = ",w.count(i))
    new.append(i)
    
