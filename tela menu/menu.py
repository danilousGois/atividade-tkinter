from tkinter import *

window = Tk()
window.title("Tela principal")
window.geometry("1440x900")


main_frame = Frame(window, width=200, height=200, bg="black")
main_frame.place(x=0, y=0)

frame_title = Label(main_frame, text="Opções")
frame_title.place(x=0, y=5)

button_1 = Button(main_frame, text="Calculadora")
button_1.place(x=0, y=30)

button_2 = Button(main_frame, text="Lista de números")
button_2.place(x=0, y=60)

button_3 = Button(main_frame, text="Formulário")
button_3.place(x=0, y=90)

button_4 = Button(main_frame, text="Sair")
button_4.place(x=0, y=120)

window.mainloop()