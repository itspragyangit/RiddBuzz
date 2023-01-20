"""
In this project we've created a mini game for solving riddles. This game will give you a better experience of text riddle solving in extremely minimal ways despite having few questions.
We've used all python internal modules for the project(game)
"""

import time
#we're importing the time module so that we can use the sleep() function for time delay

#WELCOME CODE

print("╔═════════*.·:·.☽✧    ✦    ✧☾.·:·.*═════════╗")
time.sleep(1)
print("                                            RiddBuzz             ")
time.sleep(1)
print("╚═════════*.·:·.☽✧    ✦    ✧☾.·:·.*═════════╝")
time.sleep(1)
print("•• ━━━━━━━━━━━━━ ••●•• ━━━━━━━━━━━━━ ••")
time.sleep(1)
name = input("Before starting off with the game please enter your name 『••✎••』: ")
time.sleep(0.7)
print("\nHey ", name," ! Welcome to RiddBuzz ♡‧₊˚ ")
time.sleep(1)
print("\nAll you need to do is answer the riddles and remember all the answers \nshould be in ✩CAPITAL LETTERS✩")
time.sleep(1)
print("•• ━━━━━━━━━━━━━ ••●•• ━━━━━━━━━━━━━ ••")
time.sleep(1.5)
print("✏ This game will have 3 levels : Beginner , Intermediate and Hard.")
time.sleep(2.5)
print("✏ For every Beginner level questions you get 10 points each with a total of 9 questions.")
time.sleep(2.8)
print("✏ For every Intermediate level questions you get 15 points each with a total of 10 questions.")
time.sleep(2.8)
print("✏ For every Hard level questions you get 20 points each with a total of 8 questions.")
time.sleep(2.8)
print("✏ Total of 400 points")
time.sleep(1)
print("✏ At last we'll show you your score ⚝")
time.sleep(1.2)
print("✏ Let's Begin in")
time.sleep(1)
for i in range(3):  
  print(3-i,("."*(3-i)))
  time.sleep(1)
print("Lessssgooooo... ✧ଘ(੭◌ˊᵕˋ)੭* ੈ♡‧₊˚")

#BODY CODE

lifeBeg , lifeInt , lifeHrd = 3 , 5 , 4
lifeCountBeg , lifeCountInt , lifeCountHrd = 0 , 0 , 0
countTot , countTot1, countTot2=0 , 0 , 0 
ch = 0

"""
FOR BEGINNER LEVEL'S CODE
"""

beginnerLst = ["What goes up but never comes down?","What month of the year has 28 days?","What can’t talk but will reply when spoken to?","What has many keys but can’t open a single lock?","I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?" ,"Where does today come before yesterday?","What is always in front of you but can’t be seen?","There was this competition where the contestants had to hold 'something'. At the end of the event, the winner was a person who was physically disabled (he had no hands and no any feet)! What was that 'something'?","What kind of coat is always wet when you put it on?"] #List containing all the beginner level questions
print("Beginner's Level First <3")
time.sleep(0.5)
print("✏ As mentioned above there are 9 questions.")
time.sleep(2.5)
print("✏ Type your answer only when 'Enter your answer:' appears.")
time.sleep(2.5)
print("✏ You'll get 3 life line but once you redeem all of them you won't be able to have second chances but you can answer them once only ... Take lifelines carefully")
time.sleep(2.9)
time.sleep(0.9)


