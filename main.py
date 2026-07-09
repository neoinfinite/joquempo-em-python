from tkinter import *
from tkinter import ttk

# importando pillow
from PIL import Image, ImageTk
import random

# cores -----------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

# configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

# dividindo a janela
Frame_cima =Frame(janela, width=260, height=100, bg=co1, relief='raised')
Frame_cima.grid(row=0, column=0, sticky=NW)
Frame_baixo =Frame(janela, width=260, height=300, bg=co0, relief='flat')
Frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando o frame cima
app_1 = Label(Frame_cima, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0) #seu nome
app_1.place(x=25, y=70)
app_1_linha = Label(Frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0) 
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(Frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0) #seu placar
app_1_pontos.place(x=50, y=20)


app_ = Label(Frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)


app_2_pontos = Label(Frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20) 
app_2 = Label(Frame_cima, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0) #nome da maquina
app_2.place(x=205, y=70)
app_2_linha = Label(Frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)


app_linha = Label(Frame_cima, text='', width=255, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95) #linha abaixo do placar



app_pc = Label(Frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_pc.place(x=190, y=10)

# funçoes globais
global voce
global Pc 
global rounds
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rounds = 5


# funçao logica do jogo
def jogar(i):
    global rounds
    global pontos_voce
    global pontos_pc

    if rounds > 0:
        print(rounds)
        opçoes = ['pedra', 'papel', 'tesoura']
        pc = random.choice(opçoes)
        voce = i

        app_pc['text'] = pc
        app_pc['fg']= co1

        # caso for igual
        if voce == 'pedra' and pc == 'pedra':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
        
        elif voce == 'papel' and pc == 'papel':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif voce == 'tesoura' and pc == 'tesoura':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        # movendo para frente
        elif voce == 'pedra' and pc == 'papel':
            print('pc ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            
            pontos_pc += 10

        elif voce == 'pedra' and pc == 'tesoura':
            print('voce ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0

            pontos_voce += 10

        elif voce == 'papel' and pc == 'tesoura':
            print('pc ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0

            pontos_pc += 10

        # movendo para tras
        elif voce == 'tesoura' and pc == 'pedra':
            print('pc ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0

            pontos_pc += 10


        elif voce == 'tesoura' and pc == 'papel':
            print('voce ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0

            pontos_voce += 10

        elif voce == 'papel' and pc == 'pedra':
            print('voce ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0

            pontos_voce += 10

        # atualizando a pontuaçao
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc

        # atualizando o numero de rounds
        rounds -=1


    else:
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc

        # chamando a funçao terminar
        fim_do_jogo()


# funçao iniciar o jogo
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon1
    global b_icon2
    global b_icon3

    b_jogar.destroy()

    # importando os botoes
    icon_1 = Image.open('pedra, papel, tesoura/imagens/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.Resampling.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon1 = Button(Frame_baixo, command=lambda:jogar('pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon1.place(x=15, y=60)


    icon_2 = Image.open('pedra, papel, tesoura/imagens/papel.png')
    icon_2 = icon_2.resize((50,50), Image.Resampling.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon2 = Button(Frame_baixo, command=lambda:jogar('papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon2.place(x=95, y=60)


    icon_3 = Image.open('pedra, papel, tesoura/imagens/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.Resampling.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon3 = Button(Frame_baixo, command=lambda:jogar('tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon3.place(x=170, y=60)


# funçao terminar o jogo
def fim_do_jogo():
    global rounds
    global pontos_voce
    global pontos_pc

    # reiniciando as variaveis para 0
    pontos_voce = 0
    pontos_pc = 0
    rounds = 5

    # destruindo os botoes de opçoes
    b_icon1.destroy()
    b_icon2.destroy()
    b_icon3.destroy()

    # definindo o vencedor
    jogador_voce = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])

    if jogador_voce > jogador_pc:
        app_vencedor = Label(Frame_baixo, text='Parabens voce ganhou!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        app_vencedor.place(x=5, y=60)

    elif jogador_voce < jogador_pc:
        app_vencedor = Label(Frame_baixo, text='Infelizmente voce perdeu!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        app_vencedor.place(x=5, y=60)
    
    else:
        app_vencedor = Label(Frame_baixo, text='foi um empate!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=5, y=60)


    # jogar de novo
    def jogar_denovo():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()

        b_jogar_denovo.destroy()

        iniciar_jogo()

    b_jogar_denovo = Button(Frame_baixo,command=jogar_denovo, width=30, text='jogar de novo', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=5, y=151)
        

#botao de começar o jogo
b_jogar = Button(Frame_baixo,command=iniciar_jogo, width=30, text='jogar', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)


janela.mainloop()