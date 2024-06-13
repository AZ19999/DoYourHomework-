import time

tryAgain = 0
timeLeft = 5
glyph = False
gems = False
legHelp = False

#User Responses
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
answer_E = ["E", "e"]
answer_F = ["F", "f"]
secretAdmin = ["1234509876"]

yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]

#Ending counters
endings = 0 #18 possible endings
possibleEndings = [False for x in range(0,18)]

#making sure user uses proper responses
required = ("\nPlease input a valid response\n")
requiredEnding = ("\nPlease use only y or n\n")

def intro():
    global endings
    global tryAgain
    global timeLeft
    global gems
    global glyph
    global legHelp
    if tryAgain > 0:
        tryAgain = 0
    if timeLeft < 5:
        timeLeft = 5
    if gems == True:
        gems = False
    if glyph == True:
        glyph = False
    if legHelp == True:
        legHelp = False
    print("Do Your Homework")
    time.sleep(0.5)
    print("By Alex Zhu and Henry Rouslin")
    time.sleep(0.5)
    print ("\nYou are Clyde Chesterson, an 18 year old college freshman"
         " who’s just started his first year at Brandeis. Your first day was yesterday, "
         "but the only class you had was Intro to Homework, in which you receive generic "
         "homework and then go over it in class the next day. Suddenly, you have a strange thought: "
         "“Do you want to go on an adventure?”")
    time.sleep(0.5)
    print("What is your response?")
    time.sleep(0.5)
    print ("""  A. No
  B. Hell no!""")
    if endings == 18:
        print ("""  C. See flowchart""")
    choice = input(">>> ")
    if choice in answer_A:
        option_no()
    elif choice in answer_B:
        option_hell_no()
    elif endings == 18:
        if choice in answer_C:
            print("If you're seeing this, that means you got all the endings!")
            time.sleep(0.5)
            print("To show you just how awesome of a feat that was, here's a flowchart with all of the possible paths/routes that you've been down!")
            time.sleep(0.5)
            print ("""Please copy+paste the following link to view the complete flowchart:\n\nhttp://bit.ly/CompSciRocks\n\n""")
            time.sleep(0.5)
            print("I don't know why you would, but do you want to play again?")
            choice = input(">>> ")
            if choice in yes:
                print("You asked for it...")
                time.sleep(0.5)
                intro()
            elif choice in no:
                quit()
    elif choice in secretAdmin:
        endings = 18
        intro()
    else:
        print (required)
        intro()

#No Branch

def option_no():
    print ("Aww, why not? I promise it will be a lot of fun!")
    time.sleep(0.5)
    print ("""  A. Because I don't want to.
  B. Because I'm tired""")
    choice = input(">>> ")
    if choice in answer_A:
        option_dontWant()
    elif choice in answer_B:
        option_tired()
    else:
        print (required)
        option_no()

#the don't want path
def option_dontWant():
    print ("Come on, I bet I can change your mind")
    time.sleep(2)
    print("In a sudden burst of energy, you are whisked away and thrown violently into a new region of spacetime. "
          "You land harshly against a cold, metal floor. It appears you’ve been transported onto a large spacecraft or "
          "otherwise space-faring vehicle. As furious as you are that your work has been impeded, you do admit that breaking "
          "planetary confinement is somewhat of an interesting way to spend your time. Looking around, you see two doors, both "
          "labelled in a strange alien language, yet somehow, you’re able to read it. ")
    time.sleep(0.5)
    print ("""  A. Enter the door labeled: Egress
  B. Enter the door labeled: Abstraction""")
    choice = input(">>> ")
    if choice in answer_A:
        option_Egress()
    elif choice in answer_B:
        option_Abstraction()
    else:
        print (required)
        option_dontWant()

def option_Egress():
    print("As you open the door, you see a tunnel ending in what appears to be an escape pod. "
          "However, the station begins shaking, and a red light blares. You look through a window "
          "and see the station approaching a wormhole. The escape pod has temporal shielding, and "
          "you'll surely be safe there. However, as you run to get inside, the wormhole envelopes the"
          " station, and you are exposed to its anomalous effects. All laws of physics break.")
    time.sleep(0.5)
    print ("""  A. Yes
  B. Yes
  C. Yes
  D. Yes
  E. Yes
  F. Yes
  """)
    choice = input(">>> ")
    if choice in answer_A or choice in answer_B or choice in answer_C or choice in answer_D or choice in answer_E or choice in answer_F:
        ending_3()
    else:
        print (required)
        option_Egress()

