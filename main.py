# Jesse Chavez
# Final Project
# 12/4/2023

import time  #importing time moduel used tell final end time

starting_time = time.time()  #starting time using imported moduel, naming vairable

inventory = ['jerky',]  #creating list, giving it variable name inventory

print('Please note that at anytime you die, you will have \
to restart the program, unless you beat the game.')  #printing info to user
print()
print('Please note the answers are case sensative.')
print()

name = input(
    'Hello what is your name. ')  #Global use, Getting the players name


def main_menu():  #defining function 'main_menu', The games main menu 'Start or End'

  print()
  print(f'Hello, {name} and thank you for reading this work of fiction.'
        )  #Inputing name and introduction
  print()
  print('You open your eyes so see a very wierd sight.')
  print()
  print('You are inside a resturant sitting with someone you dont know.')
  print()
  print(
      'I will be your trusted narrator, who will be guiding you through this ordeal.'
  )
  print()
  print('My name is Francis, and I am the head butler of Mansion Venture.')
  print()
  print('Your possible destination, if you will have me.')
  print()

  start = input('Would you be willing to entrust yourself to me? Yes or No: ')

  print()
  print()

  if start == 'yes' or start == 'Yes':  #start of if statment for continue or ending the game
    print('Great! Lets us begin.')
    print('____________________________________________________________________________')
    print()

    main_story_intro()  #calling the starting the story section, 'main_story_intro'

  elif start == 'no' or start == 'No':  #start of if statment for continue or ending the game
    print('I am sorry to see you go, please enjoy your trip.')
    print('If you make it.')
    print('The End')
      #ending the game, reload to start over
      
  else:
    print('Invalid entry: ')
      
    main_menu() #calling function to restart section
      

def main_story_intro():  #defining function, Background story and build-up

  print('You wake up in a dindgy appartment, sitting on your couch.')
  print()
  print(
      'Your head is killing you, and you remember why you passed out last night.'
  )
  print()
  print(
      'You remember that you were sick and should have gone to the hospital.')
  print()
  print('But you know you dont have the money for that, \
  you are barely able to afford rent.')
  print()
  print("You can't ask your family for money.")
  print()
  print(
      'You left because you could not rely on them, they were horrible people.'
  )
  print()
  print('You already work two jobs to just live, \
  if you cannot work you will not get paid.')
  print()
  print(
      'Because of this, you have decided to rest and pray that you get better.'
  )
  print()
  print('Sudenlly you hear a nock at your door followed by a voice.')
  print()
  print(f'Delivery for one {name}, is anyone there!')    #using variable name to insert name
  print()
  print('You open the door and recieve your mail.')
  print()
  print('Junk, junk, junk, bill, .... and what is this?')
  print()
  print('A large manila folder with IMPORTANT written on it.')
  print()
  print('You decide to open it hopping that it wasnt anything bad.')
  print()
  print('As you read you start to understand that this folder is wierd \
  they are talking about your Grandfather, who you thought already dead.')
  print()
  print('It seems that who ever this is has left you a inheritance,\
  though there does seem to be some conditions.')
  print()
  print('There is a location and a date of an event you will have to go to,\
  in order to anything.')
  print()
  print('Out of no where you hear your cell phone go off')
  print()
  print(
      'You dont get to it in time, but you decide to listen to the voicemail.')
  print()
  print('It is your boss, you wonder why he is calling you?')
  print()
  print(f'Hey {name}, sorry to do this to you but you are being layed off.')
  print()
  print('We just dont have the money to keep you on board. Sorry.')
  print()
  print(
      'With that you decide that maybe it is a sign and will go to the event.')
  print()
  print()
  print(f'The screen fades to black, and {name} can be seen driving \
  to the event location')
  print()
  print('____________________________________________________________________________')

  main_story_intro_2()  #calling the function 'main_story_intro_2'


