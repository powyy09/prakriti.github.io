import time
print(time.strftime('%H:%M:%S'))
n= input("enter your name:")
name= n.title()
h=int( time.strftime('%H'))
if h<=4 or h<12: #morning time 4 to 12
    print("Good Morning,",name,"!!")
elif h<=12 or h<16: #afternoon time 12 to 16
     print("Good Afternoon,",name,"!!")
elif h<=16 or h<20: #evening time 16 to 20
      print("Good Evening,",name,"!!")
else:
      print("Good Night,",name,"!!")
      

