import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
import sqlite3
import os

regApp = ctk.CTk()
regApp.title("The Frank Spreadsheets | Registro de Agentes")
regApp.geometry("640x850")
regApp.resizable(False, False)
regApp._set_appearance_mode("dark")
regApp.attributes("-topmost", True)


# variaveis

timeOnFunc = "nenhum"

# Lista de Turnos

turnoList = ['Manhã | 06:00 - 12:20', 'Tarde | 12:20 - 18:40', 'Noite | 18:40 - 01:00', 'Madrugada | 01:00 - 07:20']

# Cabeçalho

linha1Header = ctk.CTkFrame(regApp, width=500, height=4, bg_color="#242424", fg_color="#C0C0C0", border_width=0, corner_radius=0)
linha1Header.place(x=70,y=20)

registrarAgenteLabel = ctk.CTkLabel(regApp, text_color="#BABABA",text="REGISTRAR AGENTE", bg_color="#242424", font=("INTER BOLD", 45))
registrarAgenteLabel.place(x=90,y=50)

linha2Header = ctk.CTkFrame(regApp, width=500, height=4, bg_color="#242424", fg_color="#C0C0C0", border_width=0, corner_radius=0)
linha2Header.place(x=70,y=135)

# Formulàrio

# ID do Agente:

agentIDLabel = ctk.CTkLabel(regApp, text_color="#C0C0C0",text="ID do Agente: ", bg_color="#242424", font=("INTER BOLD", 25))
agentIDLabel.place(x=40,y=157)

linhaAgent = ctk.CTkFrame(regApp, width=161, height=2, bg_color="#242424", fg_color="#767676", border_width=0, corner_radius=100)
linhaAgent.place(x=40,y=187)

agentIDEntry = ctk.CTkEntry(regApp, placeholder_text="ID", placeholder_text_color="#858585", width=161, height=30, bg_color="#242424", fg_color="#1F1F1F", corner_radius=100, border_width=1, border_color="#C0C0C0")
agentIDEntry.place(x=40,y=197)

# ID Regional

regionIDLabel = ctk.CTkLabel(regApp, text_color="#C0C0C0",text="ID Regional: ", bg_color="#242424", font=("INTER BOLD", 25))
regionIDLabel.place(x=40,y=234)

linhaRegion = ctk.CTkFrame(regApp, width=161, height=2, bg_color="#242424", fg_color="#767676", border_width=0, corner_radius=100)
linhaRegion.place(x=40,y=264)

regionIDEntry = ctk.CTkEntry(regApp, placeholder_text="Regiâo", placeholder_text_color="#858585", width=161, height=30, bg_color="#242424", fg_color="#1F1F1F", corner_radius=100, border_width=1, border_color="#C0C0C0")
regionIDEntry.place(x=40,y=274)

# Turno

turnoLabel = ctk.CTkLabel(regApp, text_color="#C0C0C0",text="Turno: ", bg_color="#242424", font=("INTER BOLD", 25))
turnoLabel.place(x=40,y=307)

linhaTurno = ctk.CTkFrame(regApp, width=161, height=2, bg_color="#242424", fg_color="#767676", border_width=0, corner_radius=100)
linhaTurno.place(x=40,y=337)

optionMenuTurno= ctk.CTkOptionMenu(regApp, values=turnoList, button_color="#1F1F1F", width=161, height=30, bg_color="#242424", fg_color="#1F1F1F", button_hover_color="#4D4D4D", corner_radius=5)
optionMenuTurno.set("Selecionar Turno: ")
optionMenuTurno.place(x=40,y=347)

# Nome Completo

nomeLabel = ctk.CTkLabel(regApp, text_color="#C0C0C0",text="Nome: ", bg_color="#242424", font=("INTER BOLD", 25))
nomeLabel.place(x=40,y=391)

linhaNome = ctk.CTkFrame(regApp, width=530, height=2, bg_color="#242424", fg_color="#767676", border_width=0, corner_radius=100)
linhaNome.place(x=40,y=421)

