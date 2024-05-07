import random
userscore=0
compscore=0
while True:
    ans=input("Want to play Rock Paper Scissors game?(yes/no):")
    if ans=="yes":
        print('''The choices are:
                1:Rock
                2:Paper
                3:Scissors''')
        user=int(input("Enter your Choice no:"))
        if user==1:
            print("Your Choice is Rock")
        elif user==2:
            print("Your Choice is Paper")
        elif user==3:
            print("Your Choice is Scissors")
        choicelist=[1,2,3]
        comp=random.choice(choicelist)
        if comp==1:
            print("The Computer's Choice is Rock")
        elif comp==2:
            print("The Computer's Choice is Paper")
        elif comp==3:
            print("The Computer's Choice is Scissors")
        if user==comp:
            print("It's a Tie")
            userscore=userscore+1
            compscore=compscore+1
        elif user==1 and comp==2:
            print("You have Lost")
            compscore=compscore+1
        elif user==1 and comp==3:
            print("You have Won")
            userscore=userscore+1
        elif user==2 and comp==1:
            print("You have Won")
            userscore=userscore+1
        elif user==2 and comp==3:
            print("You have Lost")
            compscore=compscore+1
        elif user==3 and comp==1:
            print("You have Lost")
            compscore=compscore+1
        elif user==3 and comp==2:
            print("You have Won")
            userscore=userscore+1
    else:
        print("The final Scores are:")
        print("Your Score:",userscore)
        print("Computer's Score:",compscore)
        break
