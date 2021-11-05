# Warmup project to refresh python skills and knowledge written in Python 3.9
# By Jesse Gallarzo
# coding=utf-8

#Character Variables
# / HP/ ATT/ SPD/
killer_stats = [7,3,3]

# / HP/ ATT/ SPD/ LCK/
survivor_stats = [7,2,4,1]


#Game Variables
killer_wins = False
survivor_escapes = False

#Function that deals with assigning turns and dealing combat damage. Returns boolean variables that break the main method.
#TODO turn While() loop into main function.
def battle(sur_hp,kil_hp,sur_attack,kil_attack,sur_speed,kil_speed):
    global survivor_escapes
    global killer_wins
    #If the survivor is faster, damage the killer first
    if(sur_speed > kil_speed):
        killer_stats[0] = killer_stats[0] - sur_attack
        print("The killer takes " + str(sur_attack) + " damage!")
        #Win-Condition
        if killer_stats[0] <= 0:
            print("You managed to fend off the attacker and survived!")
            survivor_escapes = True
            killer_wins = False #Will only run if both instances are declared here; Look into further ; change other win cons
            return
        survivor_stats[0] = survivor_stats[0] - kil_attack
        print("You take " + str(kil_attack) + " damage!")
        #Win-Condition
        if survivor_stats[0] <= 0:    
            print("The killer got to you. Game over...")
            killer_wins = True
            survivor_escapes = False #Will only run if both instances are declared here; Look into further ; change other win cons
            return
    #If the killer is faster, damage the survivor first.
    #TODO fix 'else' statement to be better defined. I.e. 2nd if statement or look into elif again
    else:
        survivor_stats[0] = survivor_stats[0] - kil_attack
        print("You take " + str(kil_attack) + " damage!")
        #Win-Condition
        if survivor_stats[0] <= 0:
            print("The killer got to you. Game over...")
            killer_wins = True
            survivor_escapes = False
            return
        killer_stats[0] = killer_stats[0] - sur_attack
        print("The killer takes " + str(sur_attack) + " damage!")
        #Win-Condition
        if killer_stats[0] <= 0:
            print("You managed to fend off the attacker and survived!")
            survivor_escapes = True
            killer_wins = False
            return
        
#Game Start
print("You're being attacked!")
while(survivor_escapes is False and killer_wins is False):

    #Playable actions for the Player
    action = input("What do you do? FIGHT? or RUN? ")

    #Escape from attack.
    if action.upper() == "RUN":
        survivor_escapes = True
        print("You got away safely!")

    #Fight the killer.
    elif action.upper() == "FIGHT":
        battle(survivor_stats[0], killer_stats[0], survivor_stats[1], killer_stats[1], survivor_stats[2],killer_stats[2])
        print("")
        print("Survivor's health: " + str(survivor_stats[0]))
        print("Killer's health: " + str(killer_stats[0]))
        print("")
        
    #Invalidates any other input except for desired commands.
    else:
        print("Invalid option! Try again.")

    #If none of the game states resolve, restart