def main_story_intro_2():  #function 'main_story_intro_2'

  begin = input('Press enter to continue story')

  print()

  if begin == '':  #stop-gap to allow readers to catch up.
    print('You drive to the event location, and see an old, massive mansion.')
    print()
    print('It obviously run-down and needs a lot of remodeling.')
    print()
    print('You wonder why the event is happening here?')
    print()
    print('As you pull in to the large driveway you start to feel like someone\
    is watching you.')
    print()
    print('It is not a pleasent feeling.')
    print()
    print(
        'As you step out of the car, you feel the icy air rush into your lungs.'
    )
    print()
    print(
        '"This jacket is doing nothing to keep me warm, I better head in."')
    print('As you head to the door you notice that the windows are all boarded \
    up and the patio is bearly holding together.')
    print()
    print(
        'Why would anyone host an event in a place like this? You ask your self.'
    )
    print()
    print('Do you knock on the door or just hop in your car and leave?')
    print()
    print('____________________________________________________________________________')

    knock = input('Knock Yes or No?:  ')  # input for if-else statment, variable named knock
    
    print()

    if knock == 'Yes' or knock == 'yes':  #continuing the story, if statment with or statment
      print(
          'You knock on the door and a old man wearing a butlers outfit answers.'
      )
      print()
      print(f'Hello my name is Francis, glad to finally meet you {name}.')
      print()
      print('I am the butler, well former buttler of Venture Manor.')
      print()
      print('Let us talk to about your inheritance.')
      print()
      print('Your Grandfather left you everything here: the mansion, his dog, \
      and his fortune.')
      print()
      print(
          'In order for you to obtain your inheritance you must stay in here for\
      the night.')
      print()
      print(
          'Your Grandfather was a superstisious man, who believed that over time\
      anything can gain life.')
      print()
      print(
          'The energy you give of by living seeps into the house, and the house\
      absorbs the energy.')
      print()
      print('A house filled with positive emotions will feel welcoming.')
      print()
      print('A house will negative emotions will feel dark and unwelcoming.')
      print()
      print('""I that why I feel like someone is watching me?"" you say.')
      print()
      print('""O, that is just the house getting to know you,"" says the butler \
          while smiling at you.')
      print()
      print('"OK, come on in and I will leave and let \
      you get settled!" Francis exclaims.')
      print()
      print('He hands you the keys to the front door as he leaves.')
      print()
      print('""Have a good night!"" He yells as he heads towards his car.')
      print()
      print('You see him drive out of the driveway, and head inside \
      to get confortable.')
      print()

      proceed = input('Press enter to continue: ')  #stop-gap so you can finish reading, variable
      print()

      if proceed == '':  #if calling the function 'main_inside'
        main_inside()

      else:  #else statment for restarting the funtion 'main_inside'
        main_inside()

    else:  #else statment that ends the game
      print()
      print('Quickly you return to your car.')
      print()
      print('You hop in your car and drive away.')
      print()
      print('As you drive away you think to yourself.')
      print()
      print('You dont know what you were thinking coming to this event, it all \
      feels to wierd.')
      print()
      print('You are glad you got out while you could.')
      print()
      print(
          'But now you are back to square one and might lose your appartment.')
      print('As you drive away you feel as you have gotten nowhere.')
      print()
      print('THE END')
      quit()

  else:
    main_menu()      #calling the function main menu