def option_Abstraction():
    print("You open the door and walk inside. As it closes behind you, you look around. Paintings and sculptures of various shapes and sizes fill the room. You appear to be in some kind of art gallery. Quietly, you attempt to sneak around, but the floor is dummy slick, and you trip, knocking over what seems to be a priceless artifact. As it hits the floor, it bounces up, and right into your hands. Suddenly, an alarm sounds. Someone, or something is coming.")
    time.sleep(0.5)
    print ("""  A. Find a place to hide
  B. Prepare to fight
  """)
    choice = input(">>> ")
    if choice in answer_A:
        option_Hide()
    elif choice in answer_B:
        option_fight()
    else:
        print (required)
        option_Abstraction()

def option_Hide():
    print("You look around for somewhere to hide. You see a door labelled: closet, and figure it could be an option. However, there's also a funky looking wax-sculpture exhibit that, along with various unknown creatures, features a number of humans. What do you do?")
    time.sleep(0.5)
    print("""  A. Blend in with the statues
  B. Hide in the closet
  """)
    choice = input(">>> ")
    if choice in answer_A:
        ending_2()
    elif choice in answer_B:
        option_Closet()
    else:
        print(required)
        option_Hide()

def option_Closet():
    print("You hide in the closet and listen quietly as footsteps pass by you. After a bit more waiting, you come out and look around. You make it to what appears to be the central hub of the ship before a door opens and a number of guards walk in. You've been spotted, and there's no where to hide. It seems you've begun... a chase sequence!")
    time.sleep(0.5)
    chase()

def option_fight():
    print(
        "You grab a large rock from a life-size replica of stonehenge and as the door opens, and an alien guard walks in, you throw the rock. It misses, and the alien begins shooting at you with its laser gun. A few other aliens join in, and soon you're running down corridor after corridor with laser blasts following right behind you. You've begun... A Chase Sequence!")
    time.sleep(0.5)
    chase()

# chase sequence

