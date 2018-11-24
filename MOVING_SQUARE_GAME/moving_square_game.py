
import random
import time
from tkinter import *

class Score(object):
    def __init__(self):
        self._score = 0

    @property
    def getScore(self):
        return self._score

    @getScore.setter
    def getScore(self,score):
        self._score = score

    def reset(self):
        self._score = 0

    def increment(self):
        self._score +=1

    """
    Todo: Add ability to get/set score using properties
    Todo: Add ability to reset the score to zero using a reset() method
    Todo: Add ability to increment the score by one using the increment method
    """
    score = property(getScore, getScore.setter)

def onObjectClick(event):
    clicktime = int(round(time.time() * 1000))
    if (clicktime - starttime) < 2000:
        score.increment()
    label['text'] = "Score: %s" % score.getScore
    play()
    """
    #Todo: get snapshot of now again and compare the times
    #Todo: if the different is less than 2000 increment the score label by 1
    #Todo: start the next round
    #Todo: Remove this when function is implemented
    """

def play():
    x  = random.randint(50,360)
    y = random.randint(50,360)
    global starttime
    starttime = int(round(time.time())*1000)

    """
    Todo: Get two ints randomly to represent points on the canvas
    Todo: Take a snapshot of the current time
    Todo: clear the screen and draw a new square which is bound to a function
    """

    canvas.delete('all')
    square = canvas.create_rectangle(x, y, x+50,y+50, outline ="red", fill ="red")

    canvas.tag_bind(square, '<ButtonPress-1>', onObjectClick)

def quit():
    global root
    root.quit()

score = Score()

root = Tk()
root.title('Assignment 3 // Exam Number:117303363')

label = Label(root,text="Score: %s" % score.getScore)
label.grid(row=1)
labelq = Label(root, text="Assignment 3\tColin Kelleher\t117303363")
labelq.grid(row=5)


canvas = Canvas(root,width=400, height=400, bg="grey")
canvas.grid(row=2)
button = Button(root, text="Start Game", command=play)
button.grid(row=3)
button = Button(root, text="Quit Game", command=quit)
button.grid(row=4)

root.mainloop()
