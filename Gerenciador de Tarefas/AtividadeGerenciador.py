import tkinter as tk
from tkinter import messagebox

def botao_Adicionar():
    texto = entrada_tarefa.get()
    if texto:
        listaTarefa.insert(tk.END, texto)
        entrada_tarefa.delete(0, tk.END)
        messagebox.showinfo("Gerenciador",message="Tarefa Adicionada!")
    else:
        messagebox.showinfo("Atenção!",message="Digite uma Tarefa!")
    
def botao_Concluir():
    if tarefa_selecionada := listaTarefa.curselection():
        tarefa = listaTarefa.get(tarefa_selecionada)
        listaTarefa.delete(tarefa_selecionada)
        listaTarefa.insert(tarefa_selecionada,f"{tarefa} - (Concluida!)")
        messagebox.showinfo("Gerenciador",message="Tarefa Concluida!")
    else:
        messagebox.showinfo("Atenção!",message="Selecione uma Tarefa!")

def botao_Remover():
    if tarefa_selecionada := listaTarefa.curselection():
        listaTarefa.delete(tarefa_selecionada)
        messagebox.showinfo("Gerenciador",message="Tarefa Removida!")
    else:
        messagebox.showinfo("Atenção!",message="Selecione uma Tarefa!")

janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("500x500")  

rotulo_texto = tk.Label(janela, text="Adicionar Tarefas:",font=("Arial", 12))
rotulo_texto.pack(pady=20)

entrada_tarefa = tk.Entry(janela, font=("Arial", 12),width=40)
entrada_tarefa.place(x=66,y=45)

rotulo_texto = tk.Label(janela, text="Tarefas Adicionadas:",font=("Arial", 12))
rotulo_texto.pack(pady=10)

listaTarefa = tk.Listbox(janela,font=("Arial", 12), height =16, width =40)
listaTarefa.place(x=66,y=100)

botao_Adicionar = tk.Button(janela, text="Adicionar Tarefa", command=botao_Adicionar, width=15, height=2).place(x=60,y=425)

botao_Concluir = tk.Button(janela, text="Concluir Tarefa", command=botao_Concluir, width=15, height=2).place(x=190,y=425)

botao_Remover = tk.Button(janela, text="Remover Tarefa", command=botao_Remover, width=15,height=2).place(x=320,y=425)

janela.mainloop()