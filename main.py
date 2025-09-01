from tkinter import *
from tkinter import Tk



janela = Tk()
janela.title('otimizador')
janela.geometry('650x450')

#imagem de backgroud

fundo = PhotoImage(file="backgroud1.png")  
label_fundo = Label(janela, image=fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

#titulo

titulo = Label(janela, text="Otimizador aoxy", background="#4E2372", fg="white", font=('arial', 18, "bold"))
titulo.pack(pady=20)

 
#botoes exibidos
botao1 = Button(janela, text="desativar recursos")
botao2 = Button(janela, text="desinstalar app")
botao3 = Button(janela, text="atualizar drives")
botao4 = Button(janela, text="excluir arquivos desnecessarios")
botao5 = Button(janela, text="recursos de energia")
botao6 = Button(janela, text="limpar cache")
botao7 = Button(janela, text="desfragmentar disco")
botao8 = Button(janela, text="configuracoes visuais")
botao9 = Button(janela, text="limpar prefetch/temp")
botao10 = Button(janela, text="apps de inicializacao")




# funcoes dos botoes
def acao_botao1():
   mensagem.config(text = 'recursos desativados com sucesso ✔️')
   janela.after(3000, lambda: mensagem.config(text=""))
botao1 = Button(janela, text="desativar recursos", command=acao_botao1)

def acao_botao2():
   mensagem.config(text = 'app desinstalado com sucesso ✔️')
   janela.after(3000, lambda: mensagem.config(text=""))
botao2 = Button(janela, text="desinstalar app", command=acao_botao2)

def acao_botao3():
    mensagem.config(text = 'drives atualizados com sucesso ✔️')
    janela.after(3000, lambda: mensagem.config(text=""))
botao3 = Button(janela, text="atualizar drives", command=acao_botao3)

def acao_botao4():
    mensagem.config(text = 'arquivos excluídos com sucesso ✔️')
    janela.after(3000, lambda: mensagem.config(text=""))
botao4 = Button(janela, text="excluir arquivos desnecessarios", command=acao_botao4)

def acao_botao5():
    mensagem.config(text = 'recursos de energia ajustados com sucesso ✔️')
    janela.after(3000, lambda: mensagem.config(text=""))
botao5 = Button(janela, text="recursos de energia", command=acao_botao5)

def acao_botao6():
    mensagem.config(text = 'cache limpo com sucesso ✔️')
    janela.after(3000, lambda: mensagem.config(text=""))
botao6 = Button(janela, text="limpar cache", command=acao_botao6)

def acao_botao7():
    mensagem.config(text = 'disco desfragmentado com sucesso ✔️')
    janela.after(3000, lambda: mensagem.config(text=""))
botao7 = Button(janela, text="desfragmentar disco", command=acao_botao7)

def acao_botao8():
    mensagem.config(text = 'configurações visuais aplicadas com sucesso ✔️')
    janela.after(3000, lambda: mensagem.config(text=""))
botao8 = Button(janela, text="configuracoes visuais", command=acao_botao8)

def acao_botao9():
    mensagem.config(text = 'prefetch/temp limpo com sucesso ✔️')
    janela.after(3000, lambda: mensagem.config(text=""))
botao9 = Button(janela, text="limpar prefetch/temp", command=acao_botao9)

def acao_botao10():
    mensagem.config(text = 'apps de inicializacao ajustados com sucesso ✔️')
    janela.after(3000, lambda: mensagem.config(text=""))
botao10 = Button(janela, text="apps de inicializacao", command=acao_botao10)

#label para mostrar mensagens

mensagem = Label(janela,bg="#4E2372", text="",fg="white", font = ("arial", 10,"bold"))
mensagem.pack(side="top", pady=50, padx=100)

#janela com opçoes organizadas

frame = Frame(janela, bg="#4E2372")  
frame.pack(pady=20)

Button(frame, text="Desativar recursos",command=acao_botao1,width=18, bg="#2ecc71", fg="white", font=('arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=10)
Button(frame, text="Desinstalar app",command=acao_botao2, width=18, bg="#2ecc71", fg="white", font=('arial', 12, 'bold')).grid(row=0, column=1, padx=10, pady=10)
Button(frame, text="Atualizar drives",command=acao_botao3, width=18, bg="#2ecc71", fg="white", font=('arial', 12, 'bold')).grid(row=0, column=2, padx=10, pady=10)

Button(frame, text="Excluir arquivos",command=acao_botao4, width=18, bg="#2ecc71",fg="white",font=("arial",12,"bold")).grid(row=1, column=0, padx=10, pady=10)
Button(frame, text="Limpar cache",command=acao_botao6,width=18,bg="#2ecc71",fg="white",font=("arial",12,"bold")).grid(row=1, column=1, padx=10, pady=10)
Button(frame, text="Desfragmentar disco",command=acao_botao7,width=18,bg="#2ecc71",fg="white",font=("arial",12,"bold")).grid(row=1, column=2, padx=10, pady=10)

Button(frame, text="Configurações visuais",command=acao_botao8,width=18, bg="#2ecc71", fg="white", font=("arial",12,"bold")).grid(row=2, column=0, padx=10, pady=10)
Button(frame, text="Limpar prefetch/temp",command=acao_botao9,width=18, bg="#2ecc71",fg="white",font=("arial",12,"bold")).grid(row=2, column=1, padx=10, pady=10)
Button(frame, text="Apps de inicialização",command=acao_botao10,width=18, bg="#2ecc71",fg="white",font=("arial",12,"bold")).grid(row=2, column=2, padx=10, pady=10)





mainloop()