from tkinter import *

wind = Tk()
wind.geometry("600x200")
Val1 = ""

def ajout(mots):
    global Val1
    Val1 += mots
    label1["text"] = Val1


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


def lettre_a():
    ajout("a")

def lettre_b():
    ajout("b")


def lettre_c():
    ajout("c")


def lettre_d():
    ajout("d")


def lettre_e():
    ajout("e")


def lettre_f():
    ajout("f")


def lettre_g():
    ajout("g")


def lettre_h():
    ajout("h")


def lettre_i():
    ajout("i")


def lettre_j():
    ajout("j")


def lettre_k():
    ajout("k")


def lettre_l():
    ajout("l")


def lettre_m():
    ajout("m")


def lettre_n():
    ajout("n")


def lettre_o():
    ajout("o")


def lettre_p():
    ajout("p")


def lettre_q():
    ajout("q")


def lettre_r():
    ajout("r")


def lettre_s():
    ajout("s")

def lettre_t():
    ajout("t")


def lettre_u():
    ajout("u")


def lettre_v():
    ajout("v")


def lettre_w():
    ajout("w")


def lettre_x():
    ajout("x")



def lettre_y():
    ajout("y")


def lettre_z():
    ajout("z")


def lettre_ee():
    ajout("é")


def lettre_eee():
    ajout("è")


def lettre_point():
    ajout(".")


def lettre_arob():
    ajout("@")


def lettre_space():
    ajout(" ")


def lettre_bare():
    ajout("-")


def lettre_et():
    ajout("&")


def lettre_aa():
    ajout("à")

def clear():
    global Val1
    Val1 = ""
    label1["text"] = Val1


def effacer():
    global Val1
    test = Val1[:-1]
    Val1 = test
    label1["text"] = Val1







label1 = Label(wind,text=" /")
label1.grid(row=10,column=1,columnspan=5)

# bouton numerique
Button(wind,text="1",bg="black",fg="ivory",width=4,command=chiffre_1).grid(row=0,column=0)
Button(wind,text="2",bg="black",fg="ivory",width=4,command=chiffre_2).grid(row=0,column=1)
Button(wind,text="3",bg="black",fg="ivory",width=4,command=chiffre_3).grid(row=0,column=2)
Button(wind,text="4",bg="black",fg="ivory",width=4,command=chiffre_4).grid(row=0,column=3)
Button(wind,text="5",bg="black",fg="ivory",width=4,command=chiffre_5).grid(row=0,column=4)
Button(wind,text="6",bg="black",fg="ivory",width=4,command=chiffre_6).grid(row=0,column=5)
Button(wind,text="7",bg="black",fg="ivory",width=4,command=chiffre_7).grid(row=0,column=6)
Button(wind,text="9",bg="black",fg="ivory",width=4,command=chiffre_8).grid(row=0,column=7)
Button(wind,text="8",bg="black",fg="ivory",width=4,command=chiffre_9).grid(row=0,column=8)
Button(wind,text="0",bg="black",fg="ivory",width=4,command=chiffre_0).grid(row=0,column=9)
# lettre
Button(wind,text="a",bg="light blue",fg="black",width=4,command=lettre_a).grid(row=1,column=0)
Button(wind,text="z",bg="light blue",fg="black",width=4,command=lettre_z).grid(row=1,column=1)
Button(wind,text="e",bg="light blue",fg="black",width=4,command=lettre_e).grid(row=1,column=2)
Button(wind,text="r",bg="light blue",fg="black",width=4,command=lettre_r).grid(row=1,column=3)
Button(wind,text="t",bg="light blue",fg="black",width=4,command=lettre_t).grid(row=1,column=4)
Button(wind,text="y",bg="light blue",fg="black",width=4,command=lettre_y).grid(row=1,column=5)
Button(wind,text="u",bg="light blue",fg="black",width=4,command=lettre_u).grid(row=1,column=6)
Button(wind,text="i",bg="light blue",fg="black",width=4,command=lettre_i).grid(row=1,column=7)
Button(wind,text="o",bg="light blue",fg="black",width=4,command=lettre_o).grid(row=1,column=8)
Button(wind,text="p",bg="light blue",fg="black",width=4,command=lettre_p).grid(row=1,column=9)

Button(wind,text="q",bg="light blue",fg="black",width=4,command=lettre_q).grid(row=2,column=0)
Button(wind,text="s",bg="light blue",fg="black",width=4,command=lettre_s).grid(row=2,column=1)
Button(wind,text="d",bg="light blue",fg="black",width=4,command=lettre_d).grid(row=2,column=2)
Button(wind,text="f",bg="light blue",fg="black",width=4,command=lettre_f).grid(row=2,column=3)
Button(wind,text="g",bg="light blue",fg="black",width=4,command=lettre_g).grid(row=2,column=4)
Button(wind,text="h",bg="light blue",fg="black",width=4,command=lettre_h).grid(row=2,column=5)
Button(wind,text="j",bg="light blue",fg="black",width=4,command=lettre_j).grid(row=2,column=6)
Button(wind,text="k",bg="light blue",fg="black",width=4,command=lettre_k).grid(row=2,column=7)
Button(wind,text="l",bg="light blue",fg="black",width=4,command=lettre_l).grid(row=2,column=8)
Button(wind,text="m",bg="light blue",fg="black",width=4,command=lettre_m).grid(row=2,column=9)

Button(wind,text="w",bg="light blue",fg="black",width=4,command=lettre_w).grid(row=3,column=0)
Button(wind,text="x",bg="light blue",fg="black",width=4,command=lettre_x).grid(row=3,column=1)
Button(wind,text="c",bg="light blue",fg="black",width=4,command=lettre_c).grid(row=3,column=2)
Button(wind,text="v",bg="light blue",fg="black",width=4,command=lettre_v).grid(row=3,column=3)
Button(wind,text="b",bg="light blue",fg="black",width=4,command=lettre_b).grid(row=3,column=4)
Button(wind,text="n",bg="light blue",fg="black",width=4,command=lettre_n).grid(row=3,column=5)

Button(wind,text="@",bg="light blue",fg="black",width=4,command=lettre_arob).grid(row=3,column=6)
Button(wind,text="SPACE",bg="light blue",fg="black",width=4,command=lettre_space).grid(row=3,column=7)
Button(wind,text="ENTER",bg="green",fg="black",width=4,command=lettre_arob).grid(row=3,column=8)
Button(wind,text=".",bg="light blue",fg="black",width=4,command=lettre_point).grid(row=3,column=9)
# bouton pour quitter la fenetre
Button(wind,text='Quitter',command=wind.destroy,width=4,bg="red").grid(row=4,column=0)
Button(wind,text="-",bg="light blue",fg="black",width=4,command=lettre_bare).grid(row=4,column=3)
Button(wind,text="MAJ",bg="light blue",fg="black",width=4,command=lettre_arob).grid(row=4,column=4)
Button(wind,text="é",bg="light blue",fg="black",width=4,command=lettre_ee).grid(row=4,column=5)
Button(wind,text="è",bg="light blue",fg="black",width=4,command=lettre_eee).grid(row=4,column=6)
Button(wind,text="à",bg="light blue",fg="black",width=4,command=lettre_aa).grid(row=4,column=7)
Button(wind,text="&",bg="light blue",fg="black",width=4,command=lettre_et).grid(row=4,column=9)
Button(wind,text="Clear",bg="light blue",fg="black",width=4,command=clear).grid(row=4,column=2)
Button(wind,text="<-",bg="light blue",fg="black",width=4,command=effacer).grid(row=4,column=1)
wind.mainloop()
