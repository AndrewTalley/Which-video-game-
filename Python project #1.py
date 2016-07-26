def clinic():
    print ("Which game do you prefer more?")
    print ("Do you prefer Overwatch or Counterstrike?")
    answer = input("Type Overwatch or Counterstrke and hit 'Enter'.").lower()
    if answer == ("Overwatch") or answer == ("overwatch"):
        print ("I really enjoy this game too, but the competitive system sucks.")
        input("Press Enter to close")
    elif answer == ("Counterstrike") or answer == ("counterstrike"):
        print ("Of course! This game has a huge movement behind it right now!")
        input("Press Enter to close")
    else:
        print ("You didn't pick Overwatch or Counterstrike! Try again.")
        input("Press Enter to close")
        clinic()

clinic()