def main_inside():  #story section 3 inside the house

  print('You find yourself inside the foyer.')
  print()
  print('The inside of the property looks well maintained, though something\
  feels off.')
  print()
  print('You feel as though you are being watched again.')
  print()
  print('You decide to forget about the feeling and decide what to do next.')
  print()
  print('You feel exausted after all of that traveling, you are dragging your \
  feel as you walk.')
  print()
  print('It is getting late, you really should find someplace to sleep.')
  print()
  print('You see that the poyer is connected to the living room and \
  the dinning room.')
  print()
  print('Hmm....the living room may have a couch you could sleep on, \
  should I head there or search the dinning room?')
  print()
  print('____________________________________________________________________________')

  while True:  # while statment to loop back an invalid input

    choice = input(
        'Living Room or Dinning Room?: ')  #naming the variable choice via input
    print()

    if choice == 'Living Room' or choice == 'living room':  #if statment for choice 1
      print()
      print('You step into the living room.')
      print()
      print('You notice a large couch placed right infront of a fireplace.')
      print()
      print(
          'It seems Francis was nice enought to start the fire for your stay.')
      print()
      print(
          'Maybe you should think about rehiring him, that is if he wants to be.'
      )
      print()
      print(
          'As you appoach the couch you see a large dog laying infront of the fire.'
      )
      print()
      print('It is a old german shephard, most likely your grandfathers.')
      print()
      print('You notice a collar that has his name on it.')
      print()
      print('It reads ""Bear.""')
      print()
      print(
          '""Huh,"" you mutter to your self, and the dog seems to notice you.')
      print()
      print('It gives you a unfriendly stare and proceeds to lay back down.')
      print()
      print(
          'You remember that you have some beef jerky left over from the drive.'
      )
      print()
      print('Maybe you can earn its trust be feeding it.')
      print()
      print('Do you wish to feed the dog?')
      print()
      print('____________________________________________________________________________')

      decision = input('Yes or No:  ')  #start of an if-else statment

      while True:  #starting a while loop for variable decision

        if decision == 'Yes' or decision == 'yes':  #decision if statment
          print()
          print('You decide to feed the dog.')
          print()
          print('You walk up to the dog and slowly walk over to it.')
          print()
          print('The dog looks up at you as your appoach.')
          print()
          print('You notice it staring at the jerky hungerly.')
          print()
          print('""Do you want some,"" you say in a soft voice.')
          print()
          print('The old dog wags its tail and eats your offering graciously.')
          print()
          print('You notice Bear is now looking at you waiting for something.')
          print()
          print('You stick your hand out and Bear eagerly licks it.')
          print()
          print('It seems you have made a new friend.')
          print()

          inventoryadd(
              'happy_dog')  #adding argument happy_dog to inventory list

          break

        elif decision == 'No' or decision == 'no':  #decision elif statment
          print('You decide not to feed the dog.')
          print()
          print('You feel as though you missed out on something')
          print()
          break

        else:  #decision else statment for invalid answer
          print('Restarting the section please remember to type Yes or No.')

          main_inside()  #Calling function to restart section
          

      break

    elif choice == 'Dinning Room' or choice == 'dinning room':  #elif statment for choice 2
      print()
      print('You step into the dining room.')
      print()
      print('You are entranced by the elaborate furniture.')
      print()
      print(
          'Your eyes are constantly closing and you are yawning as you walk.')
      print()
      print('As you walk you do not notice a dog toy laying infront of you.')
      print()
      print(
          'You step on the dog toy and yell as your foot goes flying forward.')
      print()
      print('As you fall back you wish you had never come to this place.')
      print()
      print(
          'You head hits the marble tile flooring and your vision goes black.')
      print()
      print('You have died. THE END. ')
      print()
      quit()

    else:  #else statment for invalid input
      print()
      print('Please enter a valid location: Living Room or Dinning Room')
      continue

  print('After the day you have had you feel the couch calling to you.')
  print()
  print(
      'You put your head down and instantly fall asleed, warm and confortable.'
  )
  print()
  print('____________________________________________________________________________')

  main_story_night()  #calling on function main_story_night


