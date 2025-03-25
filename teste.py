import tkinter as tk
from datetime import datetime

from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

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


dataDaHora = dataDaHora()
print(dataDaHora)