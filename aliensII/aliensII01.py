# In version 3, I fixed the math calculations, I needed to add parenthesis for the math to work.
# Also I completed the nested if structure for all the code.
# Added comments for ease of understanding
# Fixed grammatical errors and things that can made the code hard to read
# ^ (adding empty print lines)

#Identifying variables
l = int(0)
w = int(0)

#Explaining to the user what to do and first question
print("The space aliens have invaded Earth!")
print("   ")
print("Every week, each space alien gives birth to a new space alien.")
print("   ")
print("You are the chosen one who must tell us...")
print("How many space aliens has landed on Earth?")
print("   ")

l = int(input("Please give me an answer greater than 0, no decimals or negative numbers.    "))
print("  ")

#first nested if for first question
if l > 0:
    print("You have said that",l,"space alien(s) has landed on Earth.")
    print("Thanks for your choice.")
    print("   ")
    print("Now you must tell me how long has the space alien(s)")
    print("been on Earth for...")
    print("   ")

    w = int(input("Please give me an answer greater than 0, no decimals.    "))

#Second nested if for second question
    if w > 0:
        print("   ")
        print("You have said that the alien(s) have been on Earth")
        print("for",w,"week(s).")
        print("Thanks for your choice.")
        print("   ")

#The loop
        for i in range (w):
            print("On week", i + 1,"there are", l * 2 ** (i + 1),".")

#If the user input a number less than zero that is not a decimal this error pops up (negative)
    elif w < 0:
        print("Hey you typed something wrong!")
        print("You said that the space aliens that landed on Earth have")
        print("stayed here for",w,"week(s)")
        print("   ")
        print("This is a negative number.")
        print("Restart the code and try again.  :(")

#If the user types in a different invalid answer
    else:
        print("Hey you typed something wrong!")
        print("You either typed a letter, a symbol or decimal number")
        print("Restart the code and try again.  :(")

#If the user input a number less than zero that is not a decimal this error pops up (negative)
elif l < 0:
    print("Hey you typed something wrong!")
    print("You said that",l,"space alien(s) has landed on Earth.")
    print("This is a negative number.")
    print("Restart the code and try again.  :(")

#If the user types in a different invalid answer
else:
    print("Hey you typed something wrong!")
    print("You either typed a letter, a symbol or decimal number.")
    print("Restart the code and try again.  :(")
