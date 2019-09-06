#Bidding game
#Author : Taekyung, Kil
# 01/April / 2019 


import time
import re
import random
from heapq import nsmallest


print("Welcome to the python game. ")
time.sleep(0.2)
username = input("Please enter your name using only letters: ")
username = username.capitalize()

while True:

    if ( re.search ( '[!,@,#,$,%,^,&,*]', username) is not None) :
        username = input("Please re-enter your name using only letters: ")
        
    elif (username.isnumeric()):
        print("It is a number. Please use only letters")
        username = input("Please re-enter your name using only letters: ")

    else: break

    
username = username.capitalize()
print (username + " Come on down!   You're the next contestant on the Price is (sorta) Right! \n Bob Mewoer welcomes Steve to contant's row, joining Lolobid , Juandollar , and Buckmore" )

time.sleep(0.3)         
print ( "Bob Meower shows you the prize you will be bidding on")

userbid = input(username + ", What is your bid ? $")

while True:

    if (userbid.isnumeric()) : break

    else:
        print("Bob Meower says, Im sorry I couldn't make that out, a bid of at least $1 please.")
        userbid = input(username + ", What is your bid ? $")
        

userbid = int(userbid)
lol = random.randint( 50 , 1000 )
juan = random.randint( 50 , 1000 )
buck = random.randint( 50 , 1000 )
price = random.randint ( 50 , 1000)
time.sleep(0.2)
print ( "Lolobid bids " + str(lol) + " dallars." )
time.sleep(0.2)
print ( "Juandollar bids " + str(juan) + " dallars." )
time.sleep(0.2)
print ( "Buckmore bids " + str(buck) + " dallars." )
time.sleep(0.4)

print ( "Bob Meower says, 'The actual retail parice of the item was " + str(price) + " Dollars'")

#First game processing
while True:

    if ( lol > price and juan > price and buck > price and userbid > price ) :
        print ("Bob Meower says, 'I'm sorry but everyone has bid too high, let's try agin.'")
        userbid = input(username + ", What is your bid ? $")
        while True:

            if (userbid.isnumeric()) : break

            else:
                print("Bob Meower says, Im sorry I couldn't make that out, a bid of at least $1 please.")
                userbid = input(username + ", What is your bid ? $")
                
        userbid = int(userbid)
        lol = random.randint( 50 , 1000 )
        juan = random.randint( 50 , 1000 )
        buck = random.randint( 50 , 1000 )
        price = random.randint ( 50 , 1000)
        wins = [lol, juan , buck, username ]
        print ( "Lolobid bids " + str(lol) + " dallars." )
        time.sleep(0.2)
        print ( "Juandollar bids " + str(juan) + " dallars." )
        time.sleep(0.2)
        print ( "Buckmore bids " + str(buck) + " dallars." )
        time.sleep(0.3)

        print ( "Bob Meower says, 'The actual retail parice of the item was " + str(price) + " Dollars'")

       

    else: break
                

        
        

        
Closest = lambda num, collection:min ( collection, key=lambda x:abs(x-num))
winner = Closest(price,[lol, buck,userbid, juan])

userlist = ["Lolobid", "Juandollar", "Buckmore", username]
time.sleep(0.4)
if  winner == userbid :
    print ("Bob Meower says, '"+ username +" is our winner'")
    print("Bob Meower says, 'Today we're playing Three Strikes, reach in the bag and pull out a ball to get us started'")

else:
    if winner == lol :
        print ("Bob Meower says, 'Lolobid is our winner'")
        userlist.remove("Lolobid")

    elif winner == juan :
        print ("Bob Meower says, 'Juandollar is our winner'")
        userlist.remove("Juandollar")

    elif winner == buck :
        print ("Bob Meower says, 'Buckmore is our winner'")
        userlist.remove("Buckmore")
