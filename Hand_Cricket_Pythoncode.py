"""
************************************************************************************************************************************/
*Project Name: Hand_Cricket.py

*Description: Hand cricket is a common game played in school where the batsman and bowler put a number from 1 to 6. 
              They keep doing this until the bowler and batsman put the same number,which would make the batsman out 
              and then the new innings would start. The 'runs' of the batsman would add up.

*Program: Contains 3 functions, player_batfirst(),player_bowlfirst() and Toss().#player_batfirst and #player_bowlfirst
          are built similarly but reversing by reversing the precedence. Toss() has 4 conditions of which player_batfirst
          works in two of them and player_bowlfirst works in the other two.         
 
***********************************************************************************************************************************
*/"""

"""*********************************************************************************************************************************
Date: 3 June 2020(Completed)

Name: Shreyas Ramani


********************************************************************************************************************************"""
from random import randint
"""random libraries contains a random function and randint is a variable, which randomizes given integers
#within a certain range."""
 
"""*********************************************************************************************************************************"""
def player_batfirst():
 flag1=1     
  #flag1 is to check whether the number entered by the user is within the desired range while player is batting
 flag2=1      
   #flag2 is to check whether the number entered by the user is within the desired range while player is bowling 
 flag3=1      
 #flag3 is to check whether opponent has won the game without getting out
 p_score=0    
 #p_score is to add up the player's score with the runs given as input.
 out=0 
 #out becomes 1 when player gets out.       
 o_score=0
 
 print("Start Batting:")
 while(flag1==1 or out==0):
          runs=int(input("Enter a number between 1 to 6\n"))         
          #runs takes an integer input from 1 to 6
          bowl=randint(1,6)  
            #bowl will contain a number between 1 and 6.(both included)
                                      
          print(bowl)
           
          if(runs>6 or runs<1):                                      
                #if statement to check whether the number entered is in between 1 and 6.                                                        .
             print("Please type again")
                                                                     
             
             flag1=1
             #number entered isn't in desired range
          else:                                                      
             flag1=0
             
             p_score+=runs                                           
              #p_score keeps track of players score according to the numbers he/she puts
                                                                     
             print("Your score is "+str( p_score))                  
             
             if(runs==bowl):                                           
                #if batsman and bowler put the same number, out. 
                 
              print("OUT\n")
              
              final_score=p_score-runs                                 
              #last number put while getting out doesn't count towards final score.
                                                                       
              print("Your final score is " +str(final_score))         
              
              out=1
              #player is out.
 out=0
 
 print("Start Bowling:")                                               
    #now user starts to bowl
 while(flag2==1 or out==0 or flag3==0):
     #when the number is valid, opponent is not out or opponent has won the game.
     p_bowl=int(input("Enter a number between 1 to 6:\n"))
     
     o_runs=randint(1,6)
     #random number between 1 and 6 to display opponent's score
     print(o_runs)
     if(p_bowl>6 or p_bowl<1): 
             flag2=1
             #to  filter out undesired numbers
     else:
        
         o_score+=o_runs
         #displays opponent's score at the time.
         to_win=final_score-o_score
         #displays number of runs opponent need to win at a given time.
         print("Opponent score is: "+str(o_score)      
         print("Opponent needs "+str(to_win+1)+" runs to win.")
         if(o_runs==p_bowl):
         #opponent is out
              print("OUT!!!!!!!!!!!!!!\n")
              o_final_score=o_score-o_runs
              #keeps opponent final score
              print("Opponent final score is " +str(o_final_score))
               
              out=1
               
              if(o_final_score>final_score):
                  break
                  print("Opponent has won")
               #if opponent has a higher score than player, loop breaks.
                  flag3=0   #opponent hasn't 
               
              elif(final_score>o_final_score):
               #if player score is greater than opponent score.
                  print("You won")
                  break
              else:
               #if scores are equal
                  print("Tie")
                  break
         if(to_win<=0):
               #default statement so that loop can break when score difference is settled.
             print("Opponent has won")
             break
 """*************************************************************************************************************************************"""   
               
 """*************************************************************************************************************************************"""
def player_bowlfirst():
 flag1=1
 #flag1 is to check whether the number entered by the user is within the desired range while player is batting             
 flag2=1
 #flag2 is to check whether the number entered by the user is within the desired range while player is bowling 
 flag3=1
   #flag3 is to check whether opponent has won the game without getting out             
 p_score=0
  #Player score counter.      
 out=0
   #out becomes 1 when player/opponent gets out.
 o_score=0
   #Opponent score counter.

 print("Start Bowling:")
               
 while(flag2==1 or out==0 or flag3==0):
   #if bowler's number isn't valid or player isn't out or opponent hasn't won yet.
     p_bowl=int(input("Enter a number between 1 to 6:\n"))
               
     o_runs=randint(1,6)
               #returns number between 1 and 6
     print(o_runs)
               
     if(p_bowl>6 or p_bowl<1):
               #invalid entry
             print("Please type again")
             flag2=1
     else:
        #if entry is valid
         o_score+=o_runs
               
         flag2=0
               
         #to_win=final_score-o_score
         print("Opponent score is: "+str(o_score))
         #print("Opponent needs "+str(to_win)+" runs to win.")
         if(o_runs==p_bowl):
              print("OUT\n")
              o_final_score=o_score-o_runs
              
              print("Opponent final score is " +str(o_final_score))
              out=1
            
 opp_score=o_final_score
 out=0

 print("Start Batting:")    
 while(flag1==1 or out==0):
               #when number is valid and player is not out
       runs=int(input("Enter a number between 1 to 6\n"))
               #allows batsman to enter numbers
       bowl=randint(1,6)
               #opponent puts a random number
       print(bowl)
       if(runs>6 or runs<1):
               #if player puts an invalid number
            print("Please type again")
            flag1=1
       else:
            flag1=0
            p_score+=runs
               #player score counter
            to_win=opp_score-p_score
               #runs needed to win.
            print("Your score is "+str( p_score))
            print("You need "+str(to_win+1)+" runs to win.")
            if(runs==bowl):
              print("OUT!!!!!!!!!!!!!\n")
              final_score=p_score-runs
              print("Your final score is " +str(final_score))
              out=1
    #          if(opp_score>final_score):
                #break
              print("Opponent has won by "+str(to_win+runs-1)+" runs.")
              # print("You won")
              ###print("Tie")
              if(final_score==opp_score):
                  print("Tie")
       if(to_win<0):
            print("You won")
            break
       elif(to_win==0):
           print("Tie")
           break
         #out=0
#Toss()                
#player_batfirst()  
#Hand Cricket
"""***********************************************************************************************************************************************************************"""
       
               
"""***********************************************************************************************************************************************************************"""

def Toss():
  flag1=1
    #to check whether user puts o or e.(case insensitive)
  flag2=1
     #after player chooses odd or even, he/she has to put a number between 1 and 6.
  flag3=1
     #to check whether player puts 1 to bad and 2 to bowl and nothing else.
 #play_again='y'
  sum=0
   #sum of the sum of the toss.
 #while(play_again.lower()=='y'):
  while(flag1==1):
        odd_eve=input("Odd or Even?\n Enter 'o' or 'e'\n")
     #print(odd_eve.lower())
        if(odd_eve.lower()!='o' and odd_eve.lower()!='e'):
               #.lower() makes every entry lowercase.
           print("Please type again")
        else:
           flag1=0
  while(flag2==1):
           toss_num=int(input("Enter your number(between 1 to 6):"))
               #number player puts in the toss
           if(toss_num>6 or toss_num<1):
               
               
              print("Please type again")
           else:
              flag2=0
              opponent=randint(1,6)
               #opponent's number in the toss.
              print("Opponent put "+ str(opponent))
              sum=opponent+toss_num
               #to check total of both player and opponent.
              print("Sum is "+ str(sum))
  if(sum%2==0 and odd_eve.lower()=='e' or sum%2!=0 and odd_eve.lower()=='o'):
               #if player won the toss.
   while(flag3==1):
       bat_bowl=int(input("You won the toss:\n What do you choose?\n 1.Bat\n 2.Bowl\n"))
       if(bat_bowl!=1 and bat_bowl!=2):
           print("Please type again")
           
       else:
          flag3=0
          if(bat_bowl==1):
            print("You chose to bat")
            player_batfirst()
            #calls function player_batfirst() if player chooses to bat.
          else:
             print("You chose to bowl")
             player_bowlfirst()
               #calls function player_bowlfirst() if player chooses to bowl.
             #return 'Player Bowl'
                         
  else:
       #this else statemen is a counter to the first if statement.
       print("You lost the toss")
       opp_choice=randint(1, 2)
               #opponent randomly chooses to bat or bowl.
       if(opp_choice==1):
           print("Opponent has chosen to bat")
           player_bowlfirst()
           #return'Opponent Bat'
       else:
           print("Opponent has chosen to bowl")
           player_batfirst()
           #return 'Opponent Bowl'
 """************************************************************************************************************************************************************************"""
 
play_again='y'
while(play_again.lower()=='y'):
               #as player keeps entering 'y', the game keeps going om.
    Toss()     
    play_again=input("Want to play again?\n y->yes \n anything else->no\n")

               
"""**********************************************************************************************************************************************************************
              Scope for improvement:
              1. Include super over if scores are tied.
              2. Multiple wickets.
              3. Implementing an app.
*************************************************************************************************************************************************************************"""
