# this calendar has some limitations but its operating gonna try more best next time 
A="========{calender}========="
print(A.center(30))
choose= int(input("enter the year :"))
import time
time=time.strftime("%I:%M:%S")
print(time)
choice=int(input("enter the week : "))
weeks=[1,2,3,4]
for i in weeks:
   if choice==1:
        print("week 1 (1-22)")
        break
   if choice==2:
         print("week 2 (2-23)")
         break
   elif choice==3:
         print("week 3 (3-24)")
         break
   elif choice==4:
         print("week 4 (4-28)")
         break
y=int(input("enter the date:"))
if y in [1,8,15,22]:
    day="sunday"
elif y in [2,9,16 ,23]:
    day="monday"
elif y in [3,10,17,24]:
    day="tuesday"
elif y in [4,11,18,25]:
    day="wednesday"
elif y in [5,12,19,26]:
    day="thursday" 
elif y in [6, 13, 20, 27]:
    day = "Friday"
elif y in [7, 14, 21, 28]:
    day = "Saturday"
else:
    day = "Invalid date"

print(y, "=", day)
print("------------------------------------------------")
choice2=input("do you want to caclulate anything : ")
if choice2=="yes":
           date1=int(input("enter the date 1 :" ))
           date2 =int(input("enter the date 2 :" ))
           C=input("wanna add or sub :" )
           month=input("enter the month : ")
           if C=="add":
               def  adddatecalculator(date1,date2):
                    add=date1+date2
                    return add
               print(adddatecalculator(date1,date2),month)
           elif  C=="sub":
               def subdate(date1,date2):
                   sub=date1-date2
                   return sub                  
               print(subdate(date1,date2),month,choose)           
elif choice2 =="no":
               print("ok")
X="======== done with the calendar========"
print(X.center(30))     
