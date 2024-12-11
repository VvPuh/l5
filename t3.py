from random import randint

stones = randint(4,31)

def inp():
    user = 0
    while True:
        try:
            user = int(input('Select the number of stones from 1 to 3: '))
            if user<stones and 0<user<4:
                return user
            print("You can't take so many stones:)")
        except:
            print("Incorrect input, try again.")



print("In this game your task is to leave 1 stone after your turn. Initially", stones, "stones.")
turn = 0
player = 0
#turn = randint(0,2)
while stones>1:
    if turn%2 == 0:
        print("Your turn")
        player = inp()
        stones -= player
    else:
        print("Computer turn")
        if stones>3:
            stones -= randint(1, 4)
        else:
            stones = 1
    print(stones, "stones left.")
    turn+=1

if stones == 1:
    if turn%2 == 0:
        print("Computer win:(")
    else:
        print("You win ;D")
else:
    if turn%2 == 1:
        print("Computer win:(")
    else:
        print("You win ;D")