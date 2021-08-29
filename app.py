import threading 
import time
import random

human_decision=["left","right","None"]
global decision
decision=random.choice(human_decision)


nice=[1,2,3,45,3,2,2,1,2,3,4,3,2,6]

humans=[i for i in nice if i ==1 ]
robots=[v for v in nice if v!=1]  
global slap


def loop_for_humans(x):
    pluser=0
    slap=0
    if pluser!=2:
        for n in x:
            if decision=="left" or decision=="right":
                print("Ok Thanks")
                pluser+=1
            else:
                while True:	
                    time.sleep(5)
                    print("Gimme Way Please I have a task to perform")
                
                    chance=random.choice(human_decision)
                
                    if decision=="left" or decision =="right":
                        print("Thanks for listening")
                        pluser+=1
                        break
                        

                    else:
                        if slap>=2:
                            print("B000000000BOOOOOOMMMMMMMMMMBBBBBBB")
                        else:

                            slap+=1
                            print("Please Gimme way")
    else:
        pass  


def loop_for_robots(c):
	for b in c:
		pass


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=loop_for_humans, args=(humans,))
    t2 = threading.Thread(target=loop_for_robots, args=(robots,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  

