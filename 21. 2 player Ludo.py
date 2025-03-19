import random as r
p1=0
p2=0
while (p1<20 or p2<20):
    if(p1>=20):
        print('Player 1 already finished.')
    else:
        x=r.randint(1,6)
        print("Player 1's dice says:",x)
        if(p1==0):
            if(x==6):
                p1=p1+1
                print("Player 1's position is:",p1)
            else:
                print("You can't begin yet.")
        else:
            p1=p1+x
            print("Player 1's position is:",p1)
        if(p1>=20):
            print("Congratulations! Player 1 finished the game!")
    if(p2>=20):
        print('Player 2 already finished.')
    else:
        y=r.randint(1,6)
        print("Player 2's dice says:",y)
        if(p2==0):
            if(y==6):
                p2=p2+1
                print("Player 2's position is:",p2)
            else:
                print("You can't begin yet.")
        else:
            p2=p2+y
            print("Player 2's position is:",p2)
        if(p2>=20):
            print("Congratulations! Player 2 finished the game!")