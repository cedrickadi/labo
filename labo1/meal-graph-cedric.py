#! /usr/bin/env python
# -*- coding:Utf8 -*-

from tkinter import *
from tkinter import ttk

#from meals_management_cedric import *





def pop_up_add_user():
    fInfos=Toplevel()
    fInfos.title("add user")
    Button(fInfos, text='Quitter',bg='red', command=fInfos.destroy).grid(row=4, column=3)
    Button(fInfos, text='Valider',bg='green', command=fInfos.destroy).grid(row=4, column=2)
    Label(fInfos,text = 'first name : ').grid(row = 1, column = 1, sticky = E)
    Label(fInfos,text = 'family name : ').grid(row = 2, column = 1, sticky = E)
    Label(fInfos,text = 'email address : ').grid(row = 3, column = 1, sticky = E)
    first_name = Entry(fInfos).grid(row=1, column = 2)
    family_name = Entry(fInfos).grid(row=2, column = 2)
    email_address = Entry(fInfos).grid(row=3, column = 2)
    fInfos.transient(fen)
    fInfos.grab_set()
    fen.wait_window(fInfos)


def pop_up_modify_user():
    fInfos=Toplevel()
    fInfos.title("Modify user")
    Label(fInfos,text = 'first name : ').grid(row = 1, column = 1, sticky = E)
    Label(fInfos,text = 'family name : ').grid(row = 2, column = 1, sticky = E)
    Label(fInfos,text = 'email address : ').grid(row = 3, column = 1, sticky = E)
    new_first_name=Entry(fInfos).grid(row=1, column = 2)
    new_family_name=Entry(fInfos).grid(row=2, column = 2)
    new_email_address=Entry(fInfos).grid(row=3, column = 2)
    Button(fInfos, text='Quitter',bg='red', command=fInfos.destroy).grid(row=4, column=3)
    Button(fInfos, text='Valider',bg='green', command=fInfos.destroy).grid(row=4, column=2)
    fInfos.transient(fen)
    fInfos.grab_set()
    fen.wait_window(fInfos)


def pop_up_add_menu():
    fInfos=Toplevel()
    fInfos.title("add menu")
    Label(fInfos,text = 'menu name : ').grid(row = 1, column = 1, sticky = E)
    Label(fInfos,text = 'description : ').grid(row = 2, column = 1, sticky = E)
    Label(fInfos,text = 'price : ').grid(row = 3, column = 1, sticky = E)
    menu_name = Entry(fInfos).grid(row=1, column = 2)
    description = Entry(fInfos).grid(row=2, column = 2)
    price = Entry(fInfos).grid(row=3, column = 2)
    Button(fInfos, text='Quitter',bg='red', command=fInfos.destroy).grid(row=4, column=3)
    Button(fInfos, text='Valider',bg='green', command=fInfos.destroy).grid(row=4, column=2)
    fInfos.transient(fen)
    fInfos.grab_set()
    fen.wait_window(fInfos)


def pop_up_modify_menu():
    fInfos=Toplevel()
    fInfos.title("modify menu")
    Label(fInfos,text = 'menu id : ').grid(row = 1, column = 1, sticky = E)
    Label(fInfos,text = 'new menu price : ').grid(row = 2, column = 1, sticky = E)
    menu_id = Entry(fInfos).grid(row=1, column = 2)
    new_price = Entry(fInfos).grid(row=2, column = 2)
    Button(fInfos, text='Quitter',bg='red', command=fInfos.destroy).grid(row=4, column=3)
    Button(fInfos, text='Valider',bg='green', command=fInfos.destroy).grid(row=4, column=2)
    fInfos.transient(fen)
    fInfos.grab_set()
    fen.wait_window(fInfos)



def ajout(mots):
    global valeur
    valeur += mots
    label1["text"] = valeur


def chiffre_1():
    ajout("1")


def chiffre_2():
    ajout("2")


def chiffre_3():
    ajout("3")


def chiffre_4():
    ajout("4")


def chiffre_5():
    ajout("5")


def chiffre_6():
    ajout("6")


def chiffre_7():
    ajout("7")


def chiffre_8():
    ajout("8")


def chiffre_9():
    ajout("9")


def chiffre_0():
    ajout("0")


def lettre_point():
    ajout(".")


def effacer():
    global valeur
    cancel = valeur[:-1]
    valeur = cancel
    label1["text"] = valeur


fen = Tk()
fen.title("caisse enregistreuse")
fen.geometry("1048x600")
valeur = ""



# bouton bleu
fra1 = Frame(fen)
fra1.grid(row =1, column =0, sticky =W, padx =55, pady =10)
Button(fra1,text='Add user', width=15, bg='blue', fg='white', command=pop_up_add_user).pack(side=LEFT)
Button(fra1,text='Modify user', width=15, bg='blue', fg='white', command=pop_up_modify_user).pack(side=LEFT)
Button(fra1,text='Add menu', width=15, bg='blue', fg='white', command=pop_up_add_menu).pack(side=LEFT)
Button(fra1,text='Modify menu', width=15, bg='blue', fg='white', command=pop_up_modify_menu).pack(side=LEFT)
# pavé numerique
fra2 = Frame(fen)
fra2.grid(row =2, column =1, padx =10, pady=10,sticky=S)
Button(fra2,text='CANCEL', width=10,bg='red', fg='white', command=fen.quit).grid(row=4, column=1)
Button(fra2,text='ENTER', width=10, bg='green', fg='black', command=fen.quit).grid(row=4, column=3)
Button(fra2,text='0', width=10, bg='light yellow', fg='blue', command=chiffre_0).grid(row=3, column=1)
Button(fra2,text='.', width=10, bg='light yellow', fg='blue', command=lettre_point).grid(row=3, column=2,columnspan =2,sticky=W)
Button(fra2,text='1', width=10, bg='light yellow', fg='blue', command=chiffre_1).grid(row=2, column=1)
Button(fra2,text='2', width=10, bg='light yellow', fg='blue', command=chiffre_2).grid(row=2, column=2)
Button(fra2,text='3', width=10, bg='light yellow', fg='blue', command=chiffre_3).grid(row=2, column=3)
Button(fra2,text='4', width=10, bg='light yellow', fg='blue', command=chiffre_4).grid(row=1, column=1)
Button(fra2,text='5', width=10, bg='light yellow', fg='blue', command=chiffre_5).grid(row=1, column=2)
Button(fra2,text='6', width=10, bg='light yellow', fg='blue', command=chiffre_6).grid(row=1, column=3)
Button(fra2,text='7', width=10, bg='light yellow', fg='blue', command=chiffre_7).grid(row=0, column=1)
Button(fra2,text='8', width=10, bg='light yellow', fg='blue', command=chiffre_8).grid(row=0, column=2)
Button(fra2,text='9', width=10,bg='light yellow', fg='blue', command=chiffre_9).grid(row=0, column=3)
Button(fra2,text='<-', width=10,bg='light yellow', fg='blue', command=effacer).grid(row=3, column=3)
# Zone d'affichage
label1 = Label(fra2,text=" /")
label1.grid(row=5, column=2,columnspan=1)
can1 = Canvas(fen, bg="ivory", height=400, width=500)
can1.grid(row =2, column =0, columnspan =1)



fen.mainloop()