def main_story_night():  #defining function for main story for night

  print('You wake up suddenly after heading a loud noise comming\
  from the dinning room')
  print()
  print('You think it was the sound of glass shattering.')
  print()
  print('You see that Bear has gotten up is growling in that direction.')
  print()
  print('You decide to go and see what happened.')
  print()
  print('Most likely one of the old windows finally broke, nothing\
  to be worried about.')
  print()
  print('You remember your olf pocket knife inside your bag.')
  print()
  print('Do you grab it?')
  print()

  decision = input('Yes or No:  ')  #input variable for pocket_knife item

  if decision == 'Yes' or decision == 'yes':  #if statment for pocket_knife
    print('You grab the knife.')
    print()
    inventoryadd('pocket_knife')

  else:  #else statment for pocket_knife
    print('You decide not to grab the knife.')
    print()

  print('You step out into the foyer and suddenly you hear footsteps.')
  print()
  print('The foot steps seem to be coming towards you.')
  print()
  print('Do you wish to go back into the living room or go forwards into\
  the dinning room?')
  print()

  decision = input(
      'Backwards or Forwards?:  ')  #input descision for loop if/else statment

  print()

  while True:  #starting the loop

    if decision == 'Backwards' or decision == 'backwards':  # if statment for decision
      print('You decide to go back into the living room.')
      print()
      print(
          'As you peer through the door looking at the entrance to the dinning room\
      you see shape barely visiable approaching the foyer.')
      print()
      print('You close the door to the foyer, but it makes a noise.')
      print()
      print('Just as you finish closing the door, you hear footsteps.')
      print()
      print('They are loud and are rushing towards you.')
      print()
      print('You are feeling terrified, but it is a heavy oak door.')
      print()
      print(
          'Unless they have an ax, there is no way they are making it through.'
      )
      print()
      print('Just as you think that you head a loud bang, and feel\
      the door buckle.')
      print()
      print('As you take a step back in fear, you hear it again.')
      print()
      print('""BAM!"" The door buckles again, whatever it is, you know\
      it will be getting in soon enought.')
      print()
      print('You hear bear growling and barking.')
      print()
      print('""BAM!"" The door has finally given way.')
      print()
      print('In steps a man about 7 feet tall wearing a mask.')
      print()
      print(
          '""Sorry friend, thought this house was abandoned after the old man died.""\
      says the man in a deep voice.')
      print()
      print('""No witnesses, sorry it had to be this way,"" continues the man')
      print()
      print('He starts walking towards you')
      print()

      if 'pocket_knife' in inventory and 'happy_dog' in inventory:  #if statment for list inventory using arguments 'pocket knife' and 'happy dog'
        print('You remember you grabed your old pocket knife, it isnt much,\
        but it will have to do.')
        print()
        print(
            'As you lift you knife in defence you notice Bear acting strange.')
        print()
        print('He is circling the intruder.')
        print()
        print(
            'The indtruder hasnt noticed him yet, and you wonder what he is doing?'
        )
        print()
        print('The induder laughs as he sees you wield the small knife.')
        print()
        print('""Hah, what are you going to do with that?"" He asks?')
        print()
        print('Just as he says that Bear attacks him from behind.')
        print()
        print(
            'The indruder screams in pain as his leg is ripped appart by the dog.'
        )
        print()
        print('""AHHHH,"" you hear him scream.')
        print()
        print('You run up to him and stab him multiple times,\
              each more frantic then the last.')
        print()
        print('Finaly the intruder has stopped screaming, and bear has\
        stopped attacking.')
        print()
        print('You rush over to the phone calling the local police franticy.')
        print()
        print('""We will be there shortly, please stay on the line.""\
        says the dispacher.')
        print()
        print('You stay on the line, beathing heavily while petting Bear.')
        print()
        print('____________________________________________________________________________')

        story_ending_1()  #calling the function story_ending_1

      elif 'pocket_knife' in inventory and 'happy_dog' not in inventory:  #if statment for list inventory using arguments 'pocket knife' and 'happy dog'
        print('You remember you grabed your old pocket knife, it isnt much,\
        but it will have to do.')
        print()
        print(
            'As you lift you knife in defence you notice Bear acting strange.')
        print('He is circling the intruder.')
        print()
        print(
            'The intruder hasnt noticed him yet, and you wonder what the dog is doing?'
        )
        print()
        print('The induder laughs as he sees you wield the small knife.')
        print()
        print('""Hah, what are you going to do with that?"" He asks?')
        print()
        print('Just as he says that Bear runs out of the room.')
        print()
        print(
            '""Huh, guess he wasnt your dog,"" says the intruder while smirking.'
        )
        print()
        print(
            'He procedes to grab your knife and smash your head against the wall.'
        )
        print()
        print('As you start to lose consiousness you think to your self,\
        ""Maybe I should have fed the dog.""')
        print()
        print('____________________________________________________________________________')

        story_ending_2()  #calling the function story_ending_2
        break  #stoping the loop

      else:  #else statment for loop
        print('Your story has come to a close.')
        print()
        print('You have died.')
        print()
        print('____________________________________________________________________________')

        story_ending_2()  #calling the function story_ending_2

        break  #stoping the loop

    elif decision == 'Forwards' or decision == 'forwards':  #else if statment for decision
      print('You decide to go forward towards the dining room.')
      print()
      print(
          'As you peer through the door looking at the entrance to the dinning room\
      you see shape barely visiable approaching the foyer.')
      print()
      print('You close the door to the foyer, but it makes a noise.')
      print()
      print('Just as you finish closing the door, you hear footsteps.')
      print()
      print('They are loud and are rushing towards you.')
      print()
      print('You are feeling terrified, but it is a heavy oak door.')
      print()
      print(
          'Unless they have an ax, there is no way they are making it through.'
      )
      print()
      print('Just as you think that you hear a loud bang, and feel\
      the door buckle.')
      print()
      print('As you take a step back in fear, you hear it again.')
      print()
      print('""BAM!"" The door buckles again and whatever it is, you know\
      it will be getting in soon enough.')
      print()
      print('You hear bear growling and barking.')
      print()
      print('""BAM!"" The door has finally given way.')
      print()
      print('In steps a man about 7 feet tall wearing a mask.')
      print()
      print(
          '""Sorry friend, thought this house was abandoned after the old man died.""\
      says the man in a deep voice.')
      print()
      print('""No witnesses, sorry it had to be this way,"" continues the man')
      print()
      print('He starts walking towards you')
      print()

      if 'pocket_knife' in inventory and 'happy_dog' in inventory:  #if statment for list inventory items
        print('You remember you grabed your old pocket knife, it isnnt much,\
        but it will have to do.')
        print()
        print(
            'As you lift you knife in defence you notice Bear acting strange.')
        print()
        print('He is circling the intruder.')
        print()
        print(
            'The indtruder hasnt noticed him yet, and you wonder what he is doing?'
        )
        print()
        print('The induder laughs as he sees you wield the small knife.')
        print()
        print('""Hah, what are you going to do with that?"" He asks?')
        print()
        print('Just as he says that Bear attacks him from behind.')
        print()
        print(
            'The indruder screams in pain as his leg is ripped appart by the dog.'
        )
        print()
        print('""AHHHH,"" you hear him scream.')
        print()
        print('You run up to him and stab him multiple times,\
              each more frantic then the last.')
        print()
        print('Finaly the intruder has stopped screaming, and bear has\
        stopped attacking.')
        print()
        print('You rush over to the phone calling the local police franticy.')
        print()
        print('""We will be there shortly, please stay on the line.""\
        says the dispacher.')
        print()
        print('You stay on the line, beathing heavily while petting Bear.')
        print()
        print('____________________________________________________________________________')

        story_ending_1()  #calling the function story_ending_1

      elif 'pocket_knife' in inventory and 'happy_dog' not in inventory:  #if
        print('You remember you grabed your old pocket knife, it isnt much,\
        but it will have to do.')
        print()
        print(
            'As you lift you knife in defence you notice Bear acting strange.')
        print('He is circling the intruder.')
        print()
        print(
            'The intruder hasnt noticed him yet, and you wonder what the dog is doing?'
        )
        print()
        print('The induder laughs as he sees you wield the small knife.')
        print()
        print('""Hah, what are you going to do with that?"" He asks?')
        print()
        print('Just as he says that Bear runs out of the room.')
        print()
        print(
            '""Huh, guess he wasnt your dog,"" says the intruder while smirking.'
        )
        print()
        print(
            'He procedes to grab your knife and smash your head against the wall.'
        )
        print()
        print('As you start to lose consiousness you think to your self,\
        ""Maybe I should have fed the dog.""')
        print()
        print('____________________________________________________________________________')

        story_ending_2()  #calling the function story_ending_2

        break  #stoping the loop

      else:
        print('You have nothing to fight back with.....this maybe the end.')
        print()
        print('As the intruder smashes your head you can only think,\
        ""I wish I had never revieved that piece of mail."""')
        print()
        print('Your story has come to a close.')
        print()
        print('You have died.')
        print('____________________________________________________________________________')

        story_ending_2()  #calling the function story_ending_2

    else:  #else statment for invalid entry of variable decision
      print('Please enter a valid option: Backwards or Forwards')

      main_story_night()


