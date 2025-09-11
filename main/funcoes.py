import os
import subprocess
import psutil
import shutil


# Desativar recursos desnecessários pode tornar o sistema mais leve e rápido, 
# ao impedir o carregamento de programas e serviços que você não usa. 
def desativar_recursos():
     subprocess.run('OpitionalFeature.exe', shell=True)
     print('recurso não adicionado')


#Abre os programas instalados no pc
def desinstalar_app():
     subprocess.run('appwiz.cpl', shell = True)
     


#Verificar drives a serem atualizados
def atualizar_drives():
     print('recurso não adicionado')


#Função para limpar pastas com arquivos desnecessarios-----------------------------------

def limpar_arquivos_desnecessarios(caminho):
     if os.path.exists(caminho):
      for arquivo in os.listdir(caminho):
           caminho_arquivo = os.path.join(caminho , arquivo)
           try:
                if os.path.isfile(caminho_arquivo) or os.path.islink(caminho_arquivo):
                     os.unlink(caminho_arquivo)
                elif os.path.isdir(caminho_arquivo):
                     shutil.rmtree(caminho_arquivo)
           except Exception as e:
                print(f'Não foi possivel apagar{caminho_arquivo}: {e}')    
       
# #caminhos das pastas
pasta_temp_sistem = r"C:\Windows\Temp"
pasta_temp_usuario = tempfile.gettempdir()  # isso pega %temp%
pasta_prefetch = r"C:\Windows\Prefetch"

# # Limpar as pastas
print("Limpando pastas temporárias...")
limpar_arquivos_desnecessarios(pasta_temp_sistem)
limpar_arquivos_desnecessarios(pasta_temp_usuario)
limpar_arquivos_desnecessarios(pasta_prefetch)
print("Limpeza concluída!")
                           


# Abre a janela de Opções de Energia
def recursos_energia():
     subprocess.run('powercfg.cpl', shell = True)
     


#limpar o cache do navegador CHROME
def limpar_cache_navegador():
     chrome_cache = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache")
     limpar_arquivos_desnecessarios(chrome_cache)
     print("Cache do Chrome limpo!")
     print('recurso não adicionado')
     
     

 # Desfragmentar a unidade C: necessario só para hd:
def desfragmentar_disco():
     subprocess.run("defrag C: /O", shell=True)
     
     

# Abrir Configurações Avançadas de Desempenho (Efeitos Visuais)
def configuracoes_visuais():
     subprocess.run("SystemPropertiesPerformance.exe", shell=True)
     


def limpar_prefetch_temp():
     print('recurso não adicionado')
    
    
# Abre a pasta de inicialização do usuário
def apps_inicializacao(): 
    subprocess.run("taskmgr", shell=True)
    



#Recursos futuros-------------------------------------------------------------------------------------------------------

def monitorar_temperatura():
     subprocess.run("resmon.exe", shell=True)
     
     
#Liberar cache do DNS (pode acelerar internet às vezes)  
def limpar_cache_dns():
     subprocess.run('ipconfig /flushdns', shell = True) 
     
resultado = subprocess.run("ipconfig /flushdns", shell=True, capture_output=True, text=True)

print("Saída:")
print(resultado.stdout)
print("Erros:")
print(resultado.stderr)  
    