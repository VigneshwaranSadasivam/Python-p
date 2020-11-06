import random
print("                                 WHO SHOULD BECOME 60 BY ADDING NUMBER ONE BY ONE BETWWEN\n                                       1 TO 5 THEY WILL BE A WINNER                         ")
def before_c():
    print("before adding : ",c)
def printc():
    print("by adding computer value is : ",c)
def printb():
    print("the value is : ",b)
open_question=["head","tail"]
cc=[1,2,3,4,5]
c=0
print("============choose head or tail for toss==========================")
print("head or tail")
toss=input("Enter your choice :")
x=random.choice(open_question)
print("the result is : ",x)
if(toss==x):
    print("Congratulations! you won the toss \n you will go first")
    print("lets start the game : \n you will go first :")
    while(True):
        a = int(input("\n\nenter a number between 1 to 5 :"))
        if(a==1):
            print("\nthe computer choice is : ",6-a)
            b=a+6-a
            before_c()
            c=c+b
            #printb()
            printc()
            if(c==60):
               print("=====================SORRY============================\n'you LOST the game' better luck next time")
               break
        elif(a==2):
            print("\nthe computer choice is : ",6-a)
            b=a+6-a
            before_c()
            c = c + b
            #printb()
            printc()
            if (c == 60):
                print("=====================SORRY============================\n'you LOST the game' better luck next time")
                break
        elif(a==3):
            q=print("\nthe computer choice is : ",6-a)
            b=a+6-a
            before_c()
            c = c + b
            #printb()
            printc()
            if (c == 60):
                print("=====================SORRY============================\n'you LOST the game' better luck next time")
                break
        elif(a==4):
            q=print("\nthe computer choice is : ",6-a)
            b=a+6-a
            before_c()
            c = c + b
            #printb()
            printc()
            if (c == 60):
                print("======================SORRY============================\n'you LOST the game' better luck next time")
                break

        elif(a==5):
            q=print("\nthe computer choice is : ",6-a)
            b=a+6-a
            before_c()
            c = c + b
            #printb()
            printc()
            if (c == 60):
                print("=====================SORRY============================\n'you LOST the game' better luck next time")
                break

        #elif(a==6):
            #print("the computer choice is : ",7-a)
            #b=7-a
            #c = c + b
            #printb()
            #printc()
        else:
            print("\n\nplease enter the valid number")

else:
    print("===============sorry you lost the toss=========================")
    print("\n ***************************8computer will go first : *********************************88")
    cs=6
    print("computer choice is : ", cs)
    while True:
        a = int(input("\nenter a number between 1 to 5 :"))
        if(a==1):
            print("the computer choice is : ", 6 - a)
            b = a + 6 - a
            print("before adding : ",cs)
            cs=cs+b
            # printb()
            print("\n\nafter adding : ",cs)
            if(cs==60):
                print(
                    "=====================SORRY============================\n'you LOST the game' better luck next time")
                break
        elif(a==2):
            print("the computer choice is : ", 6 - a)
            b=a+6-a
            print("before adding : ",cs)
            cs=cs+b
            # printb()
            print("\n\nafter adding : ",cs)
            if(c==60):
                print(
                    "=====================SORRY============================\n'you LOST the game' better luck next time")
                break
        elif(a==3):
            q=print("the computer choice is : ", 6 - a)
            b=a+6-a
            print("before adding : ",cs)
            cs=cs+b
            # printb()
            print("\n\nafter adding : ",cs)
            if (cs==60):
                print(
                    "=====================SORRY============================\n'you LOST the game' better luck next time")
                break
        elif(a==4):
            q = print("the computer choice is : ", 6 - a)
            b=a+6-a
            print("before adding : ",cs)
            cs=cs+b
            # printb()
            print("\n\nafter adding : ",cs)
            if(cs==60):
                print(
                    "======================SORRY============================\n'you LOST the game' better luck next time")
                break

        elif(a==5):
            q = print("the computer choice is : ", 6 - a)
            b=a+6-a
            print("before adding : ",cs)
            cs=cs+b
            # printb()
            print("\n\nafter adding : ",cs)
            if(cs==60):
                print(
                    "=====================SORRY============================\n'you LOST the game' better luck next time")
                break
        else:
            print("\n\nplease enter the valid number")