def story_ending_1():  #function for story enging 1

  print('Soon enought the police are at your front door.')
  print()
  print('As they see the sceen, they call in reinforcement.')
  print()
  print('""Are you all right?"" asks the Officer.')
  print()
  print('You spend the next 20 minutes retelling the event fo tonight\
  never missing a single detail.')
  print()
  print('After finishing with the officer you sit down on the porch.')
  print()
  print('As you sit there Bear sits down next to you and begs to be pet.')
  print()
  print('The sun is barly peaking over the horison as you sit there.')
  print()
  print('You can see the butlers car pulling into the driveway.')
  print()
  print(
      '""I rushed over as soon as I had heard what happened,"" exclaimed Francis.'
  )
  print()
  print('""I am so sorry this happened, your grandfather never wanted\
  anything like this to happen,"" he further states.')
  print()
  print('""He was just fond of jokes, and that whole story I told you was\
  his idea to have one final joke.""')
  print()
  print('You look at his horrified face, and you believe Francis'
        ' words.')
  print()
  print('""Dont worry,"" you state as he finally seems to be caling down.')
  print()
  print('Right as he seems to be ready to talk again a officer appoches you.')
  print()
  print(
      '""Well Ill be, you just took down a serial killer,"" says the officer.')
  print()
  print('""We have been looking for him for ages, but he never left a clue\
  besides some finger prints that were not in our databases.""')
  print()
  print('You realize how lucky you where.')
  print()
  print('As you sit down hugging Bear, you thank him for helping you.')
  print()
  print('""I appreciate your help, I am keeping you,"" you wisper to the dog.')
  print()
  print('Congradulations you survived the night.')
  print()
  print('THE END')
  print()

  end_time = time.time()  #ending timer from time moduel

  time_taken = end_time - starting_time  #calculating time taken

  print(f'Your final completion time is: {time_taken: .2f} seconds')  #printing out end timer
  print('____________________________________________________________________________')

  restart = input('Restart yes or no?')  #naming restart variable
  print('____________________________________________________________________________')
  print()
  

  if restart == 'Yes' or restart == 'yes':  #if statement for restarting the game
    main_menu()

  else:  #else statment for quiting game
    quit()