for i in range(len(beginnerLst)):
  x = beginnerLst[i]
  print("\n",x)
  time.sleep(2)
  a = input("Enter your answer:")
  if x == beginnerLst[0]:
    if a == "AGE":
      print("Congratulations! you got it right")
      countTot += 10
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountBeg += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: You have no control over it")
        ans = input("Enter your answer again:")
        if ans == "AGE":
          print("Congratulations! you got it right")
          countTot += 10
        else:
          print("Sorry but you couldn't crack it.... It was AGE")
      else:
        print("Issoke, the correct answer to the question is AGE")
  if x == beginnerLst[1]:
    if a == "ALL":
      print("Congratulations! you got it right")
      countTot += 10
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountBeg += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: Think about no. of days in each month")
        ans = input("Enter your answer again:")
        if ans == "ALL":
          print("Congratulations! you got it right")
          countTot += 10
        elif ans == "FEBRUARY":
          print("Ahh... It can even have 29.... Every month has 28 days :'(")
        else:
          print("Sorry but you couldn't crack it.... It was ALL")
      else:
        print("Issoke, the correct answer to the question is ALL")
  if x == beginnerLst[2]:
    if a == "ECHO":
      print("Congratulations! you got it right")
      countTot += 10
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountBeg += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: Sound has something to do with it")
        ans = input("Enter your answer again:")
        if ans == "ECHO":
          print("Congratulations! you got it right")
          countTot += 10
        else:
          print("Sorry but you couldn't crack it.... It was ECHO")
      else:
        print("Issoke, the correct answer to the question is ECHO")
  if x == beginnerLst[3]:
    if a == "PIANO":
      print("Congratulations! you got it right")
      countTot += 10
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountBeg == lifeBeg:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was PIANO")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountBeg += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: Sound has something to do with it")
          ans = input("Enter your answer again:")
          if ans == "PIANO":
            print("Congratulations! you got it right")
            countTot += 10
          else:
            print("Sorry but you couldn't crack it.... It was PIANO")
        else:
          print("Issoke, the correct answer to the question is PIANO")
  if x == beginnerLst[4]:
    if a == "BREATHE":
      print("Congratulations! you got it right")
      countTot += 10      
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountBeg == lifeBeg:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was BREATHE")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountBeg += 1
          print("You lost your lifeline :'( but we got a hidden gem for you <3")
          time.sleep(0.5)
          print("HINT: We can't live without doing it")
          ans = input("Enter your answer again:")
          if ans == "BREATHE":
            print("Congratulations! you got it right")
            countTot += 10
          else:
            print("Sorry but you couldn't crack it.... It was BREATHE")
        else:
          print("Issoke, the correct answer to the question is BREATHE")
  if x == beginnerLst[5]:
    if a == "DICTIONARY":
      print("Congratulations! you got it right")
      countTot += 10
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountBeg == lifeBeg:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was DICTIONARY")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountBeg += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: Each and every word is here")
          ans = input("Enter your answer again:")
          if ans == "DICTIONARY":
            print("Congratulations! you got it right")
            countTot += 10
          else:
            print("Sorry but you couldn't crack it.... It was DICTIONARY")
        else:
          print("Issoke, the correct answer to the question is DICTIONARY")
  if x == beginnerLst[6]:
    if a == "FUTURE":
      print("Congratulations! you got it right")
      countTot += 10
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountBeg == lifeBeg:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was FUTURE")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountBeg += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: For some it's bright and some thinks that it's dark")
          ans = input("Enter your answer again:")
          if ans == "FUTURE":
            print("Congratulations! you got it right")
            countTot += 10
          else:
            print("Sorry but you couldn't crack it.... It was FUTURE")
        else:
          print("Issoke, the correct answer to the question is FUTURE")
  if x == beginnerLst[7]:
    if a == "BREATHE":
      print("Congratulations! you got it right")
      countTot += 10
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountBeg == lifeBeg:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was BREATHE")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountBeg += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: You have seen this previously here")
          ans = input("Enter your answer again:")
          if ans == "BREATHE":
            print("Congratulations! you got it right")
            countTot += 10
          else:
            print("Sorry but you couldn't crack it.... It was BREATHE")
        else:
          print("Issoke, the correct answer to the question is BREATHE")
  if x == beginnerLst[8]:
    if a == "PAINT":
      print("Congratulations! you got it right")
      countTot += 10
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountBeg == lifeBeg:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was PAINT")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountBeg += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: What do we do with colours?")
          ans = input("Enter your answer again:")
          if ans == "PAINT":
            print("Congratulations! you got it right")
            countTot += 10
          else:
            print("Sorry but you couldn't crack it.... It was PAINT")
        else:
          print("Issoke, the correct answer to the question is PAINT")
          time.sleep(1)
          print("Your total score till now is: ",countTot)
          time.sleep(2)
    print("Your total score in this round is:",countTot)
    time.sleep(0.8)
         