#Second game processing

    print(userlist)

    print("Try again !!!")
    userbid = input(username + ", What is your bid ? $")
    while True:

        if (userbid.isnumeric()) : break

        else:
            print("Bob Meower says, Im sorry I couldn't make that out, a bid of at least $1 please.")
            userbid = input(username + ", What is your bid ? $")
            

    userbid = int(userbid)
    lol = random.randint( 50 , 1000 )
    juan = random.randint( 50 , 1000 )

    price = random.randint ( 50 , 1000)
    time.sleep(0.2)
    print ( userlist[0]+" " + str(lol) + " dallars." )
    time.sleep(0.2)
    print ( userlist[1] +" "+ str(juan) + " dallars." )

    time.sleep(0.4)
    print ( "Bob Meower says, 'The actual retail parice of the item was " + str(price) + " Dollars'")

    while True:

        if ( lol > price and juan > price and buck > price and userbid > price ) :
            print ("Bob Meower says, 'I'm sorry but everyone has bid too high, let's try agin.'")
            userbid = input(username + ", What is your bid ? $")
            while True:

                if (userbid.isnumeric()) : break

                else:
                    print("Bob Meower says, Im sorry I couldn't make that out, a bid of at least $1 please.")
                    userbid = input(username + ", What is your bid ? $")
                    


            userbid = int(userbid)
            lol = random.randint( 50 , 1000 )
            juan = random.randint( 50 , 1000 )
           
            price = random.randint ( 50 , 1000)
       
            print ( userlist[0] +" "+ str(lol) + " dallars." )
            print ( userlist[1] +" "+ str(juan) + " dallars." )

            print ( "Bob Meower says, 'The actual retail parice of the item was " + str(price) + " Dollars'")

           

        else: break
                    

            
            

            
    Closest = lambda num, collection:min ( collection, key=lambda x:abs(x-num))
    winner = Closest(price,[lol,userbid, juan])

    if winner == userbid :
        print ("Bob Meower says, '"+ username +" is our winner'")
        print("Bob Meower says, 'Today we're playing Three Strikes, reach in the bag and pull out a ball to get us started'")



    else:
        
        if winner == lol :
            print ("Bob Meower says,'" + userlist[0] +" is our winner'")
            userlist.remove(userlist[0])

        elif winner == juan :
            print ("Bob Meower says, '" + userlist[1]+" is our winner'")
            userlist.remove(userlist[1])

#3 game processing

        print(userlist)

        userbid = input(username + ", What is your bid ? $")
        while True:

            if (userbid.isnumeric()) : break

            else:
                print("Bob Meower says, Im sorry I couldn't make that out, a bid of at least $1 please.")
                userbid = input(username + ", What is your bid ? $")
                

        userbid = int(userbid)
        lol = random.randint( 50 , 1000 )


        price = random.randint ( 50 , 1000)
   
        print ( userlist[0]+" " + str(lol) + " dallars." )
     


        print ( "Bob Meower says, 'The actual retail parice of the item was " + str(price) + " Dollars'")

        while True:

            if ( lol > price and juan > price and buck > price and userbid > price ) :
                print ("Bob Meower says, 'I'm sorry but everyone has bid too high, let's try agin.'")
                userbid = input(username + ", What is your bid ? $")
                while True:

                    if (userbid.isnumeric()) : break

                    else:
                        print("Bob Meower says, Im sorry I couldn't make that out, a bid of at least $1 please.")
                        userbid = input(username + ", What is your bid ? $")
                        


                userbid = int(userbid)
                lol = random.randint( 50 , 1000 )
     
               
                price = random.randint ( 50 , 1000)
                wins = [lol, juan , buck, username ]
                print ( userlist[0] +" "+ str(lol) + " dallars." )
            

                print ( "Bob Meower says, 'The actual retail parice of the item was " + str(price) + " Dollars'")

               

            else: break
                        

                
                

                
        Closest = lambda num, collection:min ( collection, key=lambda x:abs(x-num))
        winner = Closest(price,[lol,userbid])

        if winner == userbid :
            print ("Bob Meower says, '"+ username +" is our winner'")
            print("Bob Meower says, 'Today we're playing Three Strikes, reach in the bag and pull out a ball to get us started'")



        else:
            
            if winner == lol :
                print ("Bob Meower says,'" + userlist[0] +" is our winner'")
                userlist.remove(userlist[0])
                print("\n")
                print("Bob Meower turns to Steve and says, 'I'am sorry you didn't have better luck here today, but we're sending you home with the unofficial board game of The price is (Sorta) Right.'")
