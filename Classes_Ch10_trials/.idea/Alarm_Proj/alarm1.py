import datetime 
import os


stop = False

def main():

    while stop == False:
        rn = str(datetime.datetime.now().time())
        print(rn)
        if rn == '15:55:00.000000':
            stop = True
            os.system("start BTS_House_Of_Cards.mp3")


