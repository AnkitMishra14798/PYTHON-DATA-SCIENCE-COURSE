from random import randint

def hello():
    print("HOLA")
    print("AMIGOS")
    print("👩‍🏫👩‍🏫👩‍🏫")



def roll_dice():
    dices = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    print(" => ",dices[randint(0,5)])

# CALL

hello()
hello()
hello()

roll_dice()
roll_dice()
roll_dice()