def chase():
    global tryAgain
    if tryAgain == 6:
        ending_4()
    print ("Begin Chase Sequence:\n\nYou run down a hallway. One of the aliens shoots their gun at a barrel up in front of you. It begins steaming, like it's going to explode.")
    time.sleep(0.5)
    print ("""  A. Jump\n  B. Dodge\n  C. Slide""")
    choice = input(">>> ")
    if choice in answer_A:
        tryAgain += 1
        print ("You jump over nothing, and land right in the explosion.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    elif choice in answer_B:
        chase2()
    elif choice in answer_C:
        tryAgain += 1
        print ("You slide, and skid against the ground right into the explosion.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    else:
        print(required)
        chase()

def chase2():
    global tryAgain
    print ("As the barrel explodes, shrapnel shoots out. You dodge it, all matrix style, and keep running. However, the explosion knocks over a pillar, and it begins to fall into your path.")
    time.sleep(0.5)
    print ("""  A. Jump\n  B. Dodge\n  C. Slide""")
    choice = input(">>> ")
    if choice in answer_A:
        tryAgain += 1
        print ("You try to jump over the falling pillar, but it is too tall, and you are crushed beneath it.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    elif choice in answer_B:
        tryAgain += 1
        print ("You try to dodge out of the way, but it is falling too fast, and you are unable to avoid it.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    elif choice in answer_C:
        chase3()
    else:
        print(required)
        chase2()

def chase3():
    global tryAgain
    print ("You slide under the falling pillar, which narrowly misses crushing you. You see a door at the end of the room that reads 'escape pods', but blocking your path is a huge laser field.")
    time.sleep(0.5)
    print ("""  A. Jump\n  B. Dodge\n  C. Slide""")
    choice = input(">>> ")
    if choice in answer_A:
        chase4()
    elif choice in answer_B:
        tryAgain += 1
        print ("You dodge left and right, but the lasers also dodge left and right, confusing you and catching you in the side of the leg.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    elif choice in answer_C:
        tryAgain += 1
        print ("You lower yourself to the floor and slide across. Unfortunately for you, there are also lasers on the floor..")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    else:
        print(required)
        chase3()

def chase4():
    global tryAgain
    print ("You jump over each laser, landing gracefully on the other side. You run into a pod and see three buttons.")
    time.sleep(0.5)
    print ("""  A. Jump\n  B. Dodge\n  C. Slide""")
    choice = input(">>> ")
    if choice in answer_A:
        chase5()
    elif choice in answer_B:
        tryAgain += 1
        print ("You press the 'dodge' button, and the escape pod swings violently to avoid a non-existent attacker, throwing itself instead against the wall, and self-destructing.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    elif choice in answer_C:
        tryAgain += 1
        print ("You press the 'slide' button, and a sad slide-whistle sound plays as the aliens surround you.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    else:
        print(required)
        chase4()

def chase5():
    global tryAgain
    print ("ou press the 'jump' button and immediately hyper-jump at the speed of light. However, the ship follows in close pursuit as you draw closer and closer to earth.")
    time.sleep(0.5)
    print ("""  A. Jump\n  B. Dodge\n  C. Slide""")
    choice = input(">>> ")
    if choice in answer_A:
        tryAgain += 1
        print ("You press the 'jump' button again, which sends the escape pod hurtling straight into the earth's upper crust.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    elif choice in answer_B:
        chase6()
    elif choice in answer_C:
        tryAgain += 1
        print ("You press the 'slide' button, and a sad slide-whistle sound plays as the mothership shoots a laser blast at you, blowing up the escape pod.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    else:
        print(required)
        chase5()

def chase6():
    global tryAgain
    print ("You press the 'dodge' button, and the pod dodges out of the way, narrowly missing a laser blast from the mothership. However, the laser blast is instead heading right for the earth.")
    time.sleep(0.5)
    print ("""  A. Jump\n  B. Dodge\n  C. Slide""")
    choice = input(">>> ")
    if choice in answer_A:
        tryAgain += 1
        print ("You press the 'jump' button again, which sends the escape pod hurtling straight into the earth's upper crust.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    elif choice in answer_B:
        tryAgain += 1
        print ("You dodge, and the laser blast hits the earth, killing everyone on it.")
        time.sleep(0.5)
        print ("A. Try Again")
        choice = input(">>> ")
        if choice in answer_A:
            chase()
        else:
            print(required)
            chase()
    elif choice in answer_C:
        ending_1()
    else:
        print(required)
        chase6()

#the tired path
def option_tired():
    print("Ok, that's fine. Get some sleep.")
    time.sleep(0.5)
    theNextDay()

def theNextDay():
    print("You finish your homework, and go to sleep. The next day, you wake up right on time, but are faced with a dilemma. Breakfast at Sherman or Usdan?")
    time.sleep(0.5)
    print("""  A. Go to Sherman
  B. Go To Usdan
  C. Skip Breakfast
    """)
    choice = input(">>> ")
    if choice in answer_A:
        option_Sherman()
    elif choice in answer_B:
        option_Usdan()
    elif choice in answer_C:
        ending_7()
    else:
        print(required)
        theNextDay()

#Sherman path/true ending path
def option_Sherman():
    print(
        "You walk to Sherman, have a simple breakfast, and proceed to class. Your first class is Computer Science 10a. ")
    time.sleep(0.5)
    print("""  A. Close your Eyes
  B. Take Notes
  C. Work on your Project
        """)
    choice = input(">>> ")
    if choice in answer_A:
        ending_6()
    elif choice in answer_B:
        option_Notes()
    elif choice in answer_C:
        option_Project()
    else:
        print(required)
        option_Sherman()

def option_Notes():
    print(
        "You begin to take notes. Suddenly, a number of large, angry gorillas burst into the room and begin stealing students, and taking them to their secret lair in the zoo. You didn't notice, however, because you were taking notes, and since you have your own issues to deal with, you don't really feel any obligation to fix this in any way.")
    time.sleep(0.5)
    print("""  A. Go to the Bathroom
  B. Go to your next class
            """)
    choice = input(">>> ")
    if choice in answer_A:
        option_bathroom()
    elif choice in answer_B:
        option_nextClass()
    else:
        print(required)
        option_Notes()

def option_nextClass():
    print(
        "On your way to your next class, you notice your friend heading into the same building. You want to be the nice person and open the door for them, but they're closer to the door, so it would make sense to let them open it for you.")
    time.sleep(0.5)
    print("""  A. Run up and open it for them
  B. Let them open it for you
              """)
    choice = input(">>> ")
    if choice in answer_A:
        ending_8()
    elif choice in answer_B:
        option_letThem()
    else:
        print(required)
        option_nextClass()

def option_letThem():
    print(
        "You keep your pace steady and let them open the door for you. As you walk into day 2 of Intro to Homework, you are hit by a sudden realization. You left your homework in your dorm. There are only 5 minutes until your next class, but you're 10 minutes from your dorm. You have a few items in your backpack you might be able to use.")
    time.sleep(0.5)
    print("""  A. Proceed to class
  B. Use mysterious crystal
  C. Use glowing metal object
                """)
    choice = input(">>> ")
    if choice in answer_A:
        ending_5()
    elif choice in answer_B:
        option_Crystal()
    elif choice in answer_C:
        option_GlowingObject()
    else:
        print(required)
        option_letThem()

def option_Crystal():
    print(
        "You grab the mysterious purple crystal given to you by an old woman with a cart of strange items in a Boston alley. As your skin makes contact with it, you begin to glow, and the crystal shatters. You feel empowered, and ready for life itself. However, being ready for life does not aid you in any way, so nothing changes.")
    time.sleep(0.5)
    print("""  A. Proceed to class
  B. Use glowing metal object
                    """)
    choice = input(">>> ")
    if choice in answer_A:
        ending_5()
    elif choice in answer_B:
        option_GlowingObject()
    else:
        print(required)
        option_Crystal()

def option_GlowingObject():
    print(
        "You grab the glowing metal object you found under your seat during orientation and press the button labelled 'do not press'. All around you, every student who was currently walking to class begins to slow to a halt. The birds in the sky freeze in mid-flap, and sure enough, your watch ceases to function. You take all the time in the world walking to your dorm, grabbing the homework, and making it to class.")
    time.sleep(0.5)
    print("""  A. Deactivate the Object
                       """)
    choice = input(">>> ")
    if choice in answer_A:
        ending_18()
    else:
        print(required)
        option_GlowingObject()

#Simulation 1 path
def option_Project():
    print(
        "You begin writing your computer science project. After a bit of work, you've created an intro, and a rudimentary skeleton code. You press play to test it out. ")
    time.sleep(2)
    intro()

#bathroom path
def option_bathroom():
    print(
        "You proceed to the bathroom, and use it before returning to the lecture hall. ")
    time.sleep(0.5)
    print("""  A. Go to the Bathroom
  B. Go to your next class
                """)
    choice = input(">>> ")
    if choice in answer_A:
        option_bathroom2()
    elif choice in answer_B:
        option_nextClass()
    else:
        print(required)
        option_bathroom()

def option_bathroom2():
    print(
        "You go back to the bathroom. You use it, again, before once again returning to the lecture hall.")
    time.sleep(0.5)
    print("""  A. Go to the Bathroom
  B. Go to your next class
                    """)
    choice = input(">>> ")
    if choice in answer_A:
        option_bathroom3()
    elif choice in answer_B:
        option_nextClass()
    else:
        print(required)
        option_bathroom2()

def option_bathroom3():
    print(
        "Just like the last two times. You go back to the bathroom. You use it before once again returning to the lecture hall.")
    time.sleep(0.5)
    print("""  A. Go to the Bathroom
  B. Go to your next class
                       """)
    choice = input(">>> ")
    if choice in answer_A:
        ending_9()
    elif choice in answer_B:
        option_nextClass()
    else:
        print(required)
        option_bathroom3()

#usdan path/simulation 2 path
def option_Usdan():
    print(
        "You begin walking towards Usdan, which is situated near the middle of campus, and much farther from your dorm than Sherman, However, after about 20 minutes of walking, you realize you've barely moved at all. Oh no, just your luck. It seems as if you've been trapped inside a hyper-realistic simulation. What is your reaction?")
    time.sleep(0.5)
    print("""  A. Be calm and assess your sorroundings
  B. FREAK OUT
        """)
    choice = input(">>> ")
    if choice in answer_A:
        option_calm()
    elif choice in answer_B:
        option_freak()
    else:
        print(required)
        option_Usdan()

def option_calm():
    print(
        "\nYou explore the Brandeis campus, which, aside from being completely deserted, doesn't appear to have any inconsistencies with the real equivalent. Whoever trapped you in here did a good job. You walk through various buildings to try and find a difference, and are unsuccessful, until you walk into the Schwartz 112 lecture hall. Instead of the normal hall, you find a large screen displaying various locations across campus, as well as a panel with three buttons. The first, a large blue one, reads 'On'. The second, a large red button, reads 'Off', and the third, a smaller green lever, has the text 'Restart Simulation'.")
    time.sleep(0.5)
    print("""  A. On
  B. Off
  C. Restart Simulation

            """)
    choice = input(">>> ")
    if choice in answer_A:
        option_on()
    elif choice in answer_B:
        ending_10()
    elif choice in answer_C:
        time.sleep(0.5)
        intro()
    else:
        print(required)
        option_calm()

def option_on():
    print("Nothing Happens")
    time.sleep(0.5)
    print("""  A. Off
  B. Restart simulation

                """)
    choice = input(">>> ")
    if choice in answer_A:
        ending_10()
    elif choice in answer_B:
        time.sleep(0.5)
        intro()
    else:
        print(required)
        option_calm()

def option_freak():
    print("You have a quick freak-out session, where you scream, swear, cry, and utterly embarrass yourself despite no one being around to react. Afterwards, you regain your composure and look for some way out of the simulation.")
    time.sleep(2)
    option_calm()

# Hell No Path

def option_hell_no():
  print ("Hey, that’s not very nice. I was just trying to show you something cool.")
  time.sleep(0.5)
  print ("""  A. Did I stutter? Hell no.\n  B. Alright, I'm sorry.""")
  choice = input(">>> ")
  if choice in answer_A:
      option_Hell()
  elif choice in answer_B:
      option_sorry()
  else:
      print (required)
      option_hell_no()

#The Sorry Route:
def option_sorry():
    print ("A flash of bright light twinkles from above. You have been redeemed, and therefore have earned a wish. It shines like a star in the palm of your hand. Use it wisely.")
    time.sleep(0.5)
    print ("""  A. Wish for something.\n  B. Wish for more wishes.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_wish()
    elif choice in answer_B:
        option_morewishes1()
    else:
        print (required)
        option_sorry()

def option_wish():
    print ("Please input your wish")
    time.sleep(0.5)
    wishChoice = input(">>> ")
    time.sleep(0.5)
    print ("You attempt to wish for " + str(wishChoice) + " but fumble a bit and accidentally drop the wish. It rolls out of your hands and under the door.")
    time.sleep(0.5)
    print ("""  A. Run out to retrieve it.\n  B. Eh, it's not that big of a deal.""")
    choice = input(">>> ")
    if choice in answer_A:
        ending_11()
    elif choice in answer_B:
        theNextDay()
    else:
        print (required)
        option_wish()

def option_morewishes1():
    print ("It's impossible to wish for more wishes. Please actually wish for something.")
    time.sleep(0.5)
    print ("""  A. Wish for something.\n  B. Wish for more wishes.""")
    choice = input(">>> ")
    if choice in answer_A:
      option_wish()
    elif choice in answer_B:
        option_morewishes2()
    else:
        print (required)
        option_morewishes1()

def option_morewishes2():
    print ("Like I said before, you can't wish for more wishes. Please just wish for something. Anything.")
    time.sleep(0.5)
    print ("""  A. Wish for something.\n  B. Wish for more wishes.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_wish()
    elif choice in answer_B:
        ending_17()
    else:
        print (required)
        option_morewishes2()

# The Hell Route
def option_Hell():
    print ("If you like Hell so much, why don't you go there?")
    time.sleep(0.5)
    print ("""  A. Continue.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_intoHell()
    else:
        print (required)
        option_Hell()

def option_intoHell():
    print ("The voice in your head angrily teleports you into the deepest pit of Satan’s lair. In a visceral instant, your soul itself is dragged down into the pits below. Oh crap.")
    time.sleep(0.5)
    print ("""  A. Scout out the area.\n  B. Accept your eternal punishment.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hubHell()
    elif choice in answer_B:
        ending_12()
    else:
        print (required)
        option_intoHell()

# The Hell Hub

def option_hubHell():
    print ("You find yourself in a vast wasteland of fire and basalt. Lavafalls litter the sides of smoking cliffs, and the screams of burning souls ring across the landscape. To the east, you see a forest of flaming trees, too dense to spy into. To the north, a system of mountains, and to the west, a great cave. To the south is an ocean of molten metal, impossible to traverse without meeting a hot demise.")
    time.sleep(0.5)
    print ("""  A. Go East.\n  B. Go North.\n  C. Go West.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_eHell()
    elif choice in answer_B:
        option_nHell()
    elif choice in answer_C:
        option_wHell()
    else:
      print (required)
      option_hubHell()

# East Hell

def option_eHell():
    print ("You walk deep into the forest. It becomes too thick for any light to get through the branches, but the eternally lit embers on the leaves keeps the light level at a visible dim. You come up to a river of flowing lava without any way around it.")
    time.sleep(0.5)
    print ("""  A. Build a bridge.\n  B. Try to jump the river.\n  C. Go back.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_bridgeMake()
    elif choice in answer_B:
        option_riverJump()
    elif choice in answer_C:
        option_hubHell()
    else:
        print (required)
        option_eHell()

def option_bridgeMake():
    print ("You put together a pile of sticks and branches laying on the ground, and assemble them into a rudimentary bridge to cross the river with. However, the bridge looks very unstable, and not very fireproof.")
    time.sleep(0.5)
    print ("""  A. Use the bridge.\n  B. Try to jump the river.""")
    choice = input(">>> ")
    if choice in answer_A:
        ending_13()
    elif choice in answer_B:
        option_riverJump()
    else:
        print (required)
        option_bridgeMake()

def option_riverJump():
    print ("You back up as far as you can, and then run forwards, at the last second jumping over the river. You just barely make it to the other side, but trip on the landing and fall against the side of a mound of dirt. The dirt caves in, and you fall through the ground into a pit below.")
    time.sleep(0.5)
    print("""  A. Continue.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hellHole()
    else:
        print (required)
        option_riverJump()

# North Hell

def option_nHell():
    print ("You walk to the north, and after a few hours, are climbing one of the many mountains around. The red stone is coated in an ashen floor like black snow, and it becomes thicker and thicker the farther up you travel. The wind also becomes intense, despite no weather or real sky to be seen, and in a gale of immense power, you lose your footing and fall into a crevice between two large boulders.")
    time.sleep(0.5)
    print("""  A. Continue.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hellHole()
    else:
        print (required)
        option_nHell()

# The Hell Hole

def option_hellHole():
    print ("You wake up after the fall, dazed and with a broken leg, and unable to see the hole you fell through. You check your watch. You've been out for a while, and as everyone knows, if you spend 24 hours in hell, you're stuck there forever. You only have 5 hours, so you'd better get a move on. ")
    time.sleep(0.5)
    print ("""  A. Look at your options.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hOptions()
    else:
        print (required)
        option_hellHole()

def option_hOptions():
    if timeLeft == 0:
        ending_15()
    else:
        print ("Here are your options.\nYou have " + str(timeLeft) + " hours left.")
        time.sleep(0.5)
        print ("""  A. Read the wall glyphs.\n  B. Call for help.\n  C. Dig through the rock pile.\n  D. Try to climb out.\n  E. Tend to your wound.\n  F. Complete the ritual.""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hGlyph()
        elif choice in answer_B:
            option_hHelp()
        elif choice in answer_C:
            option_hDig()
        elif choice in answer_D:
            option_hClimb()
        elif choice in answer_E:
            option_hLeg()
        elif choice in answer_F:
            option_hRitual()
        else:
            print (required)
            option_hOptions()

def option_hGlyph():
    print ("You study the glyphs on the walls. They seem to be hinting at a ritual with gem stones.")
    global glyph
    glyph = True
    global timeLeft
    timeLeft -= 1
    time.sleep(0.5)
    print ("""  A. Look at your options""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hOptions()
    else:
        print (required)
        option_hGlyph()

def option_hHelp():
    print ("You call for help...\n\n...\n\nBut nobody came.")
    global timeLeft
    timeLeft -= 1
    time.sleep(0.5)
    print ("""  A. Look at your options""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hOptions()
    else:
        print (required)
        option_hHelp()

def option_hDig():
    if legHelp == True:
        print ("You find three glowing gemstones.")
        global gems
        gems = True
        global timeLeft
        timeLeft -= 1
        time.sleep(0.5)
        print ("""  A. Look at your options""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hOptions()
        else:
            print (required)
            option_hDig()
    else:
        print ("Your leg hurts too much.")
        time.sleep(0.5)
        print ("""  A. Look at your options""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hOptions()
        else:
            print (required)
            option_hDig()

def option_hLeg():
    print ("You tend to your wound. It feels better, like you can actually put pressure on it now.")
    global legHelp
    legHelp = True
    global timeLeft
    timeLeft -= 1
    time.sleep(0.5)
    print ("""  A. Look at your options""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hOptions()
    else:
        print (required)
        option_hLeg()

def option_hClimb():
    print ("You try to climb out, but are unable. It's just too steep.")
    global timeLeft
    timeLeft -= 1
    time.sleep(0.5)
    print ("""  A. Look at your options""")
    choice = input(">>> ")
    if choice in answer_A:
        option_hOptions()
    else:
        print (required)
        option_hClimb()

def option_hRitual():
    if glyph == True:
        if gems == True:
            ending_16()
        else:
            print ("You don't have the required materials.")
            time.sleep(0.5)
            print ("""  A. Look at your options""")
            choice = input(">>> ")
            if choice in answer_A:
                option_hOptions()
            else:
                print (required)
                option_hRitual()
    else:
        print ("You don't know how.")
        time.sleep(0.5)
        print ("""  A. Look at your options""")
        choice = input(">>> ")
        if choice in answer_A:
            option_hOptions()
        else:
            print (required)
            option_hRitual()

# West Hell

def option_wHell():
    print("You enter the cave, and begin descending downwards. Eventually, you come to a door made of solid obsidian. The door has a transcription that reads:\n\nSpeak the phrase of fire and flame\nSpeak the melting maiden's name\nHer tunic white and drooping down\nHer hair bright red, her neck, dull brown")
    time.sleep(0.5)
    print("""  A. Attempt to speak the passcode.\n  B.   Go back.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_speakPhrase()
    elif choice in answer_B:
        option_hubHell()
    else:
        print (required)
        option_wHell()

def option_speakPhrase():
    answer_Candle = ['candle','a candle','Candle','A candle','A Candle']
    print("Please speak the secret phrase.")
    time.sleep(0.5)
    choice = input(">>> ")
    if choice in answer_Candle:
        ending_14()
    else:
        print("Incorrect.")
        option_wHell()

#endings
def ending_1():
    print("You press the 'slide' button, and a sad slide-whistle sound plays. You hook the sound up to a microphone and send it towards the laser blast, which resonates at the same frequency as the whistle, destroying it and saving the planet. You rejoice as the mothership, defeated, returns to its galaxy of origin, and as you slowly descend to the surface of the planet, you think about how happy everyone will be that you saved the day. Although, before any celebration can take place, you're probably going to want to finish your homework.")
    time.sleep(0.5)
    print("You found Ending #1")
    possibleEndings[0] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_1()

def ending_2():
    print("You pose yourself in between a statue of a man with a pirate hat on, and a creature with too many tentacles. After about 30 seconds, a door opens, and a number of aliens wearing night-guard outfits come into the room. They immediately notice you, since they're not stupid and have seen this exhibit hundreds, if not thousands of times. They grab you and take you to an area of the ship where it is too dark to see anything. You fear the worst. However, just when you think all hope is lost, the lights come on and... surprise! It was all an elaborate ruse for your surprise birthday party! Not that the aliens aren't real, just that they're not trying to kill you or anything. You, your earth friends, and your new gelatinous martian pals eat cake and have a great time. ")
    time.sleep(0.5)
    print("You found Ending #2")
    possibleEndings[1] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print (requiredEnding)
        ending_2()

def ending_3():
    print("Yes is no. Up is left. Red is the number 5 and the letter o. You feel adrift in the infinite cosmos, "
          "endlessly floating in and out of existence, never once becoming a full, physical entity. Your essence "
          "becomes every star, every planet, every being in the vast multiverse, and yet you feel as if you've never "
          "left the room from which you attempted to egress. Your brain becomes singularity, a black hole of truth and emotion, "
          "and you evolve into a greater being. You merge with the sun and become godhead in its purest form.")
    time.sleep(0.5)
    print("You found Ending #3")
    possibleEndings[2] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print (requiredEnding)
        ending_3()

def ending_4():
    print("The temporal loop you're in that keeps allowing you to try again disintegrates, and your body is torn apart by the black hole that appears as a result of the timeline breaking.")
    time.sleep(0.5)
    print("You found Ending #4")
    possibleEndings[3] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_4()

def ending_5():
    print("You decide to face the consequences and head to your class without the required homework. Your professor, an 18 foot tall lizard, is not impressed, and both metaphorically and literally tears you to shreds.")
    time.sleep(0.5)
    print("You found Ending #5")
    possibleEndings[4] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_5()

def ending_6():
    print(
        "You close your eyes, but accidentally fall asleep. Seems you still had a few Zs left to catch. Eventually, you awake to find yourself in handcuffs being dragged away by a police officer. You're brought to court and found guilty of manslaughter and arson. Seems like you went on an unhinged rampage in your slumber. Guess you should have taken that melatonin after all.")
    time.sleep(0.5)
    print("You found Ending #6")
    possibleEndings[5] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_6()

def ending_7():
    print(
        "Deciding not to have anything for breakfast, you hurry to your next class. However, due to the nutrient imbalance inside of your frail body as a result of not eating breakfast, you trip, fall, and phase through the very bounds of reality itself. You wake up in an infinite maze of office chairs and broken printers, unable to escape for the rest of time.")
    time.sleep(0.5)
    print("You found Ending #7")
    possibleEndings[6] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_7()

def ending_8():
    print(
        "You run ahead to open the door, but it closes onto your finger, pinching your skin. This sudden jolt of pain wakes you up, for in fact, this was all a dream. You are actually a 6 month old Dairy Cow in Northern California. You proceed to the pasture, having gotten a long night of rest, and begin to chew your cud. Moo moo, moo moo moo.")
    time.sleep(0.5)
    print("You found Ending #8")
    possibleEndings[7] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_8()

def ending_9():
    print(
        "You use the bathroom again and again. You can't stop using the bathroom. Your fecal matter discovers a new element and invents a cure for cancer. Your bowels are studied by scientists for years to come. You become famous, known worldwide as the Stool Savior.")
    time.sleep(0.5)
    print("You found Ending #9")
    possibleEndings[8] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_9()

def ending_10():
    print("You press the button and-")
    print("Error: file not found \n"*10)
    time.sleep(0.5)
    print("You found Ending #10")
    possibleEndings[9] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_10()

def ending_11():
    possibleEndings[10] = True
    endings = countEndingsFound(possibleEndings)
    print ("As you run outside, you see another student pick up the wish. You call out for them to be careful, but they shush you and say 'I wish you would be a little quieter.'' The wish begins to glow, before sending itself flying into your face. A gleam of light sears your entire head, and suddenly you become acutely aware of the fact that you no longer possess a mouth. You begin to panic, and attempt to let out a cry of desparation, but alas, you have no mouth and you must scream.")
    time.sleep(0.5)
    print("You found Ending #11")
    time.sleep(0.5)
    print("You have found " + str(endings) + " out of 18")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print (requiredEnding)
        ending_11()

def ending_12():
    possibleEndings[11] = True
    endings = countEndingsFound(possibleEndings)
    print ("You lay down and wait for the demons and hell-hounds to have their way with your corpse, but that moment never comes. In face, the very fear of what is to come is the thing that haunts you for the rest of time, and you are never truly relaxed ever again, always waiting for an end that doesn't come.")
    time.sleep(0.5)
    print("You found Ending #12")
    time.sleep(0.5)
    print("You have found " + str(endings) + " out of 18")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print (requiredEnding)
        ending_12()

def ending_13():
    possibleEndings[12] = True
    endings = countEndingsFound(possibleEndings)
    print ("You attempt to cross the bridge, but halfway across, a burning piece falls, destroying the rest, and sending you into the lava, killing you instantly.")
    time.sleep(0.5)
    print("You found Ending #13")
    time.sleep(0.5)
    print("You have found " + str(endings) + " out of 18")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no():
        quit()
    else:
        print (requiredEnding)
        ending_13()

def ending_14():
    possibleEndings[13] = True
    endings = countEndingsFound(possibleEndings)
    print ("You speak the word candle, and the stone crumbles away to reveal a glowing red portal. You step inside and wake up, back in your bed, like nothing ever happened. You are relieved, and immediately drop out of college to dedicate your life to charity work and environment protection.")
    time.sleep(0.5)
    print("You found Ending #14")
    time.sleep(0.5)
    print("You have found " + str(endings) + " out of 18")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no():
        quit()
    else:
        print (requiredEnding)
        ending_14()

def ending_15():
    possibleEndings[14] = True
    endings = countEndingsFound(possibleEndings)
    print ("Your watch begins beeping. You check. 24 hours. 24 hours since you got teleported into Hell. And so, you lay down and accept the fact that you are stuck here forever, doomed to live out eternity here.")
    time.sleep(0.5)
    print("You found Ending #15")
    time.sleep(0.5)
    print("You have found " + str(endings) + " out of 18")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no():
        quit()
    else:
        print (requiredEnding)
        ending_15()

def ending_16():
    possibleEndings[15] = True
    endings = countEndingsFound(possibleEndings)
    print ("You place the gems in the correct positions, and suddenly, a purple portal opens up. You step inside and wake up, back in your bed, like nothing ever happened. You immediately book a therapy session, haunted by what you experienced, and continue to show lasting signs of PTSD well into adulthood.")
    time.sleep(0.5)
    print("You found Ending #16")
    time.sleep(0.5)
    print("You have found " + str(endings) + " out of 18")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no():
        quit()
    else:
        print (requiredEnding)
        ending_16()

def ending_17():
    possibleEndings[16] = True
    endings = countEndingsFound(possibleEndings)
    print ("You wish for more wishes. It doesn't work and you die instantly. That's what you get for not following the rules. Shame on you.")
    time.sleep(0.5)
    print("You found Ending #17")
    time.sleep(0.5)
    print("You have found " + str(endings) + " out of 18")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no():
        quit()
    else:
        print (requiredEnding)
        ending_17()

def ending_18():
    print(
        "You deactivate the device, and time goes back to normal. Your professor and everyone else walks into class and the lesson begins. You hand in your homework, and exit class feeling accomplished and fulfilled.")
    time.sleep(0.5)
    print("Congragulations! You have completed your homework!")
    time.sleep(0.5)
    print("You found Ending #18!")
    possibleEndings[17] = True
    time.sleep(0.5)
    endings = countEndingsFound(possibleEndings)
    print("You have found " + str(endings) + " out of 18 endings")
    time.sleep(0.5)
    print("Do you want to play again? [y/n]")
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        quit()
    else:
        print(requiredEnding)
        ending_18()

def countEndingsFound(list):
    counter = 0
    for i in list:
        if i == True:
            counter += 1
    return counter

intro()