"""
FOR INTERMEDIATE LEVEL'S CODE
"""

intermediateLst = ["What belongs to you but other people use it more than you?","What runs, but never walks. Murmurs, but never talks. Has a bed, but never sleeps. And has a mouth, but never eats?","What is seen in the middle of March and April that can't be seen at the beginning or end of either month?","What is 3/7 chicken, 2/3 cat and 2/4 goat?","What five letter word stays the same when you take away the first, third, and last letter?","You’re in a race and you pass the person in second place. What place are you in now?","What is at the end of the rainbow?","What can go through glass without breaking it?","What has ten letters and starts with gas?","How many letters are in the alphabet?"] #List containing all the intermediate level questions

print("\nMoving on to the Intermediate Level ☆ﾟ")

print("✏ As mentioned above there are 10 questions.")
time.sleep(2.5)
print("✏ Type your answer only when 'Enter your answer:' appears.")
time.sleep(2.5)
print("✏ You'll get 5 life line but once you redeem all of them you won't be able to have second chances but you can answer them once only ... Take lifelines carefully")
time.sleep(2.9)
time.sleep(0.9)

for i in range(len(intermediateLst)):
  x = intermediateLst[i]
  print("\n",x)
  time.sleep(2)
  a = input("Enter your answer:")
  x = intermediateLst[i]
  if x == intermediateLst[0]:
    if a == "NAME":
      print("Congratulations! you got it right")
      countTot1+= 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountInt += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: It's given after you are born")
        ans = input("Enter your answer again:")
        if ans == "NAME":
          print("Congratulations! you got it right")
          countTot1 += 15
        else:
          print("Sorry but you couldn't crack it.... It was NAME")
      else:
        print("Issoke, the correct answer to the question is NAME")
  if x == intermediateLst[1]:
    if a == "RIVER":
      print("Congratulations! you got it right")
      countTot1+= 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountInt += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: Geography related")
        ans = input("Enter your answer again:")
        if ans == "RIVER":
          print("Congratulations! you got it right")
          countTot1 += 15
        else:
          print("Sorry but you couldn't crack it.... It was RIVER")
      else:
        print("Issoke, the correct answer to the question is RIVER")
  if x == intermediateLst[2]:
    if a == "R":
      print("Congratulations! you got it right")
      countTot1 += 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountInt += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: It's a letter")
        ans = input("Enter your answer again:")
        if ans == "R":
          print("Congratulations! you got it right")
          countTot1 += 15
        else:
          print("Sorry but you couldn't crack it.... It was R")
      else:
        print("Issoke, the correct answer to the question is R")
  if x == intermediateLst[3]:
    if a == "CHICAGO":
      print("Congratulations! you got it right")
      countTot1+= 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountInt += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: Break it down")
        ans = input("Enter your answer again:")
        if ans == "CHICAGO":
          print("Congratulations! you got it right")
          countTot1 += 15
        else:
          print("Sorry but you couldn't crack it.... It was CHICAGO")
      else:
        print("Issoke, the correct answer to the question is CHICAGO")
  if x == intermediateLst[4]:
    if a == "EMPTY":
      print("Congratulations! you got it right")
      countTot1 += 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountInt += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: Sounds exactly what's left")
        ans = input("Enter your answer again:")
        if ans == "EMPTY":
          print("Congratulations! you got it right")
          countTot1 += 15
        else:
          print("Sorry but you couldn't crack it.... It was EMPTY")
      else:
        print("Issoke, the correct answer to the question is EMPTY")
  if x == intermediateLst[5]:
    if a == "SECOND":
      print("Congratulations! you got it right")
      countTot1 += 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountInt == lifeInt:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was SECOND")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountInt += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: Overtaking results you in the same place")
          ans = input("Enter your answer again:")
          if ans == "SECOND":
            print("Congratulations! you got it right")
            countTot1 += 15
          else:
            print("Sorry but you couldn't crack it.... It was SECOND")
        else:
          print("Issoke, the correct answer to the question is SECOND")
  if x == intermediateLst[6]:
    if a == "W":
      print("Congratulations! you got it right")
      countTot1 += 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountInt == lifeInt:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was W")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountInt += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: It's a letter")
          ans = input("Enter your answer again:")
          if ans == "W":
            print("Congratulations! you got it right")
            countTot1 += 15
          else:
            print("Sorry but you couldn't crack it.... It was W")
        else:
          print("Issoke, the correct answer to the question is W")
  if x == intermediateLst[7]:
    if a == "LIGHT":
      print("Congratulations! you got it right")
      countTot1 += 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountInt == lifeInt:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was LIGHT")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountInt += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: Physics is the key")
          ans = input("Enter your answer again:")
          if ans == "LIGHT":
            print("Congratulations! you got it right")
            countTot1 += 15
          else:
            print("Sorry but you couldn't crack it.... It was LIGHT")
        else:
          print("Issoke, the correct answer to the question is LIGHT")
  if x == intermediateLst[8]:
    if a == "AUTOMOBILE":
      print("Congratulations! you got it right")
      countTot1 += 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountInt == lifeInt:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was AUTOMOBILE")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountInt += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: It's not a necessity but a luxury that almost everyone has and starts with AUTO and ends with a thing our generation can't live without")
          ans = input("Enter your answer again:")
          if ans == "AUTOMOBILE":
            print("Congratulations! you got it right")
            countTot1+= 15
          else:
            print("Sorry but you couldn't crack it.... It was AUTOMOBILE")
        else:
          print("Issoke, the correct answer to the question is AUTOMOBILE")
  if x == intermediateLst[9]:
    if a == "EIGHT":
      print("Congratulations! you got it right")
      countTot1 += 15
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountInt == lifeInt:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was EIGHT")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountInt += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: Number")
          ans = input("Enter your answer again:")
          if ans == "EIGHT":
            print("Congratulations! you got it right")
            countTot1 += 15
          else:
            print("Sorry but you couldn't crack it.... It was EIGHT")
        else:
          print("Issoke, the correct answer to the question is EIGHT")
          time.sleep(1)
          print("Your total score till now is: ",countTot1)
          time.sleep(2)
    print("Your total score in this round is:",countTot1)
    time.sleep(0.8)


