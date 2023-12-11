import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

loginWindow = ctk.CTk()
loginWindow.title('The Frank Spreadsheets | Login')

loginWindow._set_appearance_mode("dark")
loginWindow.state('normal')
loginWindow.geometry("350x500")
loginWindow.resizable(False, False)

# Logo

partyLogo = ctk.CTkImage(dark_image=Image.open(r"assets\yinyang.png"), size=(200,190))
ctk.CTkLabel(loginWindow, text=None, image=partyLogo, fg_color="#242424", corner_radius=500).place(x=75, y=26)

# Entrys

entryUserID = ctk.CTkEntry(loginWindow, 
                         width=300,
                         height=40,
                         fg_color="#C5C2C2",
                         placeholder_text="ID de Agente:",
                         placeholder_text_color="#808080",  # Cor mais suave para o texto do espaço reservado
                         text_color="black",
                         corner_radius=15,
                         bg_color="#242424",
                         border_width=0
                         )
entryUserID.place(x=25, y=240)

entryCodReg = ctk.CTkEntry(loginWindow, 
                         width=300,
                         height=40,
                         fg_color="#C5C2C2",
                         placeholder_text="Código da Região:",
                         placeholder_text_color="#808080",  # Cor mais suave para o texto do espaço reservado
                         text_color="black",
                         corner_radius=15,
                         bg_color="#242424",
                         border_width=0
                         )
entryCodReg.place(x=25, y=320)

# Funcs

def validar_id_usuario(*args):
    user_id = entryUserID.get()

    # Verificar se o ID do usuário possui exatamente 6 caracteres e são todos numéricos
    if len(user_id) != 6 or not user_id.isdigit():
        messagebox.showerror("Erro", "O ID de usuário deve conter exatamente 6 caracteres numéricos.")

entryUserVar = ctk.StringVar()
entryUserVar.trace_add("write", validar_id_usuario)

# BTNs

btnEntrar = ctk.CTkButton(loginWindow,
                             width=300,
                             height=40,
                             text="Entrar",
                             font=("Impact", 20),
                             fg_color="#363636",
                             bg_color="#242424",
                             hover_color="#262626",
                             corner_radius=5)
btnEntrar.place(x=25, y=380)

btnTempAcesso = ctk.CTkButton(loginWindow,
                             width=150,
                             height=30,
                             text="Solicitar Acesso",
                             font=("Impact", 15),
                             fg_color="#363636",
                             bg_color="#242424",
                             hover_color="#262626",
                             corner_radius=5)
btnTempAcesso.place(x=100, y=443)

radioBtnContinuarLogado = ctk.CTkRadioButton(loginWindow,
                                            width=150,
                                            height=30,
                                            text="Lembrar ID.",
                                            font=("Impact", 14),
                                            fg_color="#363636",
                                            bg_color="#242424",
                                            border_width_checked=1,
                                            border_width_unchecked=1,
                                            border_color="#363636",
                                            hover_color="#FFFFFF",
                                            corner_radius=100)
radioBtnContinuarLogado.place(x=25, y=285)
 
loginWindow.mainloop()
