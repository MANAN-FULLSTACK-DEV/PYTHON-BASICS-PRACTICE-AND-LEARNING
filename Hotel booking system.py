A="==============Hotel Booking==============="
print(A.center(30))
rooms={"single": 200 , "double": 400,"delux":800, "suite": 1600}
choice=input("which kind of  room you wan to book(eg:single,double,delux,suite) :")
if choice in rooms:
       print(choice,"room price is",rooms[choice],"rupees")
else:
    print("room not available")
choice2=int(input("enter the number of nights you want to stay : "))
if choice2 in range(1,101):
    print("the price of staying for",choice2 ,"nights is =",choice2*rooms[choice],"rupees")
else:
    print("you cant stay ")
availability={"single":25,"double":15,"delux":10,"suite":6}
choice3=int(input("enter the amount of rooms you want : "))
if choice in availability:
    if choice3<=availability[choice]:
               print(choice3,"rooms are alloted to you",availability[choice]-choice3,"rooms are available for",choice,"rooms")
    else:
        print("no rooms available")
else:
    print("room not available")
B="============Thanks for using our service==========="
print(B)