"""
FOR HARD LEVEL'S CODE
"""

hardLst = ["Two men are in a desert. They both have backpacks on. One of the guys is dead. The guy who is alive has his backpack open and the guy who is dead has his backpack closed. What is in the dead man’s backpack?","What is it that given one, you’ll have either two or none?","I am something people celebrate or resist. I change people’s thoughts and lives. I am obvious to some people but, to others, I am a mystery. What am I?","Nobody has ever walked this way. Which way is it?","I have three feet, but I can’t stand without leaning. I have no arms to hold me up. What am I?","What ancient invention allows people to see through walls?"," I am laced twice in eternity and always within sight. What could I be?","What is able to go up a chimney when down but unable to go down a chimney when up?"] #List containing all the hard level questions

print("\nMoving on to the last but not the least Hard Level ☆ﾟ")

print("✏ As mentioned above there are 8 questions.")
time.sleep(2.5)
print("✏ Type your answer only when 'Enter your answer:' appears.")
time.sleep(2.5)
print("✏ You'll get 4 life line but once you redeem all of them you won't be able to have second chances but you can answer them once only ... Take lifelines carefully")
time.sleep(2.9)
time.sleep(0.9)

for i in range(len(hardLst)):
  x = hardLst[i]
  print("\n",x)
  time.sleep(2)
  a = input("Enter your answer:")
  x = hardLst[i]
  if x == hardLst[0]:
    if a == "PARACHUTE":
      print("Congratulations! you got it right")
      countTot2+= 20
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountHrd += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: It can save your life if you fall from a height")
        ans = input("Enter your answer again:")
        if ans == "PARACHUTE":
          print("Congratulations! you got it right")
          countTot2 += 20
        else:
          print("Sorry but you couldn't crack it.... It was PARACHUTE")
      else:
        print("Issoke, the correct answer to the question is PARACHUTE")
  if x == hardLst[1]:
    if a == "CHOICE":
      print("Congratulations! you got it right")
      countTot2 += 20
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountHrd += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: We can get it always but it's hard to decide")
        ans = input("Enter your answer again:")
        if ans == "CHOICE":
          print("Congratulations! you got it right")
          countTot2 += 20
        else:
          print("Sorry but you couldn't crack it.... It was CHOICE")
      else:
        print("Issoke, the correct answer to the question is CHOICE")
  if x == hardLst[2]:
    if a == "AGE":
      print("Congratulations! you got it right")
      countTot2 += 20
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountHrd += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: You've seen it earlier in the game")
        ans = input("Enter your answer again:")
        if ans == "AGE":
          print("Congratulations! you got it right")
          countTot2 += 20
        else:
          print("Sorry but you couldn't crack it.... It was AGE")
      else:
        print("Issoke, the correct answer to the question is AGE")
  if x == hardLst[3]:
    if a == "MILKYWAY":
      print("Congratulations! you got it right")
      countTot2 += 20
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      print("If you want to try again then type YES and if you wanna continue then type NO:")
      ch = input()
      if ch == "YES":
        lifeCountHrd += 1
        print("You lost your lifeline :'( but we got a hidden gen for you <3")
        time.sleep(0.5)
        print("HINT: Up there in the universe")
        ans = input("Enter your answer again:")
        if ans == "MILKYWAY":
          print("Congratulations! you got it right")
          countTot2 += 20
        else:
          print("Sorry but you couldn't crack it.... It was MILKYWAY")
      else:
        print("Issoke, the correct answer to the question is MILKYWAY")
  if x == hardLst[4]:
    if a == "YARDSTICK":
      print("Congratulations! you got it right")
      countTot2 += 20
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountHrd == lifeHrd:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was YARDSTICK")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountHrd += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: Easily found in gardens and storage rooms")
          ans = input("Enter your answer again:")
          if ans == "YARDSTICK":
            print("Congratulations! you got it right")
            countTot2 += 20
          else:
            print("Sorry but you couldn't crack it.... It was YARDSTICK")
        else:
          print("Issoke, the correct answer to the question is YARDSTICK")
  if x == hardLst[5]:
    if a == "WINDOWS" or "WINDOW":
      print("Congratulations! you got it right")
      countTot2 += 20
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountHrd == lifeHrd:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was WINDOW/WINDOWS")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountHrd += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: Connects us to the outer worls")
          ans = input("Enter your answer again:")
          if ans == "WINDOWS" or "WINDOW":
            print("Congratulations! you got it right")
            countTot2 += 20
          else:
            print("Sorry but you couldn't crack it.... It was WINDOW/WINDOWS")
        else:
          print("Issoke, the correct answer to the question is WINDOW/WINDOWS")
  if x == hardLst[6]:
    if a == "T":
      print("Congratulations! you got it right")
      countTot2 += 20
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountHrd == lifeHrd:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was T")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountHrd += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: It's a letter")
          ans = input("Enter your answer again:")
          if ans == "T":
            print("Congratulations! you got it right")
            countTot2 += 20
          else:
            print("Sorry but you couldn't crack it.... It was T")
        else:
          print("Issoke, the correct answer to the question is T")
  if x == hardLst[7]:
    if a == "UMBRELLA":
      print("Congratulations! you got it right")
      countTot2 += 20
    else:
      print("You got it wrong or maybe you typed in small letters.")
      time.sleep(0.5)
      if lifeCountHrd == lifeHrd:
        print("You have lost all your life lines :'(")
        time.sleep(0.5)
        print("The answer was UMBRELLA")  
      else:
        print("If you want to try again then type YES and if you wanna continue then type NO:")
        ch = input()
        if ch == "YES":
          lifeCountHrd += 1
          print("You lost your lifeline :'( but we got a hidden gen for you <3")
          time.sleep(0.5)
          print("HINT: It can protect us from rain")
          ans = input("Enter your answer again:")
          if ans == "UMBRELLA":
            print("Congratulations! you got it right")
            countTot2 += 20
          else:
            print("Sorry but you couldn't crack it.... It was UMBRELLA")
        else:
          print("Issoke, the correct answer to the question is UMBREALLA")
          time.sleep(1)
          print("Your total score till now is: ",countTot2)
          time.sleep(2)
    print("Your total score in this round is:",countTot2)
    time.sleep(0.8)


