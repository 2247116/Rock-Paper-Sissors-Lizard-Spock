#so rock paper sissors lizard spock, what is needed 
import random
import time

### a list that holds the types 
choices = ['scissors', 'rock', 'paper', 'lizard', 'spock']

def validation (player_input):
    if (player_input == ""):
        ##invalid 
        print("You cant choose nothing")
        return False
    elif(player_input.lower() not in choices):
        ##return false 
        print(player_input + " isn't in the game yet, please make another choice")
        return False
    
    return True

def comp (Player1, Player2):

    #this will compare player 1 agaist player 2 to see if player 1 has won the game
    player1 = Player1.lower()
    player2 = Player2.lower()

    if(player1 == "scissors" and player2 == "paper"):
        print("scissors cuts paper")
        return True

    elif(player1 == 'paper' and player2 == 'rock'):
        print("paper covers rock")
        return True
        
    elif player1 == 'rock' and player2 == 'lizard':
        print("rock crushes lizard")
        return True

    elif player1 == 'lizard' and player2 == 'spock':
        print("lizard poisons spock")
        return True

    elif player1 == 'spock' and player2 == 'scissors':
        print("spock smashes scissors")
        return True

    elif player1 == 'scissors' and player2 == 'lizard':
        print("cissors decapitates lizard")
        return True
        
    elif player1 == 'lizard' and player2 == 'paper':
        print("lizard eats paper")
        return True

    elif player1 == 'paper' and player2 == 'spock':
        print("paper disproves spock")
        return True

    elif player1 == 'spock' and player2 == 'rock':
        print("spock vaporises rock")
        return True 
        
    elif player1 == 'rock' and player2 == 'scissors':
        print("rock crushes scissors")
        return True

    #no matches, so player 1 hasnt won
    return False

print("Welcome to rock, paper, scissors, lizard, Spock")
print(" ")

#wrap it in a while loop to go for 100 times 
i = 0
while i == 0:

    player_choice = input("Please choose an input:")

    ## player input, include validation caps + an actual thing 
    if validation(player_choice) == True:
        #all is well and it is a valid play, so keep her lit as it were, 
        # move on to generate the computer move 
        comp_choice = choices[random.randint(0,4)]
        print(comp_choice)

        ##now compare the two moves 
        #firstly has the player beat the computer 
        val = comp(player_choice,comp_choice)
        if val == True:
            #player has won
            print("Player has won!!")
            time.sleep(1)
            print("Congratulations, you have beaten me ")
            
        
        val = comp(comp_choice,player_choice)
        if val == True:
            #comp has won 
            print("The computer has won!")
            time.sleep(1)
            print("Seems like Ive won, again")
        elif comp_choice == player_choice:
            #must have chosen the same things 
            print("Draw!")
            print("")
            time.sleep(1)
            print("Well, Great minds do think alike ")

    print("Would you like to play again?")
    
    player_choice = input("y = yes, n = no: ")

    #validate the input
    print(player_choice)  
    if (player_choice == "n"):
        i = 1
        print(i)
    else:
        print("Ill take that as a yes!")
