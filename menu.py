from tkinter import *
from os import system, name

if name == 'nt':
    exec = 'python'
else:
    exec = 'python3'

def votar():
    system(f'{exec} janelas/urna.py')
def cadastrar():
    system(f'{exec} janelas/cadastro.py')
def resultado():
    system(f'{exec} janelas/resultado.py')

tela = Tk()
tela.resizable(False, False)
tela.geometry('400x300')
tela.title('menu')
cadastro = Button(tela, text = 'Cadastrar candidato', width = 30, height = 3, command = cadastrar)
cadastro.pack(side = TOP)

voto = Button(tela, text = 'Votar', width = 30, height = 3, command = votar)
voto.pack(side = TOP)

result = Button(tela, text = 'Resultado', width = 30, height = 3, command = resultado)
result.pack(side = TOP)

tela.mainloop()