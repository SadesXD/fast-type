import time
import random
import os
import json

def play():
    tem = time.localtime()[4] * 60 + time.localtime()[5]
    tik = 2
    kata2 = json.loads(open('lol.json','rb').read())
    rand = random.choice(kata2)
    mulai = input(f'[ {rand} ] answer: ')
    score = 0
    os.system('cls')

    while tik <= 2:
        tems2 = time.localtime()[4]
        if tems2 == 0:
            tems2 = 60
        tem2 = tems2 * 60 + time.localtime()[5]
        waktu = 60 - (tem2 - tem)
        if tem2 - tem < 60:
            if mulai.lower() == rand:
                score += len(rand)
                kata = json.loads(open('lol.json','rb').read())
                ran = random.choice(kata)
                rand = ran
                mulai = input(f'{waktu} Time left\n[ {ran} ] answer: ')
                os.system('cls')
            else:
                reason = ""
                if not mulai or mulai == "":
                    reason = "Not Answer"
                else:
                    reason = f'You Lose\n\nWords: {rand}\nYou\'re answer: {mulai}\nScore: {score} words per minute'              
                os.system('cls')
                print(reason)
                quit()
        else:
            os.system('cls')
            print(f"Time has been finished\nYou're score: {score} words per minute")
            quit()
opsi = input("[ SIMPLE PYTHON FAST TYPE GAME ]\n\n[ play ] -> playing a game\n[ guide ] -> give a tutorial\n\nType your selection: ")
tutor = "Simple python fast type game guide\n\n1. type PLAY for playing a game\n2. You will receive some words\n3. If you done received you can just type the words and ENTER\n4. After 1 minute your game will ends and you will see your score"
if opsi.lower() == "play":
    os.system('cls')
    play()
elif opsi.lower() == "guide":
    os.system('cls')
    print(tutor)
else:
    print("Options can't found");
