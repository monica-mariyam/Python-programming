print("The Invoice program")
class invoice:
    dis=0
    def __init__(self,typ,tot):
        self.typ=typ
        self.tot=tot
        self.dis=0

    def calculate(self):
        if typ.lower()=='r' :
            if tot<100:
                dis=0
            elif tot>=100 and tot<250:
                dis=0.1
            elif tot>=250:
                dis=0.2

        elif typ.lower()=='w':
            if tot<500:
                dis=0.4
            elif tot>=500:
                dis=0.5
        return dis

    def printDetails(self,dis):
        print("\nInvoice total : {:.2f}".format(tot))
        print("Discount percent : {:.2f}".format(dis))
        print("Discount Amount : {:.2f}".format(tot*dis))
        print("New invoice total : {:.2f}".format(tot-tot*dis))

typ=input("\nEnter customer type(r/w) : ")
tot=int(input("Enter invoice total : "))
i=invoice(typ,tot)
dis=i.calculate()
i.printDetails(dis)
