"""
Pool.py
written for python 3.8.3
By Beth Williams

"""
#import openpyxl
#from openpyxl import load_workbook
#import tkinter as tk
#from tkinter import ttk
#from tkinter import messagebox
#from openpyxl.chart import BarChart, LineChart, Reference, Series
#import pandas as pd
#import matplotlib.pyplot as plt
#import xlrd
#import os
#import win32com.client as win32

import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
import sys

mass = .17
width = 10

class Ball():
    """Ball class, x, y position on pool table, ss is stripe or solid ball"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shot_made = False
        
    def getx_y(self):
        print(self.x)
        
    def in_Hole(self):
        shot_made = False
        
    


