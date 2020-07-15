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
              
              print("Opponent final score is " +str(o_final_score))
              out=1
              if(o_final_score>final_score):
                  break
                  print("Opponent has won")
                  flag3=0    
              elif(final_score>o_final_score):
                  print("You won")
                  break
              else:
                  print("Tie")
                  break
         if(to_win<=0):
             print("Opponent has won")
             break
 """*************************************************************************************************************************************"""        
def player_bowlfirst():
 flag1=1
 flag2=1
 flag3=1
 p_score=0
 out=0
 o_score=0
 #if(Toss()=='Player Bat'):
 print("Start Bowling:")
 while(flag2==1 or out==0 or flag3==0):
     p_bowl=int(input("Enter a number between 1 to 6:\n"))
     o_runs=randint(1,6)
     print(o_runs)
     if(p_bowl>6 or p_bowl<1):
             print("Please type again")
             flag2=1
     else:
        
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
       runs=int(input("Enter a number between 1 to 6\n"))
       bowl=randint(1,6)
       print(bowl)
       if(runs>6 or runs<1):
            print("Please type again")
            flag1=1
       else:
            flag1=0
            p_score+=runs
            to_win=opp_score-p_score
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


def Toss():
  flag1=1
  flag2=1
  flag3=1
 #play_again='y'
  sum=0
 #while(play_again.lower()=='y'):
  while(flag1==1):
        odd_eve=input("Odd or Even?\n Enter 'o' or 'e'\n")
     #print(odd_eve.lower())
        if(odd_eve.lower()!='o' and odd_eve.lower()!='e'):
           print("Please type again")
        else:
           flag1=0
  while(flag2==1):
           toss_num=int(input("Enter your number(between 1 to 6):"))
           if(toss_num>6 or toss_num<1):
               
               
              print("Please type again")
           else:
              flag2=0
              opponent=randint(1,6)
              print("Opponent put "+ str(opponent))
              sum=opponent+toss_num
              print("Sum is "+ str(sum))
  if(sum%2==0 and odd_eve.lower()=='e' or sum%2!=0 and odd_eve.lower()=='o'):
   while(flag3==1):
       bat_bowl=int(input("You won the toss:\n What do you choose?\n 1.Bat\n 2.Bowl\n"))
       if(bat_bowl!=1 and bat_bowl!=2):
           print("Please type again")
           
       else:
          flag3=0
          if(bat_bowl==1):
            print("You chose to bat")
            player_batfirst()
            
          else:
             print("You chose to bowl")
             player_bowlfirst()
             #return 'Player Bowl'
                         
  else:
       print("You lost the toss")
       opp_choice=randint(1, 2)
       if(opp_choice==1):
           print("Opponent has chosen to bat")
           player_bowlfirst()
           #return'Opponent Bat'
       else:
           print("Opponent has chosen to bowl")
           player_batfirst()
           #return 'Opponent Bowl'
 
play_again='y'
while(play_again.lower()=='y'):
    Toss()     
    play_again=input("Want to play again?\n y->yes \n anything else->no\n")

