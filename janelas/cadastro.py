from tkinter import *

def cadastro():
    try:
        candidato = nome.get()
        numero = int(num.get())
        arq.write(f'{candidato}|{numero}\n')
        msg3['text'] = 'Cadastrado com sucesso'
        msg3['fg'] = 'green'
        nome.delete(0, 'end')
        num.delete(0, "end")
    except:
        msg3['fg'] = 'red'
        msg3['text'] = 'falha ao cadastrar candidato'

arq = open('candidatos.txt', 'w')

tela = Tk()
tela.geometry('220x360')
tela.resizable(False, False)
tela.title('Cadastro')

msg1 = Label(tela, text = '\nNome do candidato: ')
msg1.pack(side = TOP)

nome = Entry(tela)
nome.pack(side = TOP)

msg2 = Label(tela, text = '\nNúmero do cantidato: ')
msg2.pack(side = TOP)

num = Entry(tela)
num.pack(side = TOP)

msg3 = Label(tela)
msg3.pack(side = TOP)

cadastrar = Button (tela, text = 'Cadastrar', width = 20, bg = 'green', fg = 'white', command = cadastro)
cadastrar.pack(side = BOTTOM)

tela.mainloop()