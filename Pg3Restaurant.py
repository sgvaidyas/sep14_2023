d = {1:120,2:140,3:180,4:130}
ditems = {1:"FRIED",2:"GHEE",3:"BIRYANI",4:"JEERA"}
price = 0
bill = 0
def displaymenu():
    print("1 FRIED RICE = 120")
    print("2 GHEE RICE  = 140")
    print("3 BIRYANI    = 180")
    print("4 JEERA RICE = 130")
    print("5 EXIT")

def calculateBill(qty,itemprice):
    global price,bill
    price = qty*itemprice
    bill = bill+price

def takeorders():
    global bill
    ch = int(input("Enter choice  = "))
    if ch >= 1 and ch <= 4:
        qty = int(input("Enter the quantity = "))
        calculateBill(qty, d[ch])
        return True
    elif ch == 5:
        print("BILL = ", bill)
        if bill>=700:
            bill = bill-(bill*0.1)
            print("After discount = ",bill)
        return False
    else:
        print("Invalid choice")
        return True
def main():
    while True:
        displaymenu()
        if takeorders()==False:
            break

main()