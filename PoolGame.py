from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random
import PoolBalls
from PoolBalls import *
import math
from math import *

""" Initialize the Pool Table"""

Force = 0
Target1 = ""
Target2 = ""
myList = [200, 315, 195, 325,205, 325, 210, 335, 200, 335, 190, 335, 205, 345, 215, 345, 195, 345, 185, 345, 210, 355, 200, 355, 190, 355, 220, 355, 180, 355, 200, 115]
Player_One = ["Yellow", "Purple", "Bright_green", "Black", "Maroon", "Light_purple", "Teal", "Light_orange"]
Player_Two = ["Red", "Orange", "Pink", "Black", "Dark_green", "Grey", "Light_pink", "Light_yellow"]
Combo = ""
Count1 = 0
Count2 = 0

Yellow = PoolBalls.Ball(myList[0], myList[1])
Red = PoolBalls.Ball(myList[2], myList[3])
Orange = PoolBalls.Ball(myList[4], myList[5])
Bright_green = PoolBalls.Ball(myList[6], myList[7])
Black = PoolBalls.Ball(myList[8], myList[9])
Purple = PoolBalls.Ball(myList[10], myList[11])
Dark_green = PoolBalls.Ball(myList[12], myList[13])
Grey = PoolBalls.Ball(myList[14], myList[15])
Maroon = PoolBalls.Ball(myList[16], myList[17])
Pink = PoolBalls.Ball(myList[18], myList[19])
Light_yellow = PoolBalls.Ball(myList[20], myList[21])
Teal = PoolBalls.Ball(myList[22], myList[23])
Light_pink = PoolBalls.Ball(myList[24], myList[25])
Light_orange = PoolBalls.Ball(myList[26], myList[27])
Light_purple = PoolBalls.Ball(myList[28], myList[29])
White = PoolBalls.Ball(myList[30], myList[31])

