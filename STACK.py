#simple stack operations
stack=[]
while True:
    print("1.Push")
    print("2.Diaplay the stack")
    print("3.Pop")
    print("4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        x=int(input("Enter a number:"))
        stack.append(x)

    elif ch==2:
        if stack==[]:
            print("Empty stack")
        else:
            for i in range(len(stack)-1,-1,-1):
                print(stack[i])
    elif ch==3:
        if stack==[]:
            print("Empty stack")
        else:
            print("Deleted element:",stack.pop())
    elif ch==4:
        print("Exiting")
        break
    else:
        print("InVALID CHOICE")
    print()
