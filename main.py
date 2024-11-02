import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage


# criando janela
janela = tk.Tk()
janela.title("Tarefas")
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

# cabeçalho
font_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
font_cabecalho = tk.Label(
    janela, text="Tarefas", font=font_cabecalho, bg="#F0F0F0", fg="#333"
).pack(pady=20)


janela.mainloop()