mydict = {"Yellow":[Yellow,0,1], "Red":[Red, 2, 3], "Orange": [Orange,4, 5], "Bright_green":[Bright_green,6,7], "Black": [Black, 8, 9], "Purple":[Purple, 10, 11], "Dark_green":[Dark_green, 12, 13], "Grey":[Grey,14, 15], "Maroon":[Maroon, 16,17], "Pink":[Pink, 18, 19], "Light_yellow":[Light_yellow, 20, 21], "Teal":[Teal, 22, 23], "Light_pink":[Light_pink, 24, 25], "Light_orange": [Light_orange, 26, 27], "Light_purple": [Light_purple,28, 29], "White":[White, 30,31]}


 
class Window(QMainWindow):


    def __init__(self):
        super(Window,  self).__init__()
        
        #self.painter = QPainter(self)
        self.title = "Lets Play Pool!"
        self.top = 100
        self.left = 100
        self.width = 1000
        self.height = 600
        self.slider = QSlider(Qt.Horizontal, self)
        self.Target1 = Target1
        self.Target2 = Target2
        self.Force = Force
        self.MyList = myList
        self.Combo = Combo
        self.Count1 = Count1
        self.Count2 = Count2
        #self.Yellow = Yellow
        #self.Yellow = Ball(myList[0], myList[1])
        #self.Yellow = PoolBalls.Ball(myList[0], myList[1])
      
        self.InitWindow()

    def InitWindow(self):
        """ Window Dimensions"""
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        
        """ Force: Slider"""
        
        F_label = QtWidgets.QLabel("Stick/Cue Force", self)
        F_label.setGeometry(400, 0, 80, 60)
        S_label = QtWidgets.QLabel("1000", self)
        S_label.setGeometry(400, 80, 30, 30)
        S2_label = QtWidgets.QLabel("3500", self)
        S2_label.setGeometry(500, 80, 30, 30)
        S3_label = QtWidgets.QLabel("6000", self)
        S3_label.setGeometry(600, 80, 30, 30)
        S4_label = QtWidgets.QLabel("8500", self)
        S4_label.setGeometry(700, 80, 30, 30)
        S5_label = QtWidgets.QLabel("11000", self)
        S5_label.setGeometry(800, 80, 30, 30)
        S6_label = QtWidgets.QLabel("15000", self)
        S6_label.setGeometry(900, 80, 30, 30)
        
        self.slider.setGeometry(400, 50, 500, 30) #, x, y, size
        self.slider.setMinimum(1000)
        self.slider.setMaximum(15000)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(200)
        self.slider.value
        
        self.slider.valueChanged.connect(self.changeValue)


        """ List Box of Balls """
        
        """Player One"""
        target_Ball_1 = QListWidget(self)
        target_Ball_1.addItem("Break")
        target_Ball_1.addItem("Yellow")
        target_Ball_1.addItem("Purple") 
        target_Ball_1.addItem("Bright_green")
        target_Ball_1.addItem("Black")
        target_Ball_1.addItem("Maroon")
        target_Ball_1.addItem("Light_purple")
        target_Ball_1.addItem("Teal")
        target_Ball_1.addItem("Light_orange")
        
        
        #target_Ball_1.setWindowTitle("Target Ball")
        target_Ball_1.currentItemChanged.connect(self.b1_changed)
        target_Ball_1.setGeometry(400, 150, 100, 160)
        #target_Ball_1.setLayoutMode(QListView.Batched)
        
        P1_label = QtWidgets.QLabel("Target Ball: Player One", self)
        P1_label.setGeometry(400, 115, 150, 30)


        """Player Two"""
        target_Ball_2 = QListWidget(self)
        target_Ball_2.addItem("Red")
        target_Ball_2.addItem("Orange") 
        target_Ball_2.addItem("Pink")
        target_Ball_2.addItem("Black")
        target_Ball_2.addItem("Dark _green")
        target_Ball_2.addItem("Grey")
        target_Ball_2.addItem("Light_pink")
        target_Ball_2.addItem("Light_yellow")
       
        target_Ball_2.currentItemChanged.connect(self.b2_changed)
        target_Ball_2.setGeometry(600, 150, 100, 160)
        P2_label = QtWidgets.QLabel("Target Ball: Player Two", self)
        P2_label.setGeometry(600, 115, 150, 30)

        """Combo Shot"""
        combo_Ball = QListWidget(self)
        combo_Ball.addItem("None")
        combo_Ball.addItem("Yellow")
        combo_Ball.addItem("Purple") 
        combo_Ball.addItem("Bright_green")
        combo_Ball.addItem("Black")
        combo_Ball.addItem("Maroon")
        combo_Ball.addItem("Light_purple")
        combo_Ball.addItem("Teal")
        combo_Ball.addItem("Light_orange")
        combo_Ball.addItem("Break") 
        combo_Ball.addItem("Red")
        combo_Ball.addItem("Orange") 
        combo_Ball.addItem("Pink")
        combo_Ball.addItem("Black")
        combo_Ball.addItem("Dark_green")
        combo_Ball.addItem("Grey")
        combo_Ball.addItem("Light_pink")
        combo_Ball.addItem("Light_yellow")
       
        
        combo_Ball.currentItemChanged.connect(self.c_changed)
        combo_Ball.setGeometry(800, 150, 100, 160)

        C_label = QtWidgets.QLabel("Combo Shot", self)
        C_label.setGeometry(800, 115, 150, 30)

        """ Play1 Button """
        pybutton1 = QPushButton('1st Player Shot', self)
        pybutton1.resize(100,32)
        pybutton1.move(400, 330)

        pybutton1.clicked.connect(self.clickMethod1)
        
        P1_made_label = QtWidgets.QLabel("Player One: Shots Made", self)
        P1_made_label.setGeometry(400, 370, 150, 30)
        
        P2_made_label = QtWidgets.QLabel("Player Two: Shots Made", self)
        P2_made_label.setGeometry(600, 370, 150, 30)
        
        """ Play2 Button """
        pybutton2 = QPushButton('2nd Player Shot', self)
        pybutton2.resize(100,32)
        pybutton2.move(600, 330)
        
        pybutton2.clicked.connect(self.clickMethod2)

        """Re-Rack Button"""
        rerackbutton = QPushButton('Re-Rack', self)
        rerackbutton.resize(100,32)
        rerackbutton.move(800, 330)

        rerackbutton.clicked.connect(self.start_over)
        
        self.show()

    """Re-Racks the Game"""
    def start_over(self):
        self.reRack()
        
    """Combo Ball Shot"""
    def c_changed(self, i):
        self.Combo = i.text()
        
    """Target Ball Event, player 1 (b1), player 2 (b2)"""
    def b1_changed(self, i):
        self.Target1 = i.text()
    
    def b2_changed(self, i):
        self.Target2 = i.text()
    
    """Take Shot Player 1"""
    def clickMethod1(self):
       if self.Target1 == "Break":
            self.random_Break()
       else:
            self.calc_distance(self.Target1, self.Combo)

    """Take Shot Player 2"""
    def clickMethod2(self):
        self.calc_distance(self.Target2, self.Combo)
        
    """Force Event"""
    def changeValue(self, Value):
        self.Force = self.slider.value()

    """Paints Balls on Tables based on positions"""

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        #painter.setBrush(QBrush(Qt.blue, Qt.DiagCrossPattern))
       
        # Table
        table = painter.drawRect(100, 15, 200,400)
        
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        player_one_box = painter.drawRect(400, 400, 100, 100)
        
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        player_two_box = painter.drawRect(600, 400, 100, 100)
        
        """Holes"""
        
        painter.setPen(QPen(Qt.black, 20, Qt.SolidLine))
        painter.drawPoint(100, 415)
        
        painter.setPen(QPen(Qt.black, 20, Qt.SolidLine))
        painter.drawPoint(300, 415)
        
        painter.setPen(QPen(Qt.black, 20, Qt.SolidLine))
        painter.drawPoint(100, 215)
        
        painter.setPen(QPen(Qt.black, 20, Qt.SolidLine))
        painter.drawPoint(300, 215)
        
        painter.setPen(QPen(Qt.black, 20, Qt.SolidLine))
        painter.drawPoint(100, 15)
        
        painter.setPen(QPen(Qt.black, 20, Qt.SolidLine))
        painter.drawPoint(300, 15)
        
        """Initial Position of Balls"""
        
        """First Row"""
        # 1.Yellow
        painter.setPen(QPen(Qt.yellow, 10, Qt.SolidLine))
        yellow = painter.drawPoint(myList[0], myList[1])
        
        """Second Row"""
        # 2. Red
        painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))
        red = painter.drawPoint(myList[2], myList[3])
        
        # 3. Orange
        painter.setPen(QPen(QtGui.QColor(247,142,22),10, Qt.SolidLine))
        orange = painter.drawPoint(myList[4], myList[5])
        
        """Third Row"""
        #4. green
        painter.setPen(QPen(Qt.green, 10, Qt.SolidLine))
        bright_green = painter.drawPoint(myList[6], myList[7])
        
        #5. black
        painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        black = painter.drawPoint(myList[8], myList[9])
        
        #6. Purple
        painter.setPen(QPen(QtGui.QColor(127,0,255),10, Qt.SolidLine))
        purple = painter.drawPoint(myList[10], myList[11])
      
        """Fourth Row"""
        
        #7. Dark Green
        painter.setPen(QPen(QtGui.QColor(0,102,0),10, Qt.SolidLine))
        dark_green = painter.drawPoint(myList[12], myList[13])
        
        #8. grey
        painter.setPen(QPen(QtGui.QColor(96,96,96),10, Qt.SolidLine))
        grey = painter.drawPoint(myList[14], myList[15])
        
        #9. Maroon
        painter.setPen(QPen(QtGui.QColor(98,2,31),10, Qt.SolidLine))
        maroon = painter.drawPoint(myList[16], myList[17])
        
        #10. Pink
        painter.setPen(QPen(QtGui.QColor(255,0,127),10, Qt.SolidLine))
        pink = painter.drawPoint(myList[18], myList[19])
        
        """Fifth Row"""
        
        #11. Light Yellow
        painter.setPen(QPen(QtGui.QColor(255,255,153),10, Qt.SolidLine))
        light_Yellow = painter.drawPoint(myList[20], myList[21])
        
        #12. Teal
        painter.setPen(QPen(QtGui.QColor(51,255,255),10, Qt.SolidLine))
        teal = painter.drawPoint(myList[22], myList[23])
        
        #13. Light Pink
        painter.setPen(QPen(QtGui.QColor(255,153,204),10, Qt.SolidLine))
        light_Pink = painter.drawPoint(myList[24], myList[25])
        
        #14. Light Orange
        painter.setPen(QPen(QtGui.QColor(255,178,102),10, Qt.SolidLine))
        light_orange = painter.drawPoint(myList[26], myList[27])
        
        #15. Light Purple
        painter.setPen(QPen(QtGui.QColor(178,102,255),10, Qt.SolidLine))
        light_Purple = painter.drawPoint(myList[28], myList[29])

        #White
        painter.setPen(QPen(Qt.white, 10, Qt.SolidLine))
        white  = painter.drawPoint(myList[30], myList[31])

        painter.end()
        
    def random_Break(self):
        for i in range(32):
            if self.Force <= 2000:
                if (i%2) == 0: #Even
                    myList[i] = myList[i] + random.randint(-5, 50)
                    self.boundsX(i)
                    i= i + 1
                else:
                    if i == 31:
                        myList[i] = 315
                    else:
                        myList[i] = myList[i] + random.randint(-15, 100)
                        self.boundsY(i)
                        i = i +1
                    i = i + 1
            elif self.Force > 2000 and Force <=4000:
                if (i%2) == 0: #Even
                    myList[i] = myList[i] + random.randint(-50, 100)
                    self.boundsX(i)
                    i= i + 1
                else: #Odd
                    if i == 31:
                        myList[i] = 315
                    else:
                        myList[i] = myList[i] + random.randint(-100, 250)
                        self.boundsY(i)
                        i = i + 1
            elif self.Force > 4000 and Force <=6000:
                if (i%2) == 0: #Even
                    myList[i] = myList[i] + random.randint(-100, 200)
                    self.boundsX(i)
                    i= i + 1
                else: #Odd
                    if i == 31:
                        myList[i] = 315
                    else:
                        myList[i] = myList[i] + random.randint(250, 400)
                        self.boundsY(i)
                        i = i + 1
            elif self.Force > 6000 and Force <=8000:
                if (i%2) == 0: #Even
                    myList[i] = myList[i] + random.randint(-100, 150)
                    self.boundsX(i)
                    i= i + 1
                else: #Odd
                    if i == 31:
                        myList[i] = 315
                    else:
                        myList[i] = myList[i] + random.randint(-250, 300)
                        self.boundsY(i)
                        i = i + 1
            elif self.Force > 8000:
                if (i%2) == 0: #Even
                    myList[i] = myList[i] + random.randint(-350, 400)
                    self.boundsX(i)
                    i= i + 1
                else: #Odd
                    if i == 31:
                        myList[i] = 315
                    else:
                        myList[i] = myList[i] + random.randint(-350, 500)
                        self.boundsY(i)
                        i = i + 1
        
        self.update_BallPosition(myList)
        self.repaint()
        #print(list(mydict.keys())[list(mydict.values()).index(0)])
        print(myList)
        #Yellow.getx_y()
        #Yellow.getx_y()

        
    def boundsX(self, int):
        if myList[int] < 100 and myList[int] >= 0:
            print(myList[int])
            myList[int] = 100 + (100 - myList[int])
        elif myList[int] < 0:
            myList[int] = 100 + abs(100 - myList[int])
        elif myList[int] > 300:
            myList[int] = 300 - (myList[int] - 300)
        
        
    def boundsY(self, int):
        
        if 15 > myList[int] >= 0:
            myList[int] = 15 + (15 - myList[int])
        elif myList[int] < 0:
            myList[int] = 15 + abs(15 - myList[int])
        elif myList[int] > 415:
            myList[int] = 415 - (myList[int] - 415)
        
        
    def reRack(self):
        rackList = [200, 315, 195, 325,205, 325, 210, 335, 200, 335, 190, 335, 205, 345, 215, 345, 195, 345, 185, 345, 210, 355, 200, 355, 190, 355, 220, 355, 180, 355, 200, 115]
        for i in range(32):
            myList[i] = rackList[i]
        self.repaint()
        
    def calc_distance(self, Target, ComboShot):
        """time stick in contact with cue ball = .001 seconds
           time ball to ball contact = 1 seconds,
           mass of ball = .17 kilograms
           39.4 = inches per meter (table dimensions are in inches"""

        delta_y = mydict[Target][2] - myList[mydict["White"][2]]
        delta_x = mydict[Target][1] - myList[mydict["White"][1]]
        shot_angle = atan(delta_y/delta_x)
        
        if delta_y == 0 and delta_x == 0:
            print(self.Force)
            Force_x = self.Force
            Force_y = Self.Force
        else:
            Force_x = self.Force*cos(shot_angle)
            Force_y = self.Force*sin(shot_angle)
        
        d_x = ((Force_x * .001)/.17) * .1*39.4
        d_y = ((Force_y * .001)/.17) * .1*39.4
        
        if mydict[Target][0].shot_made == False:
            if ComboShot=="None" or ComboShot=="":
                White.x = int(myList[mydict[Target][1]])
                White.y = int(myList[mydict[Target][2]])
            else:
                White.x = int(myList[mydict[ComboShot][1]])
                White.y = int(myList[mydict[ComboShot][2]])
                
        if mydict[Target][0].shot_made == False:   
            """North East"""
            if myList[mydict["White"][1]] < myList[mydict[Target][1]] and myList[mydict["White"][2]] > myList[mydict[Target][2]]:
                print("NorthEast")
                print(ComboShot)
                print(Target)
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]] + d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]] - d_y)
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]] + d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]] - d_y)
            elif myList[mydict["White"][1]] < myList[mydict[Target][1]] and myList[mydict["White"][2]] < myList[mydict[Target][2]]:
                print("EastSouth")
                """EastSouth"""
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]] + d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]] + d_y)
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]] + d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]] + d_y)
            elif myList[mydict["White"][1]] > myList[mydict[Target][1]] and myList[mydict["White"][2]] < myList[mydict[Target][2]]:
                print("SouthWest")
                """SouthWest"""
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]] - d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]] + d_y)
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]] - d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]] + d_y)
            elif myList[mydict["White"][1]] > myList[mydict[Target][1]] and myList[mydict["White"][2]] > myList[mydict[Target][2]]:
                print("WestNorth")
                """WestNorth"""
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]] - d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]] - d_y)
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]] - d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]] - d_y)
            elif myList[mydict["White"][1]] == myList[mydict[Target][1]] and myList[mydict["White"][2]] > myList[mydict[Target][2]]:
                """North"""
                print("North")
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]])
                    mydict[Target][0].y = int(myList[mydict[Target][2]] - d_y)
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]])
                    mydict[Target][0].y = int(myList[mydict[Target][2]] - d_y)
            elif myList[mydict["White"][1]] == myList[mydict[Target][1]] and myList[mydict["White"][2]] < myList[mydict[Target][2]]:
                """South"""
                print("South")
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]])
                    mydict[Target][0].y = int(myList[mydict[Target][2]] + d_y)
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]])
                    mydict[Target][0].y = int(myList[mydict[Target][2]] + d_y)
            elif myList[mydict["White"][1]] < myList[mydict[Target][1]] and myList[mydict["White"][2]] == myList[mydict[Target][2]]:
                """East"""
                print("East")
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]] + d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]])
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]] + d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]])
            elif myList[mydict["White"][1]] < myList[mydict[Target][1]] and myList[mydict["White"][2]] == myList[mydict[Target][2]]:
                """West"""
                print("West")
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]] - d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]])
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]] - d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]])
            elif myList[mydict["White"][1]] == myList[mydict[Target][1]] and myList[mydict["White"][2]] == myList[mydict[Target][2]]:
                if ComboShot == "None" or ComboShot=="":
                    mydict[Target][0].x = int(myList[mydict[Target][1]] + d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]])
                else:
                    mydict[ComboShot][0].x = int(myList[mydict[Target][1]])
                    mydict[ComboShot][0].y = int(myList[mydict[Target][2]])
                    myList[mydict[ComboShot][1]] = mydict[ComboShot][0].x
                    myList[mydict[ComboShot][2]] = mydict[ComboShot][0].y
                    mydict[Target][0].x = int(myList[mydict[Target][1]] + d_x)
                    mydict[Target][0].y = int(myList[mydict[Target][2]])


            myList[mydict[Target][1]] = mydict[Target][0].x
            self.boundsX(mydict[Target][1])
            myList[mydict[Target][2]] = mydict[Target][0].y
            self.boundsY(mydict[Target][2])
            myList[mydict["White"][1]] = White.x
            self.boundsX(mydict["White"][1])
            myList[mydict["White"][2]] = White.y
            self.boundsY(mydict["White"][2])
            self.check_ball_Made()
            self.repaint()
        elif mydict[Target][0].shot_made == True:
            QMessageBox.about(self, "Ball Status Update", "Please pick a ball that has not alread been made")

       
    """update Ball Position after Break"""
    def update_BallPosition(self, myList = []):
        if Yellow.shot_made == False:
            Yellow.x = myList[mydict["Yellow"][1]]
            Yellow.y = myList[mydict["Yellow"][2]]
        if Red.shot_made == False:   
            Red.x = myList[mydict["Red"][1]]
            Red.y = myList[mydict["Red"][2]]
        if Orange.shot_made == False:    
            Orange.x = myList[mydict["Orange"][1]]
            Orange.y = myList[mydict["Orange"][2]]
        if Black.shot_made == False:    
            Black.x = myList[mydict["Black"][1]]
            Black.y = myList[mydict["Black"][2]]
        if Bright_green.shot_made == False:    
            Bright_green.x = myList[mydict["Bright_green"][1]]
            Bright_green.y = myList[mydict["Bright_green"][2]]
        if Purple.shot_made == False:   
            Purple.x = myList[mydict["Purple"][1]]
            Purple.y = myList[mydict["Purple"][2]]
        if Dark_green.shot_made == False:    
            Dark_green.x = myList[mydict["Dark_green"][1]]
            Dark_green.y = myList[mydict["Dark_green"][2]]
        if Grey.shot_made == False:    
            Grey.x = myList[mydict["Grey"][1]]
            Grey.y = myList[mydict["Grey"][2]]
        if Maroon.shot_made == False:    
            Maroon.x = myList[mydict["Maroon"][1]]
            Maroon.y = myList[mydict["Maroon"][2]]
        if Pink.shot_made == False:   
            Pink.x = myList[mydict["Pink"][1]]
            Pink.y = myList[mydict["Pink"][2]]
        if Light_yellow.shot_made == False:    
            Light_yellow.x = myList[mydict["Light_yellow"][1]]
            Light_yellow.y = myList[mydict["Light_yellow"][2]]
        if Teal.shot_made == False:    
            Teal.x = myList[mydict["Teal"][1]]
            Teal.y = myList[mydict["Teal"][2]]
        if Light_pink.shot_made == False:    
            Light_pink.x = myList[mydict["Light_pink"][1]]
            Light_pink.y = myList[mydict["Light_pink"][2]]
        if Light_orange.shot_made == False:    
            Light_orange.x = myList[mydict["Light_orange"][1]]
            Light_orange.y = myList[mydict["Light_orange"][2]]
        if Light_purple.shot_made == False:    
            Light_purple.x = myList[mydict["Light_purple"][1]]
            Light_purple.y = myList[mydict["Light_purple"][2]]
        

    def check_ball_Made(self):
        for ball in mydict:
            if  100 <= myList[mydict[ball][1]] <= 110 and 405 <= myList[mydict[ball][2]] <= 415:
                if ball == "White":
                    self.update_White()
                elif ball == "Black":
                    self.update_Black()
                else:
                    mydict[ball][0].shot_made = True
                    QMessageBox.about(self, "Ball Status Update", "Congrats " + ball + " has made it into the hole")
                    self.remove_made_targets_P1(ball)
                    self.remove_made_targets_P2(ball)
            elif 289 <=myList[mydict[ball][1]] <= 300 and 405 <= myList[mydict[ball][2]] <= 415:
                if ball == "White":
                    self.update_White()
                elif ball == "Black":
                    self.update_Black()
                else:
                    mydict[ball][0].shot_made = True
                    QMessageBox.about(self, "Ball Status Update", "Congrats " + ball + " has made it into the hole")
                    self.remove_made_targets_P1(ball)
                    self.remove_made_targets_P2(ball)
            elif 100 <= myList[mydict[ball][1]] <=110 and 225 <= myList[mydict[ball][2]] <= 205:
                if ball == "White":
                    self.update_White()
                elif ball == "Black":
                    self.update_Black()
                else:
                    mydict[ball][0].shot_made = True
                    QMessageBox.about(self, "Ball Status Update", "Congrats " + ball + " has made it into the hole")
                    self.remove_made_targets_P1(ball)
                    self.remove_made_targets_P2(ball)
            elif 289 <= myList[mydict[ball][1]] <= 300 and 205 <=myList[mydict[ball][2]] <= 225:
                if ball == "White":
                    self.update_White()
                elif ball == "Black":
                    self.update_Black()
                else:
                    mydict[ball][0].shot_made = True
                    QMessageBox.about(self, "Ball Status Update", "Congrats " + ball + " has made it into the hole")
                    self.remove_made_targets_P1(ball)
                    self.remove_made_targets_P2(ball)
            elif 100 <= myList[mydict[ball][1]] <= 110 and 15 <= myList[mydict[ball][2]] <= 25:
                if ball == "White":
                    self.update_White()
                elif ball == "Black":
                    self.update_Black()
                else:
                    mydict[ball][0].shot_made = True
                    QMessageBox.about(self, "Ball Status Update", "Congrats " + ball + " has made it into the hole")
                    self.remove_made_targets_P1(ball)
                    self.remove_made_targets_P2(ball)
            elif 289 <= myList[mydict[ball][1]] <= 300 and 15 <= myList[mydict[ball][2]] <= 25:
                if ball == "White":
                    self.update_White()
                elif ball == "Black":
                    self.update_Black()
                else:
                    mydict[ball][0].shot_made = True
                    QMessageBox.about(self, "Ball Status Update", "Congrats " + ball + " has made it into the hole")
                    self.remove_made_targets_P1(ball)
                    self.remove_made_targets_P2(ball)

    def update_White(self):
        QMessageBox.about(self, "Ball Status Update", "Scratch: White ball in hole.  Next players turn")
        myList[mydict["White"][1]] = 20
        myList[mydict["White"][2]] = 115
        
    def update_Black(self):
        QMessageBox.about(self, "Ball Status Update", "Scratch: Black ball in hole.  You Lose")
       
    def remove_made_targets_P1(self, Ball):
        dx = 20
        x1 = 420
        x2 = 420
       
        if Ball in Player_One:
            if self.Count1 <=4:
                if mydict[Ball][0].shot_made == True:
                    myList[mydict[Ball][1]] = x1 + self.Count1*dx
                    myList[mydict[Ball][2]] = 420
                    self.Count1 = self.Count1 + 1
            if self.Count1 > 4 and self.Count1 <=8:
                if mydict[Ball][0].shot_made == True:
                    myList[mydict[Ball][1]] = x2 + self.Count1*dx
                    myList[mydict[Ball][2]] = 440
                    self.Count1 = self.Count1 + 1
            if self.Count1 ==9:
                QMessageBox.about(self, "Ball Status Update", "Congratulations!!! Player 1 has won the Game")
            
    def remove_made_targets_P2(self, Ball):
        dx = 20
        x1 = 620
        x2 = 620
        
        if Ball in Player_Two:
            if self.Count2 <=4:
                if mydict[Ball][0].shot_made == True:
                    myList[mydict[Ball][1]] = x1 + self.Count2*dx
                    myList[mydict[Ball][2]] = 420
                    self.Count2 = self.Count2 + 1
            if self.Count2 > 4 and self.Count2 <=8:
                if mydict[Ball][0].shot_made == True:
                    myList[mydict[Ball][1]] = x2 + self.Count2*dx
                    myList[mydict[Ball][2]] = 440
                    self.Count2 = self.Count2 + 1
            if self.Count2 == 9:
                QMessageBox.about(self, "Ball Status Update", "Congratulations!!! Player 2 has won the Game")
              
        
                      
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())





 