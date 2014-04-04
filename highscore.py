'''
Created on Apr 3, 2014

@author: Tryggvi SETJA INN DATE??'
'''
import os
from globals import *
import sqlite3
    
def getHighScore() :    
    conn = sqlite3.connect(os.path.join(main_dir, 'data/sqlitebrowser_200_b1_win/Highscores.sqlite'))
    c = conn.cursor()
    scores = []
    for row in c.execute('SELECT * FROM HIGHSCORE ORDER BY Score'):
        scores.append(row)
        
    conn.close()
    return scores

def setHighScore(player, score): 
    conn = sqlite3.connect(os.path.join(main_dir, 'data/sqlitebrowser_200_b1_win/Highscores.sqlite'))
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO HIGHSCORE (id, Player, Score) VALUES (?,?,?)''', (None, player, score))
        conn.commit() 
    except Exception, e: 
        print e
    finally:
        conn.close()
    

def main():
    print getHighScore()
    #setHighScore('TG', 3000)
    #setHighScore('TGGG', 3)
    test = getHighScore()
    print test[0][2]
    
if __name__ == '__main__':
    main()
        