
import math
def EcnomicOrderQuantity(d,s,h):

    eoq=math.sqrt((2*d*s)/h)

    return eoq


if __name__ =="__main__":
    print("Economic Order Calculator")
    while (True):
        d=float(input("enter Demand in units\n>>"))
        s=float(input("enter order cost\n>>"))
        h=float(input("enter Holding cost\n>>"))
        print(f"the economic order quantity of your company is {EcnomicOrderQuantity(d,s,h)}")

        print("press CRTL+C to terminate the calculator")

