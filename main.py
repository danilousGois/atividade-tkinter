
import os

def executar_arquivos_executaveis(lista_de_arquivos):
    for arquivo in lista_de_arquivos:
        if arquivo.endswith('.exe'):  # Certifique-se de que o arquivo seja um executável (extensão .exe)
            caminho_completo = os.path.abspath(arquivo)
            
            try:
                os.system(caminho_completo)
                print(f"Executando: {caminho_completo}")
            except Exception as e:
                print(f"Erro ao executar {caminho_completo}: {e}")

# Substitua a lista abaixo pelos nomes dos seus arquivos executáveis
arquivos_executaveis = ["..\calculadora tkinter\calculadora.py", "..\Tkinter-Designer\build\gui.py", "..\formulario\formulario.py"]

executar_arquivos_executaveis(arquivos_executaveis)