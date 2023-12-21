import time 
print("\nYou're trapped in a pyramid after exploring for treasure. Three doors appear, and you must find a way to escape.\n\n")

escaped = False
trapDoor = True
inventory = []
key = False
unlocked = False
passKey = "123"
keyAttempts = 5
lose = False

while not escaped:
  print("Inventory:", inventory)
  print('\n1. Door 1\n2. Door 2\n3. Door 3\n')
  options = input("Choose door: ")

  if options not in ("1", "2", "3"):
    print("\nInvalid response!")
    continue


#Door one option code
  elif options == "1":
    print("Entering Room 1...")
    time.sleep(1)
    
    if trapDoor: #If trap door true this code run 
      print("\nRoom 1 is empty\nSo... ")
      time.sleep(1)
      print("You left Room 1...\n")
      print("\nCurrent Location: 'Main Room'")

    elif trapDoor == False:  #If there is not trap door (false) this code will run. The value is changed by the blue button in door 3
      inventory.append("Key")
      key = True
      inventory.append("Letter") 
      print("\nRoom 1 has a hidden room\nWhich appeared because of the Blue button\nYou received a letter and a key.\nItems added to Inventory.")
      decision = input("\nDo you want to:\n\na. Exit this room\nb. Read letter and Exit\n\nChoose Option: ")
      if decision == "a":
        continue
      if decision == "b":
        print('\n\nDear Player,\nAs you navigate through this pyramid, remember that the key is as simple as 123, remember that Right is always right\nand if you want to escape you want to escape this pyramid just trust your instincts.\nSincerely, Python 3.11.7 \n\n')
        continue



#Door two option code
  elif options == "2": 
    print("Entering Room 2...")
    time.sleep(1)

#This will run if the value of key set to true by door one or if unlocked is set to true by door 3 green button
    if (key or unlocked): 
      print("\nYou Entered Room 2.\nThere is a pin locked door in front of you:")
      print("\na. Attempt opening Door\nb. Leave Room 2")
      response = input("\nChoose option: ")

      if response not in ("a", "b"):
        print("\nInvalid response!")
        continue

      elif response == "a": #Attempt opining the pin door behind door 2.
        
        inputKey = 0
        for i in range(keyAttempts):
          if keyAttempts == 1:
            print('\nWARNING\nThis is you last chance!')
            time.sleep(1)

          print("\nYou have", keyAttempts, "attempts!")
          inputKey = input("Enter PassKey: ")

          if inputKey == passKey:
            print("\nSUCCESS!\nAccess Granted!")
            time.sleep(0.8)
            doorChosen = input ("\nThere are now two doors in front of you:\n\na. Door on the right\nb. Door on the left\n\nChoose Door: ")

            if doorChosen not in ("a", "b"):
              print("\nInvalid response!")
              continue
            if doorChosen == "a":
              print("\n\nYou chose the door on the right\nCongratulation you are now free to leave with all the treasure you can carry\n\nYOU WIN\n\n")#WIN MESSAGE
              escaped = True
              break
            if doorChosen == "b":
              lose = True
              print("\n\nYou chose the door on the left!\nYou opened the door and walked towards a sun lit tunnel but you accidentally stepped on a pressure plate\nwhich triggered a trap to open up and throw u into a pit full of spikes\n\n YOU LOSE\n\n")#!LOSE MESSAGE
              break

          else:
            print('Incorrect Key!')
            keyAttempts = keyAttempts - 1
            continue
          
        if inputKey != passKey:
          print("\n\nYou entered the incorrect pin too many times\nThis triggers the security systems and the room fills with toxic gas!\n\nYOU LOSE\n\n")#!LOSE MESSAGE
          break

      if lose:
        break

      elif response == "b": #Leave the room 2
        time.sleep(1)
        print("You left Room 2...\n")
        print("\nCurrent Location: 'Main Room'")
    

    else:
      print("\nRoom 2 is locked\nSo...")
      time.sleep(1)
      print("You Couldn't Enter Room 2...\n")
      print("\nCurrent Location: 'Main Room'")



#Door option three code
  elif options == "3":
    print("Entering Room 3...")
    time.sleep(1)

    while True: #This will continue to loop until we break out it.
      #If the value of lose is set to true when break occurs this will cause the player to loose
      print("\nThere are three buttons:\n\na. Red Button\nb. Blue Button\nc. Green Button")
      btnOption = input('\nButton Option: ')

      if btnOption not in ("a", "b", "c"):
          print("\nInvalid response!")
          continue
      
      if btnOption == "a":
        print('You chose the Red Button')
        print("\n\nYou Made a bad decision!") #!LOSE 
        time.sleep(2)
        print("You will now die a slow death\nAs the room you're in fill with water!\n\nYOU LOSE\n")
        lose = True
        break

      elif btnOption == "b":
        print('You chose the Blue Button\n\nYou received Treasure\nItem added to Inventory')
        inventory.append("Treasure")
        trapDoor = False
        decision = input("\nDo you want to:\n\na. Exit this room\nb. Press another Button\n\nChoose Option: ")
        if decision == "a":
          break
        if decision == "b":
          continue

      elif btnOption == "c":
        print('You chose the Green Button')
        unlocked = True
        print("\n\nDoor 2 has been unlocked by this Button!\n")
        decision = input("\nDo you want to:\n\na. Exit this room\nb. Press another Button\n\nChoose Option: ")
        if decision == "a":
          break
        if decision == "b":
          continue
    if lose:
      break

