from tkinter import *

def delete():
    voto = open('votos.txt', 'w')

tela = Tk()
tela.geometry('480x320')
tela.title('MENU')
tela.iconbitmap('arq/urna.ico')
tela.resizable(False, False)

voto1 = 0
voto2 = 0
voto3 = 0

try:
    votos = open('votos.txt', 'r')  
    for voto in votos:
        if int(voto) == 1:
            voto1 = voto1 + 1
        elif int(voto) == 2:
            voto2 = voto2 + 1
        elif int(voto) == 3:
            voto3 = voto3 + 1
        else:
            pass

except:
    votos = open('votos.txt', 'w')


msg = Label (tela, font = "impact 30", text = f' \ncandidato1: {voto1} \ncandidato2: {voto2} \ncandidato3: {voto3}')
msg.pack(side = TOP)

reset = Button (tela, text = 'Deletar votos computados', command = delete, width = 60, height = 4, bg = 'red', fg = 'white')
reset.pack(side = BOTTOM)


tela.mainloop()