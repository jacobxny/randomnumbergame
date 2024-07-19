import random 

x = random.randint(1, 100)

usernum2 = int(input("Choose a number between 1 and 100 and you will get prompted if its higher or lower. You get 9 tries. "))

if usernum2 == x:
    print("You guessed it correct. First try too! ")
elif usernum2 < x:
    print("Your number is lower than the computers. ")
    usernum2 = int(input("Please guess again. "))
elif usernum2 > x:
    print("Your number is higher than the computers. ")
    usernum2 = int(input("Please guess again. "))
if usernum2 == x:
    print("You guessed it correctly. ")
elif usernum2 < x:
    print("Your number is lower than the computers. ")
    usernum2 = int(input("Please guess again. "))
elif usernum2 > x:
    print("Your number is higher than the computers. ")
    usernum2 = int(input("Please guess again. "))
if usernum2 == x:
    print("You guessed it correct. ")
elif usernum2 < x:
    print("Your number is lower than the computers. ")
    usernum2 = int(input("Please guess again. "))
elif usernum2 > x:
    print("Your number is higher than the computers. ")
    usernum2 = int(input("Please guess again. "))
if usernum2 == x:
    print("You guessed it correctly. ")
elif usernum2 < x:
    print("Your number is lower than the computers. ")
    usernum2 = int(input("Please guess again. "))
elif usernum2 > x:
    print("Your number is higher than the computers. ")
    usernum2 = int(input("Please guess again. "))
if usernum2 == x:
    print("You guessed it correct. ")
elif usernum2 < x:
    print("Your number is lower than the computers. ")
    usernum2 = int(input("Please guess again. "))
elif usernum2 > x:
    print("Your number is higher than the computers. ")
    usernum2 = int(input("Please guess again. "))
if usernum2 == x:
    print("You guessed it correctly. ")
elif usernum2 < x:
    print("Your number is lower than the computers. ")
    usernum2 = int(input("Please guess again. "))
elif usernum2 > x:
    print("Your number is higher than thw computers. ")
    usernum2 = int(input("Please guess again. "))
if usernum2 == x:
    print("You guessed it correctly.")
elif usernum2 < x:
    print("Your number is lower than the computers. ")
    usernum2 = int(input("Please guess again. "))
elif usernum2 > x:
    print("Your number is higher than the computers. ")
    usernum2 = int(input("Please guess again. "))
if usernum2 == x:
    print("You guessed it correctly. ")
elif usernum2 < x:
    print("You Lost. The number was",x)    
elif usernum2 > x:
    print("You Lost. The number was",x)
