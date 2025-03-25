import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage
from datetime import datetime

frame_em_edicao = None
verificao = False

# Função de adicionar tarefa

def adicionar_tarefa():
    global frame_em_edicao
    dataDaHora1 = dataDaHora()
    tarefa = entrada_tarefa.get().strip()

    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            
            adicionar_item_tarefa(tarefa, dataDaHora1)
            entrada_tarefa.delete(0, tk.END)
    
    else: 
        messagebox.showwarning('Entrada vazia', 'Por favor, insira sua tarefa')

def adicionar_item_tarefa(tarefa, dataAtual):

    global verificao
    
    frame_tarefa = tk.Frame(canvas_interior, bg='white', bd=1, relief=tk.SOLID)

    label_tarefa = tk.Label(frame_tarefa, text=tarefa, font=('Garamond', 14), bg="white", width=30, height=2, anchor='w')
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    label_tarefaHorario = tk.Label(frame_tarefa, text=dataAtual, font=('Garamond', 14), bg=("white"), width=30, height=2, anchor='w')
    label_tarefaHorario.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botao_editar = tk.Button(frame_tarefa, image=icone_editar, command=lambda f=frame_tarefa, l=label_tarefa:preparar_edicao(f, l), bg='white', relief=tk.FLAT )
    botao_editar.pack(side=tk.RIGHT, padx=5)

    botao_deletar = tk.Button(frame_tarefa, image=icone_deletar, command=lambda f=frame_tarefa: deletar_tarefa(f), bg='white', relief=tk.FLAT)
    botao_deletar.pack(side=tk.RIGHT, padx=5)

    botao_verificao = tk.Button(frame_tarefa, image=icone_ok, command=lambda label=label_tarefa: alternar_sublinhado(label), bg='white', relief=tk.FLAT)
    botao_verificao.pack(side=tk.RIGHT, padx=5)
    
    frame_tarefa.pack(fill=tk.X, padx=5, pady=5)

    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_em_edicao
    frame_em_edicao = frame_tarefa
    entrada_tarefa.delete(0, tk.END)
    entrada_tarefa.insert(0, label_tarefa.cget("text"))
    
def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao
    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=nova_tarefa)

def alternar_sublinhado(label):
    fonte_atual = label.cget('font')
    color_atual = label.cget('fg')
    global verificao
    if 'overstrike' in fonte_atual:
        nova_fonte = fonte_atual.replace(' overstrike', '')
        nova_cor = 'black'
        verificao = False
    else:
        nova_fonte = fonte_atual + ' overstrike'
        nova_cor = 'green'
        verificao = True
    label.config(font=nova_fonte, fg=nova_cor)
    print(verificao)


def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

def confirmation():

    def fechar_janela():
        print('Entrou')
        janelaOpcoes.destroy()  # Fecha a janela

    def adicionar_e_fechar():
        adicionar_tarefa()  # Chama a função de adicionar tarefa
        fechar_janela()

    janelaOpcoes = tk.Tk()
    janelaOpcoes.title("Tarefas")
    janelaOpcoes.configure(bg="#F0F0F0")
    janelaOpcoes.geometry("520x600")

    botao_teste = tk.Button(janelaOpcoes,command=adicionar_e_fechar, text='Adicionar', width=15)
    botao_teste.pack(padx=20, pady=20)




def dataDaHora():
    agora = datetime.now()
    
    # Formata os dados
    dia = agora.day
    mes = agora.month
    ano = agora.year
    hora = agora.hour
    minuto = agora.minute

    print(f"Data: {dia}/{mes}/{ano} - Hora: {hora}:{minuto:02d}")

    return f"Data: {dia}/{mes}/{ano} - Hora: {hora}:{minuto:02d}"
# Criando a janela da aplicação

janela = tk.Tk()
janela.title("Tarefas")
janela.configure(bg="#F0F0F0")
janela.geometry("850x600")
font_cabecalho = font.Font(family="Garamond", size=30, weight="bold")
icone_editar = PhotoImage(file="icon_editar.png").subsample(14,14)
icone_deletar = PhotoImage(file="icon_remover.png").subsample(7,7)
icone_ok = PhotoImage(file="icon_ok.png").subsample(14,14)
icone_nao_ok = PhotoImage(file="icon_nao_ok.png").subsample(14,14)



rotulo_cabecalho = tk.Label(janela, text="Minhas tarefinhas", font=font_cabecalho, bg="#F0F0F0", fg="#333").pack(pady=20)

frame = tk.Frame(janela, bg='#F0F0F0')
frame.pack(pady=10)


entrada_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg='white', fg='grey', width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

entrada_tarefa.bind("<Return>", lambda event: confirmation())

botao_adicionar = tk.Button(frame, command=confirmation, text='Adicionar Tarefa', bg='#4CAF50', fg='White', height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

# Criar um frame para a lsita de tarefas com rolagem

frame_lista_tarefas = tk.Frame(janela, bg="white")
frame_lista_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_lista_tarefas, bg='white')
canvas.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_lista_tarefas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas_interior = tk.Frame(canvas, bg='white')
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

janela.mainloop()