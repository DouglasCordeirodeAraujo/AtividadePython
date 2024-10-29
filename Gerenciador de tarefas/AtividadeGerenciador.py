import tkinter as tk
from tkinter import messagebox


def botao_Adicionar():
    messagebox.showinfo("Gerenciador",message="Tarefa Adicionada!")
    
def botao_Concluir():
    messagebox.showinfo("Gerenciador",message="Tarefa Concluida!")
    
def botao_Remover():
    messagebox.showinfo("Gerenciador",message="Tarefa Removida!")

janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("500x500")  


rotulo_texto = tk.Label(janela, text="Gerenciar Tarefas:",font="Arial")
rotulo_texto.pack(pady=20)



listaTarefa = tk.Listbox(janela, height = 20, width = 60)
listaTarefa.pack(padx=20)

botao_Adicionar = tk.Button(janela, text="Adicionar Tarefas", command=botao_Adicionar).place(x=60,y=425)

botao_Concluir = tk.Button(janela, text="Concluir Tarefas", command=botao_Concluir).place(x=190,y=425)

botao_Remover = tk.Button(janela, text="Remover Tarefas", command=botao_Remover).place(x=320,y=425)

janela.mainloop()