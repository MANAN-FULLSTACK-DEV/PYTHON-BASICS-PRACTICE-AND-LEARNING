#trying to build a clock 
import time 
import datetime
while True :
    options={
    1:"get current time ",
    2:"set a alaram/timer",
    3:"set a stopwatch ",
    4:"exit"
    }
    print(options)
    a=int(input("please enter what you want to do numbers only:"))
    if a==1:
        now=datetime.datetime.now()
        print("current time is :",now.strftime("%I:%M:%S"))
    elif a==2:
        b=input("enter alaram/timer time :")
        while True:
            Time=time.strftime("%I:%M:%S")
            if b==Time:
                for i in range(1,6):
                    print("alaram rings⏰")
                    time.sleep(5)
                break
            else:
                time.sleep(1)
    elif a==3:
        c=input("wanna start/stop the stopwatch:")
        if c=="start":
            sw=0
            while True:
                time.sleep(1)
                sw+=1
                print(sw,"sec")
                # to stop the stopwatch enter ctrl+c in your terminal thank you 
        elif c=="stop":
            print("stopwatch cancelled")
    else:
        print("thanks for coming ")
        break
