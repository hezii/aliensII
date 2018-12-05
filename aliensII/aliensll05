#Identifying variables
l = int(0) #The value for the landed space aliens question
w = int(0) #The value for the weeks the space aliens have been on Earth question
aliensL = False #boolean for while loop 1
aliensT = False #boolean for while loop 2

#Explaining to the user what to do and first question
print("The space aliens have invaded Earth!") 
print("Every week, each space alien gives birth to a new space alien.")
print("   ") #These are used to space out the print lines
print("You are the chosen one who must tell us...")
print("    ") #These are used to space out the print lines

while aliensL == False: #first while loop
    try: #The code will attempt to run this first
        print("How many space aliens has landed on Earth?") #first question
        l = int(input("Please give me an answer greater than 0.   ")) #waiting for answer from user
        print("  ") #These are used to space out the print lines

        if l > 0: #if the value given is greater than 0, then...
            aliensL = True #because aliensL is now true, the 1st while loop will not run anymore
            print("You have said that",l,"space alien(s) has landed on Earth.") #Telling the user what they answered
            print("Thanks for your choice.")
            print("   ") #These are used to space out the print lines
            aliensT = False #This will go to line 36 because aliensT is false, which runs the 2nd while loop

        else: #if the value given is less than 0...
            print("Hey you typed in a negative number!")

    except ValueError: #If try does not work, go here
            print("Hey you typed something that wasn't a number.") #Explaining to the user what happened
            print("Please try again.") #after line 33, the code will go back to line 15
            print("  ") #These are used to space out the print lines


while aliensT == False: #second while loop
    try: #the code will attempt to run this
        print("Now you must tell me how long has the space alien(s)") #second question
        print("been on Earth for...?") #second question
        print("   ") #These are used to space out the print lines
    
        w = int(input("Please give me an answer greater than 0, no decimals.    ")) #waiting for an answer from the user             

        if w > 0: #if the answer given from the user is greater than 0, then...
            print("   ") #These are used to space out the print lines
            print("You have said that the alien(s) have been on Earth") #comfirming with user what they said
            print("for",w,"week(s).")
            print("Thanks for your choice.") #print line thanking user
            print("   ") #These are used to space out the print lines
            aliensT = True #exits 2nd while loop and goes to line 63
                        
        else: #if the user gives us something less than 0
            print("   ") #These are used to space out the print lines
            print("Hey you typed in a negative number!") #telling user what they did
            
    except ValueError: #if try does not work, go here
        print("Hey you typed something that wasn't a number.") #the user typed a symbol or letter
        print("Please try again.") #while loop 2 will repeat after line 60
        print("  ") #These are used to space out the print lines
        
            print("The following is the population per week...")
    
for i in range (w): #The line under this one will run for (w) times
    print("On week", i + 1,"there are", l * 2 ** (i + 1),".") #math calculations
