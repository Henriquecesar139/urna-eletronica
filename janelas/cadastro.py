from tkinter import *

def cadastro():
    try:
        candidato = nome.get()
        numero = int(num.get())
        partido = part.get()
        arq.write(f'{candidato} ({partido}) |{numero}\n')
        aviso['text'] = 'Cadastrado com sucesso'
        aviso['fg'] = 'green'
        nome.delete(0, 'end')
        num.delete(0, "end")
        part.delete(0, "end")
    except:
        aviso['fg'] = 'red'
        aviso['text'] = 'falha ao cadastrar candidato'

arq = open('dados/candidatos.txt', 'w')

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

msg3 = Label(tela, text = '\nPartido')
msg3.pack(side = TOP)
part = Entry(tela)
part.pack(side = TOP)


aviso = Label(tela)
aviso.pack(side = TOP)

cadastrar = Button (tela, text = 'Cadastrar', width = 20, bg = 'green', fg = 'white', command = cadastro)
cadastrar.pack(side = BOTTOM)

tela.mainloop()