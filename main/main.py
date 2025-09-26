from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import time
from funcoes import *
from tktooltip import ToolTip
import subprocess

#============================================= Funções================================================================

# Função para modificar a cor dos botões quando o mouse passa por cima
def add_hover_effect1(widget, 
    color_hover='#3a3a3a',
    color_normal='#3e3e4e'):
      def on_enter(e):
          widget['background']= color_hover
      def on_leave(e): 
          widget['background']= color_normal
      widget.bind("<Enter>", on_enter)
      widget.bind("<Leave>", on_leave)   
      
# Hover dos botoes de restauracao---------------------           
def add_hover_effect2(widget, 
    color_hover="#26486e",
    color_normal="#4a90e2"):
      def on_enter(e):
          widget['background']= color_hover
      def on_leave(e): 
          widget['background']= color_normal
      widget.bind("<Enter>", on_enter)
      widget.bind("<Leave>", on_leave)  
      
def add_hover_effect3(widget, 
    color_hover="#803f1f",
    color_normal="#e27d4a"):     
      def on_enter(e):
          widget['background']= color_hover
      def on_leave(e): 
          widget['background']= color_normal
      widget.bind("<Enter>", on_enter)
      widget.bind("<Leave>", on_leave)                  
      
      
# Função para criar um ponto de restauração-------------------------------------------------------------------

def criar_ponto_restauracao():
    global ultimo_ponto
    try:
        # cria ponto de restauração no Windows
        subprocess.run([
            "powershell",
            "-Command",
            "Checkpoint-Computer -Description 'Ponto_Otimizador_Aoxy' -RestorePointType 'MODIFY_SETTINGS'"
        ], check=True)
        atualizar_status("💾 Ponto de restauração criado com sucesso!", cor="lightgreen")
        ultimo_ponto = "Ponto_Otimizador_Aoxy"
    except Exception as e:
        atualizar_status(f"❌ Erro ao criar ponto de restauração: {e}", cor="red")
        
# Restaura ponto --------------------------------------------------------------------------------------------
        
def restaurar_ponto():
    if not ultimo_ponto:
        atualizar_status("⚠️ Nenhum ponto de restauração criado ainda!", cor="red")
        return

    # alerta o usuário que o PC será reiniciado
    if messagebox.askyesno("Restaurar Sistema", 
                           "Deseja realmente restaurar o sistema ao último ponto?\nO PC será reiniciado."):
        try:
            subprocess.run([
                "powershell",
                "-Command",
                f"Restore-Computer -RestorePoint '{ultimo_ponto}'"
            ], check=True)
            atualizar_status("♻️ Restaurando para o ponto de restauração...", cor="yellow")
        except Exception as e:
            atualizar_status(f"❌ Erro ao restaurar ponto: {e}", cor="red")

#Função para atualizar status ----------------------------------------------------------------------------------

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

def limpar_arquivos_desnecessarios(): # ABRIR COMO ADMIN # STATUS NA TELA DO APP
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

#criando os botoes do menu e tooltips

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

# Mensagem para cada botão

Tooltips = [
    "Desativar recursos desnecessários pode tornar o sistema mais leve e rápido,\n\n ao impedir o carregamento de programas e serviços que você não usa.",
    "🗑️ Remove programas desnecessários instalados no PC.\n\n➜ Ajuda a liberar espaço e deixar o sistema mais limpo.",
    "🔄 Atualiza os drivers do computador.\n\n➜ Mantém os dispositivos funcionando corretamente e melhora a performance.",
    "🧹 Exclui arquivos temporários e inúteis.\n\n➜ Libera espaço em disco e pode deixar o PC mais rápido.",
    "⚡ Ajusta as configurações de energia.\n\n➜ Pode economizar bateria (notebooks) ou melhorar desempenho.",
    "🌐 Limpa o cache do navegador.\n\n➜ Libera espaço, melhora a velocidade da internet e resolve erros em sites.",
    "💽 Desfragmenta o disco rígido.\n\n➜ Organiza os arquivos no HD para aumentar a velocidade de leitura.",
    "🎨 Ajusta efeitos visuais do Windows.\n\n➜ Reduz o consumo de recursos e deixa o sistema mais leve.",
    "🧹 Remove arquivos do Prefetch e da pasta TEMP.\n\n➜ Elimina restos de programas antigos e acelera o sistema.",
    "🔄 Gerencia aplicativos que iniciam junto com o Windows.\n\n➜ Diminui o tempo de inicialização e economiza memória.",
    "🌡️ Monitora a temperatura do processador e do PC.\n\n➜ Ajuda a evitar superaquecimento e problemas de hardware.",
    "Fecha o programa" 
]
# Lista para armazenar cada botão
lista_botoes = []

