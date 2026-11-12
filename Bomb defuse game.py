# defuse the bomb
import random
import time
a=random.randint(1000,9999)
for i in range(1,5):
    i=int(input("enter the code to defuse the bomb :"))
    if i==a:
        print("boom ! you just defused the bomb 😂 ")
        break
    elif i<1000:
        print("bro this is not allowed ☹️")
    elif i>9999:
        print("bro this is not allowed ☹️")
    else:   
        print("something is ticking isn't it ?")
        time.sleep(3)
else:
     print("game over ! man better luck next time 😉")
