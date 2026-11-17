# quiz game 
import time
quiz={
    1:"who is the ceo of claude ? ",
    2:"which game won game of the year in 2026 ",
    3:"which programming language is known as the slow language  yet newbies choses it ?",
    4:"when was world war 2 happened ?",
    5:"who is the director of the movie (A clockwork orange)?"
    }
answers={
    1:"Dario Amodei",
    2:"Resident Evil Requiem",
    3:"python",
    4:"September 1, 1939",
    5:"stanley kubrick"
    }
count=0
for i in range(1,6):
        print(quiz[i])
        time.sleep(2)
        a=input("answer the questions :").lower().strip()
        if a ==answers[i].lower().strip():
            count+=10
        else:
              print("out of the game bye ^_^ ")
              break
if  count==50: 
 	print("congo you won -_-! and your score is ",count)
elif count==0:
	  print(" awww you lose ")   
else:          
 	print(" your  score is ",count)
  