# criando os botões e aplicando tooltip
for i, item in enumerate(botoes):
    if len(item) == 3:
        texto, command, cor = item
        bg_color = cor
    else:
        texto, command = item
        bg_color = '#3e3e4e'
    
    btn = tk.Button(
        frame_menu, text=texto, command=lambda c=command: c(), anchor='center', width=25,
        font=('Caviar Dreams', 10, 'bold'), bg=bg_color, fg='white',
        activebackground='#57576e', activeforeground='white',
        relief='flat', pady=10
    )
    btn.pack(fill='x', pady=2, padx=2)
    add_hover_effect1(widget=btn)
    
# adiciona tooltip correspondente
    ToolTip(btn, msg=Tooltips[i])
    
    # guarda botão na lista (se precisar depois)
    lista_botoes.append(btn)    
    
#======================Frame principal==========================================
frame_main = Frame(janela, bg='#1e1e2e')
frame_main.place(x=250, y=0, width=500, height=600)


notebook = ttk.Notebook(frame_main)
notebook.pack(fill="both", expand=True, padx=10, pady=10)    
    
#======================= aba de status =========================================

aba_status = tk.Frame(notebook, bg='#1b1b2f')
notebook.add(aba_status, text='status')

label_status = tk.Label(aba_status, text="📌 Histórico de Ações", font=("Heavitas", 14, "normal"),
                        bg="#1b1b2f", fg="lightblue", anchor="w")
label_status.pack(fill="x", padx=10, pady=(10,0))

historico_status = tk.Listbox(aba_status, bg="#2c2c44", fg="white",
                              font=("Caviar Dreams", 12, 'bold'), height=15, selectbackground="#57577e")
historico_status.pack(fill="both", expand=True, padx=10, pady=10)


# ================================ Aba Configurações =============================================
aba_config = tk.Frame(notebook, bg="#1b1b2f")
notebook.add(aba_config, text="Configurações")

tk.Label(aba_config, text="Configurações", font=("Heavitas", 14, "normal"),
         bg="#1b1b2f", fg="lightblue").pack(pady=20)

tk.Checkbutton(aba_config, text="Iniciar com Windows", bg="#1b1b2f", fg="white",
               font=("Caviar Dreams", 12, 'bold'), selectcolor="#2c2c44").pack(anchor="w", padx=20, pady=5)
tk.Checkbutton(aba_config, text="Notificações Ativas", bg="#1b1b2f", fg="white",
               font=("Caviar Dreams", 12 , 'bold'), selectcolor="#2c2c44").pack(anchor="w", padx=20, pady=5)


#====================================Aba ponto de restauração =================================
aba_restauracao = tk.Frame(notebook, bg="#1b1b2f")
notebook.add(aba_restauracao, text="Ponto de Restauração")

tk.Label(aba_restauracao, text="Ponto de Restauração do Sistema", font=("Heavitas", 14, "normal"),
         bg="#1b1b2f", fg="lightblue").pack(pady=20)
tk.Label(aba_restauracao, text="Crie um ponto de restauração\npara reverter alterações indesejadas.",
         font=("Caviar Dreams", 12, "bold"), bg="#1b1b2f", fg="white").pack(pady=10)

# Botoes de Restauração------
btn_criar_ponto = tk.Button(aba_restauracao, text='💾 Criar ponto de restauração', 
        command=criar_ponto_restauracao, font=('Caviar Dreams', 10, 'bold'),
        bg="#4a90e2", fg="white",
        activebackground="#357ab7", activeforeground="white",
        relief="raised", padx=20, pady=10 , width = 30
 ) 
btn_criar_ponto.pack(padx=5)
add_hover_effect2(btn_criar_ponto)

# Botão restaurar ponto de restauração
btn_restaurar_ponto = tk.Button(
    aba_restauracao, text="♻️ Voltar ao ponto de restauração",
    command=restaurar_ponto,
    font=('Caviar Dreams', 10, 'bold'),
    bg="#e27d4a", fg="white",
    activebackground="#b75c34", activeforeground="white",
    relief="raised", padx=20, pady=10 , width=30
)
btn_restaurar_ponto.pack(padx=5)
add_hover_effect3(btn_restaurar_ponto)

# ====================================Aba Sobre =============================================
aba_sobre = tk.Frame(notebook, bg="#1b1b2f")
notebook.add(aba_sobre, text="Sobre")

tk.Label(aba_sobre, text="Otimizador Aoxy v1.0", font=("Heavitas", 16, "normal"),
         bg="#1b1b2f", fg="lightblue").pack(pady=20)
tk.Label(aba_sobre, text="Desenvolvido com Python e Tkinter puro.\nTodos os recursos são simulados para demonstração.",
         font=("Caviar Dreams", 12, "bold"), bg="#1b1b2f", fg="white").pack(pady=10)


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