#RESULT TIME

print("\n",name,"! Let's check your result <3")
time.sleep(1.5)
count=countTot+countTot1+countTot2
print("\nAs you can see you have scored : ", count)
time.sleep(1)
if count >=0 and count<=100:
    print("\nI'm sorry , You gotta work on it buddy")
    time.sleep(0.8)
if count >=101 and count<=150:
    print("\nGotta improve on your thinking a little bit")
    time.sleep(0.8)
if count >=151 and count<=250:
    print("\nIssoke. Just try a little harder")
    time.sleep(0.8)
if count >=251 and count<=325:
    print("\nCheer up buddy. You're doing great")
    time.sleep(0.8)
if count >=326 and count<=375:
    print("\nWow! Your peformance just amazed me")
    time.sleep(0.8)
if count >=376 and count<=400:
    print("\nHmmm.....exciting. Looks like you got awesome skills")
    time.sleep(0.8)
    



#END CODE
def end():
  print("Thank You for playing(๑˃̵ᴗ˂̵)و ♡ ")
  time.sleep(1)
  print("Hope you enjoyed!")
  print()
  print("   ૮₍｡ᵔꈊᵔ｡₎ა")
  time.sleep(1)
  print()
  print()
  print("•─────⋅☾ ☽⋅─────•")
  time.sleep(0.8)
  print("Bibliography:https://www.brightful.me/blog/clever-riddles/")
  time.sleep(0.5)
  print("https://www.rd.com/article/short-riddles/")
  time.sleep(0.5)
  print("https://www.letsroam.com/explorer/really-hard-riddles/")
  time.sleep(0.5)
  print("https://thoughtcatalog.com/january-nelson/2020/08/hard-riddles/")
  time.sleep(1.5)
  print()
  print("© 2022-23 by Pragyan P Dutta, Samriddha Nath and Modhuriima Talukdar")
  print()
  time.sleep(3)
  print("        ∘₊✧──────✧₊∘")
  time.sleep(0.5)
  print("Credits:-")
  time.sleep(0.5)
  print("Roll no.-27 Pragyan Paramita Dutta")
  time.sleep(0.5)
  print("Roll no.-45 Samriddha Nath")
  time.sleep(0.5)
  print("Roll no.-60 Modhuriima Talukdar")
  time.sleep(0.5)
  print("        ∘₊✧──────✧₊∘")
  time.sleep(2)
  print()
  print()
  print("  •───────•°•❀•°•───────•")
  time.sleep(0.5)     
  print("              **   THANK YOU  ** ")
  time.sleep(0.5)
  print(" •───────•°•❀•°•───────•")
end()
