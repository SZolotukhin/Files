correct=False
while correct == False:
    album=input("What is the best selling album of all time?")
    if (album != "Thriller"):
        print("Sorry, this is incorrect. Try again")
    else:
        print("That is correct!")
        correct=True