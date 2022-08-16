from tkinter import *

tela = Tk()
tela.geometry('660x50')
tela.resizable(False, False)
tela.title('aviso')

msg = Label(tela, text = 'Sem candidatos cadastrados // Sem votos computados', fg = 'red', font = 'arial 15')
msg.pack(side = TOP)

tela.mainloop()
