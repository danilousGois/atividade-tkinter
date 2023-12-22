link = "C:\Users\LNV\OneDrive\Área de Trabalho\atividade final tkinter\atividade-tkinter\calculadora tkinter\calculadora.py"

import subprocess

def executar_script_python(nome_do_script):
    try:
        subprocess.run(["python", nome_do_script], check=True)
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o script Python: {nome_do_script}")

# Exemplo de uso
nome_script = "caminho/do/seu/script.py"
executar_script_python(link)