import random


#print type(pc)
#1=rock
#2=scissor
#3=cloth
player = 9
while (player != 0):
    player = input('please input,exit with "q":')
    pc = random.randint(1, 3)
    print pc
    if (player == 3 and pc == 1):
        print "you lose!"
        continue

    if (player ==1 and pc ==3):
        print "you win!"
        continue

    if (player == pc):
        print "draw!"
        continue

    if (player > pc):
        print "you win!"
    else:
        print "you lose!"



