from tkinter import *
from os import system, name, stat
from pygame import mixer

#funções
def votar(num):
    num_voto = num['text']
    if voto[0] == '-':
        voto.remove(voto[0])
        voto.insert(0, num_voto)
        voto_lb['text'] = voto
    elif voto[1] == '-':
        voto.remove(voto[1])
        voto.insert(1, num_voto)
        voto_lb['text'] = voto
    exibir_candidato()
    

def exibir_candidato():
    try:
        if int(''.join(voto)) in numeros:
            candidato_lb['text'] = candidatos[numeros.index(int(''.join(voto)))]
    except:
        pass

def remover():
    candidato_lb['text'] = ''
    if voto[1] != '-':
        voto.remove(voto[1])
        voto.insert(1, '-')
        voto_lb['text'] = voto
    elif voto[0] != '-':
        voto.remove(voto[0])
        voto.insert(0, '-')
        voto_lb['text'] = voto

def confirmar():
    global voto
    audio()
    try:
        if int(''.join(voto)) in numeros:
            arq2.write(f'{"".join(voto)} ')
    except:
        pass
    voto = ['-', '-']
    voto_lb['text'] = voto
    candidato_lb['text'] = ''

def audio():
    mixer.music.load('som.mp3')
    mixer.music.play()
    
if name == 'nt':
    exec = 'python'
else:
    exec = 'python3'

#Tela
tela = Tk()
tela.geometry('220x360')
tela.resizable(False, False)
tela.title('Urna')

mixer.init()

voto = ['-', '-']

#abre o arquivo com os candidatos e os números
try:
    arq = open('dados/candidatos.txt', 'r')
    arq2 = open('dados/votos.txt', 'w')
except:
    system(f'{exec} janelas/aviso.py')
    exit()

if stat('dados/candidatos.txt').st_size == 0:
    system(f'{exec} janelas/aviso.py')
    exit()

candidatos = []
numeros = []

for cand in arq:
    candidatos.append(cand.split('|')[0])
    numeros.append(int(cand.split('|')[1]))


#Botões, Labels e posicionamentos

n1 = Button (tela, width = 4,height = 2, text = '1', command = lambda : votar(n1))
n1.place(x = 30, y = 150)

n2 = Button (tela, width = 4, height = 2, text = '2', command = lambda : votar(n2))
n2.place(x = 90, y = 150)

n3 = Button (tela, width = 4, height = 2, text = '3', command = lambda : votar(n3))
n3.place(x = 150, y = 150)

n4 = Button (tela, width = 4, height = 2, text = '4', command = lambda : votar(n4))
n4.place(x = 30, y = 200)

n5 = Button (tela, width = 4, height = 2, text = '5', command = lambda : votar(n5))
n5.place(x = 90, y = 200)

n6 = Button (tela, width = 4, height = 2, text = '6', command = lambda : votar(n6))
n6.place(x = 150, y = 200)

n7 = Button (tela, width = 4, height = 2, text = '7', command = lambda : votar(n7))
n7.place(x = 30, y = 250)

n8 = Button (tela, width = 4, height = 2, text = '8', command = lambda : votar(n8))
n8.place(x = 90, y = 250)

n9 = Button (tela, width = 4, height = 2, text = '9', command = lambda : votar(n9))
n9.place(x = 150, y = 250)

confir = Button (tela, text = 'confirma', bg = 'green', fg = 'white', width = 4, height = 2, command = confirmar)
confir.place(x = 30, y = 300)

n0 = Button (tela, width = 4, height = 2, text = '0', command = lambda : votar(n0))
n0.place(x = 90, y = 300)

delete = Button (tela, text = 'del', fg = 'white', bg = 'red', width = 4, height = 2, command = remover)
delete.place(x = 150, y = 300)

voto_lb = Label (text = voto, font="arial 30 bold")
voto_lb.place(x = 90, y = 50)

candidato_lb = Label (tela, text = '')
candidato_lb.pack(side = TOP)


tela.mainloop()