import tkinter as tk
from tkinter import *
from Lista import btn_listagem

class Application:
    janela = tk.Tk()
    fundoImg = PhotoImage(file = "Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Robert/BannerWEN.PNG")

    label1 = Label( janela, image = fundoImg)
    label1.place(x = 0,y = 0)
    janela.geometry("1225x710")
    janela.resizable(False, False)
    janela.title("Central de macros SBC")

    listagem_atual = btn_listagem(janela)

    janela.mainloop()

Application()