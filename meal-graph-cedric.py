#!/usr/bin/python3

from tkinter import *

ecran_principal = Tk()
can = Canvas(ecran_principal, width = 1000, height = 500, bg = 'dark grey')
can.pack(side = BOTTOM)
bou1 = Button(ecran_principal,text='Add user', bg = 'blue', fg = 'white', width =25, command= ecran_principal.quit)
bou1.pack(side = LEFT)
bou2 = Button(ecran_principal,text='Modify user', bg = 'blue', fg = 'white', width =25, command= ecran_principal.quit)
bou2.pack(side = LEFT)
bou3 = Button(ecran_principal,text='Add menu', bg = 'blue', fg = 'white', width =25, command= ecran_principal.quit)
bou3.pack(side = RIGHT)
bou4 = Button(ecran_principal,text='Modify menu', bg = 'blue', fg = 'white', width =25, command= ecran_principal.quit)
bou4.pack(side = RIGHT)





ecran_principal.mainloop()