nomeEntry= ctk.CTkEntry(regApp, placeholder_text="Nome Completo", placeholder_text_color="#858585", width=530, height=30, bg_color="#242424", fg_color="#1F1F1F", corner_radius=100, border_width=1, border_color="#C0C0C0")
nomeEntry.place(x=40,y=431)

# Gerente

gerenteLabel = ctk.CTkLabel(regApp, text_color="#C0C0C0",text="Gerente Rensponsável: ", bg_color="#242424", font=("INTER BOLD", 25))
gerenteLabel.place(x=40,y=470)

linhaGerente = ctk.CTkFrame(regApp, width=530, height=2, bg_color="#242424", fg_color="#767676", border_width=0, corner_radius=100)
linhaGerente.place(x=40,y=500)

gerenteEntry= ctk.CTkEntry(regApp, placeholder_text="Gerente", placeholder_text_color="#858585", width=530, height=30, bg_color="#242424", fg_color="#1F1F1F", corner_radius=100, border_width=1, border_color="#C0C0C0")
gerenteEntry.place(x=40,y=510)

# Endereço

endLabel = ctk.CTkLabel(regApp, text_color="#C0C0C0",text="Endereço: ", bg_color="#242424", font=("INTER BOLD", 25))
endLabel.place(x=40,y=550)

linhaEnd = ctk.CTkFrame(regApp, width=530, height=2, bg_color="#242424", fg_color="#767676", border_width=0, corner_radius=100)
linhaEnd.place(x=40,y=580)

endEntry= ctk.CTkEntry(regApp, placeholder_text="Endereço Completo", placeholder_text_color="#858585", width=530, height=30, bg_color="#242424", fg_color="#1F1F1F", corner_radius=100, border_width=1, border_color="#C0C0C0")
endEntry.place(x=40,y=590)

# Carregar LOGO

homePageIMG = ctk.CTkImage(light_image=Image.open(r"assets\bgFrankSpreadsheetsIMG.jpg"), size=(302,167))
ctk.CTkLabel(regApp, text=None, image=homePageIMG, corner_radius=280).place(x=268, y=169)

# Bottom Frames

# Foto Display

bottomCarregarIMGLabel = ctk.CTkLabel(regApp, text_color="#8E8E8E",text="Carregar Foto do Agente: ", bg_color="#242424", font=("ARIAL BOLD", 25))
bottomCarregarIMGLabel.place(x=40,y=644)

linhaCarregarIMGLabel = ctk.CTkFrame(regApp, width=299, height=2, bg_color="#242424", fg_color="#8E8E8E", border_width=0, corner_radius=100)
linhaCarregarIMGLabel.place(x=40,y=673)

bottomDisplayIMGFrame = ctk.CTkFrame(regApp, width=150, height=120, bg_color="#242424", fg_color="#292929", corner_radius=0)
bottomDisplayIMGFrame.place(x=105,y=681)

bottomFotoCarregadaLabel = ctk.CTkLabel(regApp, text_color="#939393",text="Foto Carregada", bg_color="#292929", font=("ARIAL BOLD", 15))
bottomFotoCarregadaLabel.place(x=124,y=725)

# Saída Frame

bottomSaidaFrame = ctk.CTkFrame(regApp, width=640, height=44, bg_color="#242424", fg_color="#292929", corner_radius=0)
bottomSaidaFrame.place(x=0,y=806)

# Saída Label

bottomSaidaLabel = ctk.CTkLabel(regApp, text_color="#8E8E8E",text="Saída: ", bg_color="#292929", font=("INTER BOLD", 15))
bottomSaidaLabel.place(x=40,y=815)

# Func buttons

# Adicione um rótulo para exibir a imagem
display_label = None  # Defina display_label como uma variável global

