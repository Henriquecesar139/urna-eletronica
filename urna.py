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
        exibir_candidatos()
        voto_lb['text'] = voto
    elif voto[1] == '-':
        voto.remove(voto[1])
        voto.insert(1, num_voto)
        voto_lb['text'] = voto
        exibir_candidatos()

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
    global voto
    audio(2)
    if voto == candidato1:
        arquivo.writelines('1\n')
    elif voto == candidato2:
        arquivo.writelines('2\n')
    elif voto == candidato3:
        arquivo.writelines('3\n')
    else:
        pass
    voto = ['-', '-']
    voto_lb['text'] = voto
    

#Função que exibe o nome dos candidatos
def exibir_candidatos():
    candidato_lb['text'] = ''
    if voto == candidato1:
        candidato_lb['text'] = 'candidato1'
    elif voto == candidato2:
        candidato_lb['text'] = 'candidato2'
    elif voto == candidato3:
        candidato_lb['text'] = 'candidato3'

#Função de áudio  
def audio(audio):
    if audio == 1:
        mixer.music.load('arq/som.mp3')
        mixer.music.play()
    elif audio == 2:
        mixer.music.load('arq/som2.mp3')
        mixer.music.play()

mixer.init()

#Abre o arquivo de texto, caso ele não exista, o código irá criar um

try:
    arquivo = open('votos.txt', 'a')
except:
    arquivo = open('votos.txt', 'a')

#Tela
tela = Tk()
tela.geometry('220x360')
tela.resizable(False, False)
tela.title('Urna')
tela.iconbitmap('arq/urna.ico')

voto = ['-', '-']

#Número dos candidatos
candidato1 = ['4', '5']
candidato2 = ['2', '3']
candidato3 = ['1', '5']

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

confir = Button (tela, text = 'confirmar', bg = 'green', fg = 'white', width = 8, command = confirmar)
confir.place(x = 30, y = 300)

delete = Button (tela, text = 'del', fg = 'white', bg = 'red', width = 4, command = remover)
delete.place(x = 150, y = 300)

voto_lb = Label (text = voto, font="impact 30 bold")
voto_lb.place(x = 90, y = 50)

candidato_lb = Label (tela, text = '')
candidato_lb.pack(side = TOP, anchor = W)


tela.mainloop()
