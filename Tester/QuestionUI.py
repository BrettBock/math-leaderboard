
from Tkinter import *
import Tkinter as Tk

import random


# This class sets up the interface for asking the question
class QuestionUI:

    def __init__(self, root):
        self.window = Frame(root)
        self.q = Tk.StringVar()
        self.q.set('q')
        self.answer = Tk.StringVar()
        self.answer.set('a')
        self.question = Label(textvariable=self.q, relief=RIDGE, width=40).grid(row=1, column=1, columnspan=5)
        self.a = []
        self.l = []
        for i in range(4):
            var = StringVar()
            self.a.append(var)
            self.l.append(Label(textvariable=var, relief=RIDGE))

        self.l[0].grid(row=2, column=1, columnspan=5)#W
        self.l[1].grid(row=4, column=1)#A
        self.l[2].grid(row=4, column=5)#D
        self.l[3].grid(row=6, column=1, columnspan=5)#S

        self.b_W = Button(text='W', width=5).grid(row=3, column=3)
        self.b_A = Button(text='A', width=5).grid(row=4, column=2)
        self.b_D = Button(text='D', width=5).grid(row=4, column=4)
        self.b_S = Button(text='S', width=5).grid(row=5, column=3)

        self.window.bind("w", self.Key_W)
        self.window.bind("a", self.Key_A)
        self.window.bind("d", self.Key_D)
        self.window.bind("s", self.Key_S)

    def Key_W(self, event):
            self.TestAnswer(self.a[0])

    def Key_A(self, event):
            self.TestAnswer(self.a[1])

    def Key_D(self, event):
            self.TestAnswer(self.a[2])

    def Key_S(self, event):
            self.TestAnswer(self.a[3])

    def TestAnswer(self, test):
        if test.get() == self.answer:
            print("Correct!")
        else:
            print("Try again!")
        self.window.destroy()

    def AskQuestion(self, tq):
        self.q.set(tq.question)
        self.answer = tq.answer
        random.shuffle(tq.possibles)
        for i in range(4):
            self.a[i].set(tq.possibles[i])
