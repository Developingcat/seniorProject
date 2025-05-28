# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define E = Character('Eden', color="#f2c1b6")

define L = Character('Lily', color = "#b07bba" )

# The game starts here.

label start:

# Narration will go inside two double quotations, remember that 

    "An average Thursday Morning. Nothing too out of the loop." 

    "Birds are singing, alarms are ringing---"

    "Alarms are ringing?"

    
# To make a line with a speaker, the name has to be in two double quotations as well! 
label sprites: 
    
    show lily mildlyFearful 

    "L" "Wait. What time is it--"

    "E" "Hey."

    "L" "...Hey?" 

    "E" "If you don't get up, I'm pouring water over your bed. I have mother's permission. So there will be no stopping me."

    "L" "????"

    "Eden walks out of my room promptly out of my room after that statement." 

    "I've never been more confused."

    "Lily" "??? IT'S SATURDAY???"

    "There's no response, which leaves me more confused. And he left my door WIDE OPEN-- he couldn't bother to close it???"

    "Well, only two reasonable options now."

    menu:
        "Sleep a little longer.":
            jump choice1_sleep
            "I guess the passage of time will be allowed..":
            jump choice1_nosleep:

    label choice1_sleep: 
        $ menu_flag = True 
            "Why the hell would I wake up early on a Satruday."
            screen end_credit()
            frame:
            xalign 0.5 ypos 50
            text "Roll Credits.": 
            size 30 
        jump choice1_sleep:

    label choice1_nosleep:
        $ menu_flag = False 
            "Lily" "No point in sleeping in, the day burns away quicker that way."
        jump choice1_done
        
    label choice1_done: 


      

# To continue on with the no sleep thing once it's actually selected, since for some reason it's not working with the choice selection. 

# It'd continue to along, main character asks "Hey, what day is it." and then someone goes "Oh, it's this date" and then the revelation of "OH THAT'S A BIRTHDAY" 






    return