import random

while True:

    thecar = random.randint(1,3)
    oldinput=None
    doors = [1,2,3]
    
    print("""
    *******************
    select a door

    1, 2 or 3

    string for quit
    *******************\n-
    """)

    while True:
        try:
            pinput = int(input("select...:"))
        except:
            print("shutdown...")
            exit()

        if pinput > 3 or pinput < 1:
            print("there is no such door please try again\n")
            continue
        break

    

    while True:
        montysdoor=random.choice(doors)
        if montysdoor==thecar or montysdoor == pinput:
            continue
        else:
            print("i'm opening a door for you :" + str(montysdoor) + " now, will you change your choice? ?\n-")
            break

    while True:
        sinput = input("y/n:")
        if sinput=="y" or sinput=="n":
            break
        else:
            print("use y or n")
            continue


    if sinput=="n":
        if  thecar == pinput:
            print("congratulations you won a car by staying in your choice\n-")
        else:
            print("you didn't change your choice and you lost\n-")
    elif sinput =="y":
        for i in doors:
            if i==montysdoor or i==pinput:
                continue
            else:
                oldinput=pinput
                pinput = i 
                break

        if  thecar == pinput:
            print("congratulations you have changed your choice and won a car\n-")
        else:
            print("you changed your choice and lost\n-")

    print("""
    ------------
    car................:{}
    montys door........:{}
    players door.......:{}
    players first door.:{}
    ------------
    """.format(thecar,montysdoor,pinput,oldinput))
    