
from datetime import datetime
Name=input("Enter your name:")

lists='''
Rice   Rs 50/kg
paneer Rs 80/kg
alu    Rs 20/kg
tomato Rs 30/kg
onion  Rs 25/kg
ginger Rs 10/kg
colgateRs 15/kg
boost  Rs 150/kg
maggi  Rs 20/kg
'''
# declaration
price=0
pricelist=[]
totalprice=0
finalamount=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':50,'paneer':80,'alu':20,'tomato':30,'onion':25,'ginger':10,'colgate':15,'boost':150,'maggi':20}
option=int(input('for list of items press 1:'))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:print('sorry you entered item is not available')
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
    if finalamount!=0:
        print(25*"=",'bhuvan supermarket',25*"=")
        print(30*" ","store")
        print("Name:",Name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ","quantity",3*" ",'price')
        for i in range(len(pricelist)):
            print(i,8*' ',ilist[i],8*' ',qlist[i],10*" ",plist[i])
        print(75*"-")
        print(50*" ",'TotalAmount:','Rs',totalprice)
        print("gst amount",50*" ","Rs",gst)
        print(75*"-")
        print(50 * " ",'finalamount:','Rs',finalamount)
        print(75 * "-")
        print(25 *" ","Thanks for visting")
        print(75 *"")
