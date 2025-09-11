import os
import subprocess
import psutil
import shutil

#Por que desativar recursos?
# Melhorar o desempenho: 
# Desativar recursos desnecessários pode tornar o sistema mais leve e rápido, 
# ao impedir o carregamento de programas e serviços que você não usa. 
def desativar_recursos():
     subprocess.run('OpitionalFeature.exe', shell=True)
     print('recurso não adicionado')



def desinstalar_app():
     subprocess.run('appwiz.cpl', shell = True)
     



def atualizar_drives():
     print('recurso não adicionado')



def excluir_arquivos():
     print('recurso não adicionado')



def recursos_energia():
     print('recurso não adicionado')



def limpar_cache():
     print('recurso não adicionado')


def desfragmentar_disco():
     subprocess.run('cleanmgr', shell = True)
     


def configuracoes_visuais():
     print('recurso não adicionado')


def limpar_prefetch_temp():
     print('recurso não adicionado')
    

def apps_inicializacao(): 
     print('recurso não adicionado')   



#Recursos futuros------------------------------------

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
    