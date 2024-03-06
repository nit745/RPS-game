import random
l = ["rock", "scissor", "paper"]

print('''Rule of game:- In this game round are 5,in every round you choose number(1,2 or 3)
      1.rock, 2.scissor, 3.paper... 
      rock <> scissor =win rock
      rock <> paper = win paper
      scissor <> paper = win scissor
      After 5 rounds Final score decides who win the game..that's it ''')

while True:
    ccount = 0
    ucount = 0
    round=0
              #user choice
    uc = int(input('''
    Game start.....
    1. Yes
    2. No | Exit

                 '''))
                       
    if uc == 1:
        for a in range(1, 6):
            print("           Round=",a+round)   #count round
            print("        -------------")
            
            #user input
            uI = int(input('''
          1.rock
          2.scissor
          3.paper
          
          '''))
            
            if uI == 1:
                uchoice = "rock"
            elif uI == 2:
                uchoice = "scissor"
            elif uI == 3:
                uchoice = "paper"

            cchoice = random.choice(l)    #computer choice

            if cchoice == uchoice:        #if both choices are equal
                print("Computer value: ", cchoice)
                print("User value: ", uchoice)
                print("Game Draw\n")
               
                #case pn which user win the game
            elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == "scissor" and cchoice == "paper") or (uchoice == "paper" and cchoice == "rock"):
                print("Computer value: ", cchoice)
                print("User value: ", uchoice)
                print("You win\n")
                ucount = ucount+1

            else:
                print("Computer value: ", cchoice)
                print("User value: ", uchoice)
                print("Computer win\n")
                ccount = ccount+1
                
        print("\n      Game over")       #end game
        print("\n     Final Score:- ")    #show score
        print("--------------------------")
        
        
        #if both count are equal
        if ucount == ccount:      
            print("User score: ", ucount)
            print("Computer score: ", ccount)
            print(" Game Draw..")

        #if both user count greater than computer count 
        elif ucount > ccount:       
            print("User score: ", ucount)
            print("Computer score: ", ccount)
            print("Congratulations 🫅🎉")
            print("You win the Game..")
                         
        else:
            print("User score: ", ucount)
            print("Computer score: ", ccount)
            print("Computer win the Game..")
            print("\nYou lost 😒")

    else:
        break
