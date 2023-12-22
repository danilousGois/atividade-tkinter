import tkinter as tk

projetos = ["D:\Users\20221041110029\Desktop\tkinter\calculadora tkinter\calculadora.py", "D:\Users\20221041110029\Desktop\tkinter\Tkinter-Designer\build\gui.py", "D:\Users\20221041110029\Desktop\tkinter\formulario\formulario.py"]

def abrir_tela(posicao):
    open(projetos[posicao])

abrir_tela(1)

# Criar a janela principal
janela = tk.Tk()
janela.title("Menu com 4 Botões")

# Criar os botões
botao1 = tk.Button(janela, text="calculadora")
botao2 = tk.Button(janela, text="listagem de números")
botao3 = tk.Button(janela, text="formulário")
botao4 = tk.Button(janela, text="sair")

# Posicionar os botões na janela
botao1.pack(pady=10)
botao2.pack(pady=10)
botao3.pack(pady=10)
botao4.pack(pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()