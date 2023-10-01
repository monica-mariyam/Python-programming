def display():
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    ch=int(input("\nEnter a menu option : "))
    return ch

def f_to_c(f):
    c=5/9*(f-32)
    print("Degree celsius : ",round(c,2))

def c_to_f(c):
    f=9/5*c+32
    print("Degrees fahrenheit : ",round(f,2))

def convert(ch):
    if ch==1:
        f=float(input("Enter degrees in fahrenheit : "))
        f_to_c(f)
    elif ch==2:
        c=float(input("Enter degrees in celsius : "))
        c_to_f(c)

def menu():
    ch=display()
    convert(ch)

if __name__=='__main__':
    menu()
