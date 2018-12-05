#Identifying variables
l = int(0) #The value for the landed space aliens question
w = int(0) #The value for the weeks the space aliens have been on Earth question
aliensL = False #boolean for while loop 1
aliensT = False #boolean for while loop 2
aliensP = False #boolean for while loop 3


#Explaining to the user what to do and first question
print("The space aliens have invaded Earth!")
print("Every week, each space alien gives birth to a new space alien.")
print("   ") #These are used to space out the print lines
print("You are the chosen one who must tell us...")
print("    ") #These are used to space out the print lines

while aliensL == False: #first while loop
    try:
        print("How many space aliens has landed on Earth?")
        l = int(input("Please give me an answer greater than 0.   "))
        print("  ") #These are used to space out the print lines

        if l > 0:
            aliensL = True
            print("You have said that",l,"space alien(s) has landed on Earth.")
            print("Thanks for your choice.")
            print("   ") #These are used to space out the print lines
            aliensT = False

        else:
            print("Hey you typed in a negative number!")

    except ValueError:
            print("Hey you typed something that was a decimal or wasn't a number.")
            print("Please try again.")
            print("  ")


while aliensT == False: #second while loop
    try:
        print("Now you must tell me how long has the space alien(s)")
        print("been on Earth for...?")
        print("   ") #These are used to space out the print lines
    
        w = int(input("Please give me an answer greater than 0, no decimals.    "))              

        if w > 0:
            print("   ")
            print("You have said that the alien(s) have been on Earth")
            print("for",w,"week(s).")
            print("Thanks for your choice.")
            print("   ") #These are used to space out the print lines
            
            print("The following is the population per week...")
            for i in range (w):
                print("On week", i + 1,"there are", l * 2 ** (i + 1),".")
                
            print("Thanks for using this program")
            aliensT = True
            
        else:
            print("Hey you typed in a negative number!")
            
    except ValueError:
        print("Hey you typed something that was a decimal or wasn't a number.")
        print("Please try again.")
        print("  ") #These are used to space out the print lines

            
while aliensP == False:
    if tri == "yes":
        aliensL = False
        aliensP = True

        
    elif tri == "no":
       
        
    else:
        print("Hey, you typed something wrong...")
        print("Try again")
