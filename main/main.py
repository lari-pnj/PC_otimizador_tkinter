from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import time
from funcoes import *



#====================== Funções simulando as otimizações===========================================

def add_hover_effect(widget, 
    color_hover='#3a3a3a',
    color_normal='#3e3e4e'):
      def on_enter(e):
          widget['background']= color_hover
      def on_leave(e): 
          widget['background']= color_normal
      widget.bind("<Enter>", on_enter)
      widget.bind("<Leave>", on_leave)   


def atualizar_status(texto, cor='white'):
    historico_status.insert(END, texto)
    historico_status.itemconfig(tk.END, fg=cor)
    historico_status.yview(END)
    
def executar_acao(texto, cor='white', tempo=2000):
    atualizar_status(texto, cor) 
    barra_progresso.start(10)
    janela.after(tempo, lambda: finalizar_acao("✅ Concluído!"))
      
def desativar_recursos():
   executar_acao('⚡desativando recursos...', cor='lightgreen', tempo=2000)
   desativar_recursos_func()

def desinstalar_app():
   executar_acao('🗑️desinstalando app...', cor='yellow', tempo=2000)
   desinstalar_app_func()

def atualizar_drives(): 
   executar_acao('🔄atualizando drives...', cor='lightblue', tempo=2000)
   atualizar_drives_func()

def limpar_arquivos_desnecessarios(): # ABRIR COMO ADMIN
   executar_acao('🗑️excluindo arquivos...', cor='lightgray', tempo=2000)
   limpar_arquivos_desnecessarios_func()

def recursos_energia(): 
   executar_acao('⚡ajustando recursos de energia...', cor='red', tempo=2000)
   recursos_energia_func()

def limpar_cache_navegador(): # STATUS NA TELA DO APP
   executar_acao('🧹limpando cache...', cor='lightgreen', tempo=2000)
   limpar_cache_navegador_func()

def desfragmentar_disco(): # ABRIR COMO ADMIN
   executar_acao('💽desfragmentando disco...', cor='lightgray', tempo=2000)
   desfragmentar_disco_func()

def configuracoes_visuais():
   executar_acao('🎨configurando visual...', cor='orange', tempo=2000)
   configuracoes_visuais_func()

def limpar_prefetch_temp(): # STATUS NA TELA
   executar_acao('🧹limpando prefetch/temp...', cor='blue', tempo=2000)
   limpar_prefetch_temp_func()

def apps_inicializacao():
   executar_acao('🔄ajustando apps de inicializacao...', cor='purple', tempo=2000)
   apps_inicializacao_func()
   
def monitorar_temperatura():
    executar_acao('🔍monitorando temperatura...', cor='lightblue', tempo=2000) 
    monitorar_temperatura_func()  


def finalizar_acao(texto):
    barra_progresso.stop()
    atualizar_status(texto, cor='lightgray')    

def Sair():
    if messagebox.askyesno('sair','Deseja realmente sair?'):
        janela.destroy()

#====================== Janela principal===========================================

janela = Tk()
janela.title('otimizador Aoxy v1.0')
janela.geometry('800x600')
janela.config(background="#1e1e2e")
janela.resizable(False, False)
janela.iconbitmap('main\\icon.ico')

# ======================Frame lateral==========================================

frame_menu = Frame(janela, bg='#2e2e3e', width=250)
frame_menu.pack(side='left', fill='y')

#criando os botoes do menu
#botoes exibidos
botoes = [
    ('⚡desativar recursos', desativar_recursos),
    ('🗑️desinstalar app', desinstalar_app),
    ('🔄atualizar drives', atualizar_drives),
    ('limpar arquivos desnecessarios', limpar_arquivos_desnecessarios),
    ('⚡recursos energia', recursos_energia),
    ('🧹limpar cache navegador', limpar_cache_navegador),
    ('💽desfragmentar disco', desfragmentar_disco),
    ('🎨configuracoes visuais', configuracoes_visuais),
    ('🧹limpar prefetch/temp', limpar_prefetch_temp),
    ('🔄apps de inicializacao', apps_inicializacao),
    ('🔍monitorar temperatura', monitorar_temperatura),
    ('❌Sair', Sair, '#a33')
]

for item in botoes:
    if len(item) == 3:
        texto, command, cor = item
        bg_color = cor
    else:
        texto, command = item
        bg_color = '#3e3e4e'
    tk.Button(
        frame_menu, text=texto, command=lambda c=command: c(), anchor='center', width=25,
        font=('Arial', 10, 'bold'), bg=bg_color, fg='white',
        activebackground='#57576e', activeforeground='white',
        relief='flat', pady=10
    ).pack(fill='x', pady=2, padx=2)
    add_hover_effect(widget=frame_menu.winfo_children()[-1])
    
#======================Frame principal==========================================
frame_main = Frame(janela, bg='#1e1e2e')
frame_main.place(x=250, y=0, width=500, height=600)


notebook = ttk.Notebook(frame_main)
notebook.pack(fill="both", expand=True, padx=10, pady=10)    
    
#======================= aba de status =========================================

aba_status = tk.Frame(notebook, bg='#1b1b2f')
notebook.add(aba_status, text='status')

label_status = tk.Label(aba_status, text="📌 Histórico de Ações", font=("Arial", 14, "bold"),
                        bg="#1b1b2f", fg="white", anchor="w")
label_status.pack(fill="x", padx=10, pady=(10,0))

historico_status = tk.Listbox(aba_status, bg="#2c2c44", fg="white",
                              font=("Arial", 12), height=15, selectbackground="#57577e")
historico_status.pack(fill="both", expand=True, padx=10, pady=10)


# ================================ Aba Configurações =============================================
aba_config = tk.Frame(notebook, bg="#1b1b2f")
notebook.add(aba_config, text="Configurações")

tk.Label(aba_config, text="Configurações", font=("Arial", 14, "bold"),
         bg="#1b1b2f", fg="white").pack(pady=20)

tk.Checkbutton(aba_config, text="Iniciar com Windows", bg="#1b1b2f", fg="white",
               font=("Arial", 12), selectcolor="#2c2c44").pack(anchor="w", padx=20, pady=5)
tk.Checkbutton(aba_config, text="Notificações Ativas", bg="#1b1b2f", fg="white",
               font=("Arial", 12), selectcolor="#2c2c44").pack(anchor="w", padx=20, pady=5)


# ====================================Aba Sobre =============================================
aba_sobre = tk.Frame(notebook, bg="#1b1b2f")
notebook.add(aba_sobre, text="Sobre")

tk.Label(aba_sobre, text="Otimizador Aoxy v1.0", font=("Arial", 16, "bold"),
         bg="#1b1b2f", fg="lightblue").pack(pady=20)
tk.Label(aba_sobre, text="Desenvolvido com Python e Tkinter puro.\nTodos os recursos são simulados para demonstração.",
         font=("Arial", 12), bg="#1b1b2f", fg="white").pack(pady=10) 
    

# Barra de progresso

barra_progresso = ttk.Progressbar(frame_main, orient="horizontal", length=350, mode="indeterminate")
barra_progresso.pack(pady=10)

# Rodapé
label_footer = tk.Label(
    janela, text="© 2025 Otimizador Aoxy",
    font=("Arial", 10), bg="#1e1e2e", fg="gray"
)
label_footer.pack(side="bottom", fill="x")

# Inicializa com mensagem de boas-vindas
atualizar_status("🎉 Bem-vindo ao Otimizador Aoxy!", cor ='lightgreen')


mainloop()