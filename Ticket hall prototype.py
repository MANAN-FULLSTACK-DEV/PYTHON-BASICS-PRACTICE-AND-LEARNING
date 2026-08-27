A="=============Ticket Hall============="
print(A.center(20))
movies={"abcdefghijklmnopqrstuvwxyz"}
choice=input("enter the movie name : ")
if choice.startswith(("a", "b", "c", "d", "e", "f")):
     print(choice , "time= 7 30 pm to 10 15 pm")
elif choice.startswith(("g","h","i","j","k","l")):
    print(choice , 'time= 3 30 to 6 45 pm')
elif choice.startswith(("m","n","o","p","q","r")):
    print(choice,"time=1 30 pm to 4 45 pm")
elif choice.startswith(("s","t","u","v","w","x","y","z")):
    print(choice , " time = 8 to 11 15 ")
seats={"normal":200 , "premium":400}
choice2=input("enter the seat type : ")
if choice2=="normal":
    print(choice2, "=" ,seats[choice2])
elif choice2=="premium":
    print(choice2,"=",seats[choice2])
else:
    print("not available")
choice3=int(input("enter the persons :" ))
if choice3 in range(1,701):
    print("your movie price = ",seats[choice2]*choice3)
else:
    print("no seats available")
print("===============enjoy your movie ^_^ =========")
