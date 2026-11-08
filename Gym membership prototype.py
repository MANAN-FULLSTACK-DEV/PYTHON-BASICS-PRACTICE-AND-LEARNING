A="GYM membership checker "
print(A.center(30))
all_member=[]
while True:
    menu={
    1:"Add a member",
    2:"Renew membership",
    3:"cancel Membership",
    4:"exit"
    }
    print(menu)
    B=int(input("enter what you want to do : "))
    print(menu.get(B))
    # for the owner to add a member 
    if B==1:
        class member:
            def __init__(self,name,id,is_active,pin):
                self.name=name
                self.id=id
                self.is_active=is_active
                self.pin=pin
        name=input("enter the name :")
        is_active=True
        id=int(input("enter id :"))
        if 100<id>9999:
                print("id should neither be less than 100 nor more than 9999")
                continue
        else:
            pin=name[:2].lower()+str(id)[:2]
            b=input("enter pin :")
            obj=member(name,id,is_active,pin)
            print("name :",obj.name,"id :",obj.id,"pin :",obj.pin)
            all_member.append(obj)
            
    elif B==2:
         
            name=input("enter name :")
            id=int(input("enter id : "))
            pin=name[:2].lower()+str(id)[:2]
            c=input("enter the pin :")
            if c==pin:
                g=int(input("enter the due ammount :"))
                if g>500:
                    print("you are not an active member now")
                else:
                    print("you are active but get this ammount done before it stacks up")
    elif B==3:    
        name=input("enter name :")
        id=int(input("enter id : "))
        pin=name[:2].lower()+str(id)[:2]
        d=input("enter the pin :") 
        if d==pin:
         c=input("do yo want to cancel the membersehip ?")
        if c=="yes":
                e=int(input("enter your due ammount first :"))
                if e>=500:
                    print("clear your ammount first -__-")
                else:
                    print("ok membership will be canceled by next day")
                
        if c=="no":
                print("thanks for being with us")       
    else:
         f=input("do you want to get out ? :")
         if f=="yes":
              break
         else:
              continue
