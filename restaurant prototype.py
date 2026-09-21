A="====restaurant system===="
print(A.center(30))
menu={"healthy food":1,"fast food":2,"dessert":3,"snacks":4}
while True:
    print(menu)
    B=input("Enter the kind of food you want :")
    if B=="healthy food":
        prices=[60,100,200,1000,1500]
        print("prices are",prices)
        a=input("Enter the food you want :")
        b=int(input("Enter in what range :"))
        c=int(input("enter the amount :"))
        if b in prices:
            print(a,"coming to your table , price is",b*c)
        else:
            print("not available")
    if B=="fast food":
        prices=[50,150,250,500,1500,3000]
        print("prices are",prices)
        d=input("enter the food you want :")
        e=int(input("enter the range : "))
        f=int(input("enter the ammount : "))
        if e in prices:
            print(d,'coming to your table and price is =',e*f)
        else:
            print("not available")
    if B=="dessert":
        prices=[30,50,100,200,300,500,1000]
        print("prices are",prices)
        g=input("enter the food you want :")
        h=int(input("enter the range : "))
        i=int(input("enter the amount : "))
        if h in prices:
                print(g,"coming to your table and prices is =",h*i)
        else:
                print("not available")
    if B=="consumeables"or B=="snacks":
        prices=[30,60,90,150,180,240,300]
        print("prices are",prices)
        j=input("enter the name of snack : ")
        k=int(input('enter the range  : '))
        l=int(input('enter the ammount : '))
        if k in prices:
                print(j,"coming to your table price is = ",k*i)
        else:
                print("not available")
    C=input("place order or not:")
    if C=="yes":
        print("your order has been placed offcially now")
        print("thanks for using our service ^_^")
        break
    else:
        print("wanna add some more ? :")
        continue
