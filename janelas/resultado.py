from tkinter import *
from os import system, name

tela = Tk()
tela.geometry('300x300')
tela.resizable(False, True)
tela.title('resultado')

candidatos = []
votos = []
numeros = []

if name == 'nt':
    exec = 'python'
else:
    exec = 'python3'

try:
    arq1 = open('dados/candidatos.txt', 'r')
    arq2 = open('dados/votos.txt', 'r')
except:
    system(f'{exec} aviso.py')
    exit()


for c in arq1:
        candidatos.append(c.split('|')[0])
        numeros.append(int(c.split('|')[1]))

for c in arq2:
        votos = c.split()

for c in range(0, len(candidatos)):
    Label (tela, text = f'{candidatos[c]} : {votos.count(str(numeros[c]))} voto(s)').pack(side = TOP)

tela.mainloop()
