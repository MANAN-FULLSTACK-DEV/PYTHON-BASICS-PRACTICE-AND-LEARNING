A="___________________Bank system___________________________"
print(A.center(20))
a=input(" enter your your name :" )
b=int(input("enter your 4-digit account pin :"))
if 1000<=b<=9999:
         pass
elif b<1000 or b>9999:
        print("wrong pin")
B=input("what you want to do with the money you have ? : ")
balance=int(input("enter the balance : "))
if B=="withdrawal":
                C=int(input("enter the  amount of money you want to withdraw : " ))
                def withdrawal(C):
                         return balance - C
                if C<=balance:
                    balance=withdrawal(C)
                    print(C,"rupees are withdrawn")
                    print("remaining balance","=",balance)
                else:
                        print("lower than balance not allowed")
if B == "deposit":
    D = int(input("enter the amount of money you want to deposit: "))
    if D<0:
        print('no you cant deposit that ')
    else:
        pass 

    def deposit(D):
        return balance + D
    print(deposit(D), " rupees are deposited")        
if B=="check balance":
    print("your bank balance is =",balance,"rupees")