def story_ending_2():  #calling story ending 2

  print('The next day Francis, the butler, knocks on the door to the mansion.')
  print()
  print(f'That is wierd, {name} isnt answers and the front window\
  is broken,"" wispers Francis ')
  print()
  print(
      'As he uses the spare key and enters the house he is hit with a copper oddur.'
  )
  print()
  print(
      'As he sniffs in disgust he notices the broken door to the living room.')
  print()
  print('Francis rushes in to see your body on the floor surrounded by blood.')
  print()
  print('He lets out a frantic scream as he rushed to the phone.')
  print()
  print('Five minutes later the police arrive at the mansion.')
  print()
  print(
      'As Francis tell the officers all he knows, the investigation unit arives.'
  )
  print()
  print('Ten minutes later, the investigators let the officers know that\
  the serial murderer has stuck again.')
  print()
  print('""Another one for the morgue,"" says the officer as they had\
  back to their cars.')
  print()
  print('""Why...."" wispers the voice of a hopeless old man.')
  print()
  print('Francis starts crying as he heads towards his car.')
  print()
  print('THE END')
  print('____________________________________________________________________________')
  
  end_time = time.time()  #naming variable for ending timer from time moduel

  time_taken = end_time - starting_time  #calculating time taken

  print(f'Your final completion time is: {time_taken: .2f} seconds')  #printing out end timer
  print('____________________________________________________________________________')
  print()

  restart = input('Restart yes or no?')    # naming input variable for restart
  print('____________________________________________________________________________')

  if restart == 'Yes' or restart == 'yes':    #start of if/else for restarting game
    main_menu()

  else:
    quit()

def inventoryadd(item):  #function to add items to inventory
  inventory.append(item)  #appending the list inventory with variable 'item'

if __name__ == '__main__':  #Calling the Main menu to start
  main_menu()
