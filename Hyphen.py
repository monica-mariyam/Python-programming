'''
Sample input : Here-is-the-Great-Wall-of-China
Sample output : China-Great-Here-Wall-is-of-the
'''

def convert(a):
    r=a.split('-')
    r.sort()
    s='-'.join(r)
    return s
a=input("Enter a hyphen separated sequence of words : ")
print("Result : ",convert(a))
