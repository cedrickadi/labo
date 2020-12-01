#! /usr/bin/env python
# -*- coding:Utf8 -*-

from tkinter import *


def Pop_up()







fen = Tk()
fen.title("caisse enregistreuse")

can1 = Canvas(fen, bg="dark grey", height=300, width=678)
can1.grid(row =2, column =0, columnspan =1)
valM1 = Label(fen, text="Purchase number : 7\n Date : 31-10-2020 15:49:09 \n Employee : Olivia JONES \n Menu: Sandwich 3.75   € \nMenu: Salad 5.00  € \n Menu: Chicken 10.00  €\n Menu: teak  15.00  €\n \nTOTAL : 33.75 €")
valM1.grid(row =2, column =0)
# bouton bleu
fra1 = Frame(fen)
fra1.grid(row =1, column =0, sticky =W, padx =55, pady =10)
Button(fra1,text='Add user', width=15, bg='blue', fg='white', command=fen.quit).pack(side=LEFT)
Button(fra1,text='Modify user', width=15, bg='blue', fg='white', command=fen.quit).pack(side=LEFT)
Button(fra1,text='Add menu', width=15, bg='blue', fg='white', command=fen.quit).pack(side=LEFT)
Button(fra1,text='Modify menu', width=15, bg='blue', fg='white', command=fen.quit).pack(side=LEFT)
# pavé numerique
fra2 = Frame(fen)
fra2.grid(row =2, column =1, padx =10, pady=10)#sticky=E)
Button(fra2,text='CANCEL', width=20,height=3, bg='red', fg='white', command=fen.quit).grid(row=4, column=1)
Button(fra2,text='ENTER', width=20,height=3, bg='light yellow', fg='blue', command=fen.quit).grid(row=4, column=3)

Button(fra2,text='0', width=20,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=3, column=1)
Button(fra2,text='.', width=30,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=3, column=2,columnspan =2)

Button(fra2,text='1', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=2, column=1)
Button(fra2,text='2', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=2, column=2)
Button(fra2,text='3', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=2, column=3)

Button(fra2,text='4', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=1, column=1)
Button(fra2,text='5', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=1, column=2)
Button(fra2,text='6', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=1, column=3)

Button(fra2,text='7', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=0, column=1)
Button(fra2,text='8', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=0, column=2)
Button(fra2,text='9', width=10,height=2, bg='light yellow', fg='blue', command=fen.quit).grid(row=0, column=3)

# Zone d'affichage





fen.mainloop()