def carregarFoto():
    global display_label  # Indique que estamos usando a variável global

    try:
        # Abre o arquivo de imagem
        file_path = filedialog.askopenfilename(title="Selecione a Foto do Agente", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            raise ValueError("Nenhum arquivo selecionado.")

        # Redimensiona a imagem para 150x120 usando LANCZOS
        img = Image.open(file_path)
        img = img.resize((150, 120), Image.LANCZOS)

        # Salva a imagem na pasta agentIcons com o nome do agenteID
        agentID = agentIDEntry.get()
        img.save(f"assets/agentIcons/{agentID}.png", format="PNG")

        # Se display_label ainda não foi criado, crie-o
        if display_label is None:
            display_label = ctk.CTkLabel(regApp)
            display_label.place(x=105, y=681)

        # Exibe a imagem no display
        img = ImageTk.PhotoImage(img)
        display_label.configure(image=img)
        display_label.image = img

        # Oculta o bottomFotoCarregadaLabel após carregar a imagem com sucesso
        bottomFotoCarregadaLabel.place_forget()

    except Exception as e:
        print(f"Erro ao carregar a foto: {e}")
        bottomSaidaLabel.configure(regApp, text=f"Saída: Erro ao carregar a foto - {e}")

def registrarAgente():
    try:
        # Obter dados do formulário
        agentID = agentIDEntry.get()
        regionID = regionIDEntry.get()
        agentShift = optionMenuTurno.get()
        agentName = nomeEntry.get()
        agentManagerName = gerenteEntry.get()
        regionEND = endEntry.get()

        # Verificar se todos os campos estão preenchidos
        if not all([agentID, regionID, agentShift, agentName, agentManagerName, regionEND]):
            raise ValueError("Preencha todos os campos antes de registrar um agente.")

        # Verificar se a foto foi carregada
        if not os.path.exists(f"assets/agentIcons/{agentID}.png"):
            raise ValueError("Carregue a foto do agente antes de registrar.")

        dados_agente = [agentID, agentName, agentShift, agentManagerName, regionID, regionEND, timeOnFunc]

        print(f"{agentName} registrado com sucesso sob o ID: {agentID}")
        bottomSaidaLabel.configure(regApp, text=f"Saída: {agentName} registrado no ID: {agentID}")

        with sqlite3.connect('usuarios.db') as banco:
            cursor = banco.cursor()
            cursor.execute('INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?, ?)', dados_agente)

    except ValueError as ve:
        print(f"Erro ao registrar agente: {ve}")
        bottomSaidaLabel.configure(regApp, text=f"Saída: Erro ao registrar agente - {ve}")

    except sqlite3.Error as e:
        print(f"Erro ao interagir com o banco de dados: {e}")
        bottomSaidaLabel.configure(regApp, text=f"Saída: Erro ao interagir com o banco de dados - {e}")

 
# Bottom Buttons

# Frame 1

bottomBtnFrame1 = ctk.CTkFrame(regApp, width=180, height=206, bg_color="#242424", fg_color="#292929", corner_radius=10)
bottomBtnFrame1.place(x=390,y=644)

# Frame 2
bottomBtnFrame2 = ctk.CTkFrame(regApp, width=180, height=63, bg_color="#242424", fg_color="#383838", corner_radius=0)
bottomBtnFrame2.place(x=390,y=743)

# BTNS

bottomUploadIcon = ctk.CTkButton(regApp, width=153, height=30, fg_color="#454545", bg_color="#292929", text="Carregar Foto", text_color="#FFFFFF", font=("Impact Bold", 15), corner_radius=10, hover_color="#A5A5A5", command=carregarFoto)
bottomUploadIcon.place(x=403, y=655)

bottomBtnRegistrar = ctk.CTkButton(regApp, width=153, height=44, fg_color="#000000", bg_color="#292929",text="Registrar", text_color="#FFFFFF", font=("Impact Bold", 20), corner_radius=25, hover_color="#595959", command=registrarAgente)
bottomBtnRegistrar.place(x=403,y=695)

bottomBtnAtualizar = ctk.CTkButton(regApp, width=75, height=30, fg_color="#0E2713", bg_color="#383838",text="Atualizar", text_color="#FFFFFF", font=("Impact Bold", 10), corner_radius=25, hover_color="#329347")
bottomBtnAtualizar.place(x=403,y=755)

bottomBtnRemover = ctk.CTkButton(regApp, width=75, height=30, fg_color="#5B1010", bg_color="#383838",text="Remover", text_color="#FFFFFF", font=("Impact Bold", 10), corner_radius=25, hover_color="#A31F1F")
bottomBtnRemover.place(x=481,y=755)

regApp.mainloop()