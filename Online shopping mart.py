M="--------------------MyMART.com---------------------------"
print(M.center(25))
print("welcome to MyMART WHAT YOU WANT TO BUY :")
Choice=input()
A="---------------groceries---------------------"
groceries={
   "rice" : 50 ,
   "flour": 60,
   "cornflour": 50,
   "cornflour": 40,
   "snacks": 100,
}
B="--------------------vegetables-------------"
vegetables={
   "potato": 30 ,
   "onion"  : 40 , 
    "garlic" : 50 , 
    " all fruits " : 50 , 
    " rest vegetables" : 30 ,
}
C="--------------------medical(from M1 tier to M10)--------------------"
medical={
    "m1" : 25, 
    "m" : 60 , 
     "m3" : 35 ,
     " m4" : 45 ,
     "m5" : 100 ,
     "m6" : 80 ,
     "m7" : 70 , 
     "m8"   :  55 ,
     "m9" : 150 ,
     "m10" : 90 ,
}
D="--------------------home items --------------------"
items={
  "electrical items" : 200 ,
  "decorative things" : 300 ,
}
if Choice=="groceries":
    print(A, groceries)
    choice2=input("enter the items you love to select : ")
    if choice2 in groceries:
        print(choice2,"=",groceries[choice2])
    else:
         print("item not found ")
elif Choice=="vegetables":
    print(B,vegetables)
    choice2=input("enter the items you love to select  : ")
    if choice2 in vegetables:
        print(choice2,"=",vegetables[choice2])
    else:
        print("item not found ")
elif Choice=="medical":
    print(C,medical)
    choice2=input("enter the items you love to select  : ")
    if choice2 in medical :
        print(choice2,"=",medical[choice2])
    else:
        print("item not found")
elif Choice=="home items":
    print(D,items)
    choice2=input("enter the items you love to select  : " )   
    if  choice2 in  items:
        print(choice2,"=",items[choice2])
    else : 
        print("item not found")
else:
       print("not available bettee luck next time ... ^_^ ")
cart={ }
while True :
    choice=input("enter the items to cart (enter 'done' to checkout the cart') : ")
    if choice.lower()=="done":
        break
    if choice in groceries :
       cart[choice]=groceries[choice]
    elif choice in vegetables:
        cart[choice]=vegetables[choice]
    elif choice in medical :
         cart[choice]=medical[choice]
    elif choice in items:
          cart[choice]=items[choice]
    else:
       print("item not available ")
total=0
for items , price in cart.items():
      print(items, "=",price)
      total+=price
print("total=",total,"₹")
print("please pay this amount via cash or online")
print(" --------------------thanks for using our site --------------------")
