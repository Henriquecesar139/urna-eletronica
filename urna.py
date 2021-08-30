#Colocar o som no bptão confirmar

from tkinter import *
from pygame import mixer

#Funções

#Função que captura o número do botão pressionado
def votar(num):
    audio(1)
    num_voto = num['text']
    if voto[0] == '-':
        voto.remove(voto[0])
        voto.insert(0, num_voto)
        candidatos()
        voto_lb['text'] = voto
    elif voto[1] == '-':
        voto.remove(voto[1])
        voto.insert(1, num_voto)
        voto_lb['text'] = voto
        candidatos()

#Função que deleta um número digitado
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

#Função que Confirma o voto
def confirmar():
    audio(2)
    global voto, voto1, voto2, voto3
    if voto == candidato1:
        voto1 = voto1 + 1
    elif voto == candidato2:
        voto2 = voto2 + 1
    elif voto == candidato3:
        voto3 = voto3 + 1
    else:
        pass
    voto = ['-', '-']
    voto_lb['text'] = voto

#Função que exibe o nome dos candidatos
def candidatos():
    candidato_lb['text'] = ''
    if voto == candidato1:
        candidato_lb['text'] = 'candidato1'
    elif voto == candidato2:
        candidato_lb['text'] = 'candidato2'
    elif voto == candidato3:
        candidato_lb['text'] = 'candidato3'
    
def audio(audio):
    if audio == 1:
        mixer.init()
        mixer.music.load('som.mp3')
        mixer.music.play()
    elif audio == 2:
        mixer.init()
        mixer.music.load('som2.mp3')
        mixer.music.play()


#Tela
tela = Tk()
tela.geometry('250x360')
tela.resizable(False, False)
tela.title('Urna eletônica')
tela.iconbitmap('urna.ico')

#Label
voto = ['-', '-']
voto_lb = Label (text = voto, font="impact 30 bold")
voto_lb.place(x = 90, y = 50)

candidato_lb = Label (tela, text = '')

#Número dos candidatos
candidato1 = ['4', '5']
candidato2 = ['2', '3']
candidato3 = ['1', '5']

voto1 = 0
voto2 = 0
voto3 = 0
#Botões

n1 = Button (tela, width = 4,height = 2, text = '1', command = lambda : votar(n1))
n2 = Button (tela, width = 4, height = 2, text = '2', command = lambda : votar(n2))
n3 = Button (tela, width = 4, height = 2, text = '3', command = lambda : votar(n3))
n4 = Button (tela, width = 4, height = 2, text = '4', command = lambda : votar(n4))
n5 = Button (tela, width = 4, height = 2, text = '5', command = lambda : votar(n5))
n6 = Button (tela, width = 4, height = 2, text = '6', command = lambda : votar(n6))
n7 = Button (tela, width = 4, height = 2, text = '7', command = lambda : votar(n7))
n8 = Button (tela, width = 4, height = 2, text = '8', command = lambda : votar(n8))
n9 = Button (tela, width = 4, height = 2, text = '9', command = lambda : votar(n9))

confir = Button (tela, text = 'confirmar', bg = 'green', fg = 'white', width = 8, command = confirmar)
delete = Button (tela, text = 'del', fg = 'white', bg = 'red', width = 4, command = remover)

#Posicionamento

n1.place(x = 30, y = 150)
n2.place(x = 90, y = 150)
n3.place(x = 150, y = 150)
n4.place(x = 30, y = 200)
n5.place(x = 90, y = 200)
n6.place(x = 150, y = 200)
n7.place(x = 30, y = 250)
n8.place(x = 90, y = 250)
n9.place(x = 150, y = 250)
confir.place(x = 30, y = 300)
delete.place(x = 150, y = 300)
candidato_lb.pack(side = TOP)


tela.mainloop()
#=============#

#Tela de resultados (Essa tela irá aparecer quando a tela da urna for fechada)
resultado = Tk()
resultado.resizable(False, False)
resultado.geometry('400x150')
resultado.title('Resultado')

#Mensagem de Resultados
result = Label (resultado, text = f'''Candidato1: {voto1} voto(s)
candidato2: {voto2} voto(s)
candidato3: {voto3} voto(s)''', font = 'impact 20 bold')
result.pack(side = TOP)


resultado.mainloop()