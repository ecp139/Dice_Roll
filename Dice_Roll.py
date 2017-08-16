print "Dice Game!"
endProgram = 0
while endProgram != 1:
    from random import randint
    userInput = raw_input("Do you want to roll dice? Enter yes/no. ")
    if userInput.lower() in ['y', 'yes']:
        print(randint(1, 6))
    if userInput.lower() in ['n', 'no']:
        print("Okay then go away!")
        endProgram = 1
