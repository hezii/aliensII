#Identifying variables
l = int(0)
w = int(0)
aliensL = False
aliensT = False

#Explaining to the user what to do and first question
print("The space aliens have invaded Earth!")
print("Every week, each space alien gives birth to a new space alien.")
print("   ")
print("You are the chosen one who must tell us...")
print("    ")

while aliensL == False:
    try:
        print("How many space aliens has landed on Earth?")
        l = int(input("Please give me an answer greater than 0.   "))
        print("  ")

        if l > 0:
            aliensL = True
            print("You have said that",l,"space alien(s) has landed on Earth.")
            print("Thanks for your choice.")
            print("   ")
            aliensT = False

        else:
            print("Hey you typed in a negative number!")

    except ValueError:
            print("Hey you typed something that wasn't a number.")
            print("Please try again.")
            print("  ")


while aliensT == False:
    try:
        print("Now you must tell me how long has the space alien(s)")
        print("been on Earth for...?")
        print("   ")
    
        w = int(input("Please give me an answer greater than 0, no decimals.    "))              

        if w > 0:
            print("   ")
            print("You have said that the alien(s) have been on Earth")
            print("for",w,"week(s).")
            print("Thanks for your choice.")
            print("   ")
            aliensT = True
            aliensP = False
            
        else:
            print("Hey you typed in a negative number!")
            
    except ValueError:
        print("Hey you typed something that wasn't a number.")
        print("Please try again.")
        print("  ")
            
while aliensP == False:
    print("The following is the population per week...")
    
    for i in range (w):
        print("On week", i + 1,"there are", l * 2 ** (i + 1),".")
