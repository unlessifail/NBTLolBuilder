import customtkinter as ctk
from tkinter import *
from PIL import Image
import os

appPCC = ctk.CTk()
appPCC.title('The Frank Spreadsheets | Management Integrated System')

appPCC._set_appearance_mode("dark")
appPCC.state('normal')
appPCC.geometry("1440x850")

# variaveis kkk

agentID = "69420"
agentName = "Frank Nóia"
agentShift = "Noite | 23:00 - 05:00"
agentManagerName = "Marcola"
regionID = "011"
regionEND = "Rodovia Raposo Tavares, Km 623"
timeOnFunc = "03:45:29"
currentPageName = "PÁGINA INICIAL"

# Frames

mainTopFrame = ctk.CTkFrame(appPCC, 
                               width=1100,
                               height=70,
                               fg_color="#242424",
                               bg_color="#242424",
                               corner_radius=0,
                               )

mainTopFrame.place(x=340,y=0)

centerTopFrame = ctk.CTkFrame(appPCC, 
                               width=1100,
                               height=45,
                               fg_color="#404040",
                               bg_color="#242424",
                               corner_radius=0,
                               )

centerTopFrame.place(x=340,y=70)

agentIconFrame = ctk.CTkFrame(appPCC, 
                               width=150,
                               height=120,
                               fg_color="#242424",
                               bg_color="#242424",
                               corner_radius=0,
                               )

agentIconFrame.place(x=95,y=23) 

mainCenterFrame = ctk.CTkFrame(appPCC, 
                               width=1100,
                               height=615,
                               fg_color="#242424",
                               bg_color="#242424",
                               corner_radius=0,
                               )

mainCenterFrame.place(x=340,y=115)

mainLeftFrame = ctk.CTkFrame(appPCC, 
                               width=340,
                               height=730,
                               fg_color="#303030",
                               bg_color="#242424",
                               corner_radius=0,
                               )

mainLeftFrame.place(x=0,y=0)

mainBottomFrame = ctk.CTkFrame(appPCC, 
                               width=1440,
                               height=120,
                               fg_color="#1F1F1F",
                               bg_color="#242424",
                               corner_radius=0,
                               )

mainBottomFrame.place(x=0,y=730)

# IMG Home Page

homePageIMG = ctk.CTkImage(dark_image=Image.open(r"assets\bgFrankSpreadsheetsIMG.jpg"), size=(1110,615))

ctk.CTkLabel(appPCC, text=None, image=homePageIMG).place(x=340, y=115)

# IMG Agent Pic

image_path = os.path.join('assets', 'userIcons', agentID + '.png')
agentPicIMG = ctk.CTkImage(dark_image=Image.open(image_path), size=(150, 120))
ctk.CTkLabel(appPCC, text=None, image=agentPicIMG).place(x=95, y=23)

# Button Funcs

def laborFuncStartEvent():
    print("Iniciou a função")

def laborFuncPauseEvent():
    print("Pausou a função")

def closeCurrentPageEvent():
    print("Fechou a página atual")

# Left Menu Button Funcs

def checkInventoryEvent():
    print("Ver Estoque")

def registerProductEvent():
    print("Registrar Mercadoria")

    # Create Register Framework

    

def financialReportsEvent():
    print("Relatórios Financeiros")

def cashBoxClosingEvent():
    print("Fechamento de Caixa")

def agentsReportsEvent():
    print("Relação de Agentes")

def managerPageEvent():
    print("Gerência")

def emergencyChannelEvent():
    print("Canal de Emergência")

def leaveButtonEvent():
    print("Saindo...")
    appPCC.destroy()

def selectFunctionBarEvent(functionSelected):
    print(functionSelected)
    selectedFunctionLabel.configure(text="FUNÇÃO: " + functionSelected)

# Select Function Bar

selectFunctionBar = ctk.CTkOptionMenu(appPCC,
                                     values=['Chefe de facção', 'Subchefe', 'Disciplina', 'Tesoureiro', 'Armeiro',
                                             'Mensageiro', 'Vigarista', 'Assassino', 'Recrutador', 'Padrinho'],
                                     width=446,
                                     height=25,
                                     fg_color="#454545",
                                     bg_color="#242424",
                                     font=("Syne", 10),
                                     button_color="#808080",
                                     corner_radius=0,
                                     hover="#5D5D5D",
                                     command=selectFunctionBarEvent,
                                     )

selectFunctionBar.set("Funçâo: ")
selectFunctionBar.place(x=340,y=22)

# Buttons

btnFuncStart = ctk.CTkButton(appPCC,
                               text="INICIAR FUNÇÃO",
                               width=100,
                               height=25,
                               font=("Syne", 10),
                               fg_color="#808080",
                               bg_color="#242424",
                               corner_radius=10,
                               hover_color="#5C5B5B",
                               command=laborFuncStartEvent,
                               )

btnFuncStart.place(x=845,y=23)

btnFuncPause = ctk.CTkButton(appPCC,
                               text="PAUSAR FUNÇÃO",
                               width=100,
                               height=25,
                               font=("Syne", 10),
                               fg_color="#808080",
                               bg_color="#242424",
                               corner_radius=10,
                               hover_color="#5C5B5B",
                               command=laborFuncPauseEvent,
                               )

btnFuncPause.place(x=981,y=23)

btnCloseCurrentPage = ctk.CTkButton(appPCC,
                               text="FECHAR",
                               width=100,
                               height=45,
                               font=("Syne", 20),
                               fg_color="#808080",
                               bg_color="#404040",
                               corner_radius=0,
                               hover_color="#959595",
                               command=closeCurrentPageEvent,
                               )

btnCloseCurrentPage.place(x=1320,y=70)

# Left Menu Buttons

btnCheckInventory = ctk.CTkButton(appPCC,
                               text="VER ESTOQUE",
                               width=294,
                               height=60,
                               font=("Syne", 20),
                               fg_color="#6A6A6A",
                               bg_color="#303030",
                               corner_radius=5,
                               hover_color="#878787",
                               command=checkInventoryEvent,
                               )

btnCheckInventory.place(x=23,y=219)

btnRegisterProduct = ctk.CTkButton(appPCC,
                               text="REGISTRAR MERCADORIA",
                               width=294,
                               height=60,
                               font=("Syne", 20),
                               fg_color="#6A6A6A",
                               bg_color="#303030",
                               corner_radius=5,
                               hover_color="#878787",
                               command=registerProductEvent,
                               )

btnRegisterProduct.place(x=23,y=305)

btnfinancialReports = ctk.CTkButton(appPCC,
                               text="RELATÓRIO FINANCEIRO",
                               width=294,
                               height=60,
                               font=("Syne", 20),
                               fg_color="#6A6A6A",
                               bg_color="#303030",
                               corner_radius=5,
                               hover_color="#878787",
                               command=financialReportsEvent,
                               )

btnfinancialReports.place(x=23,y=391)

btnCashBoxClosing = ctk.CTkButton(appPCC,
                               text="FECHAMENTO DE CAIXA",
                               width=294,
                               height=60,
                               font=("Syne", 20),
                               fg_color="#6A6A6A",
                               bg_color="#303030",
                               corner_radius=5,
                               hover_color="#878787",
                               command=cashBoxClosingEvent,
                               )

btnCashBoxClosing.place(x=23,y=477)

btnAgentsReports = ctk.CTkButton(appPCC,
                               text="RELAÇÃO DE AGENTES",
                               width=294,
                               height=60,
                               font=("Syne", 20),
                               fg_color="#6A6A6A",
                               bg_color="#303030",
                               corner_radius=5,
                               hover_color="#878787",
                               command=agentsReportsEvent,
                               )

btnAgentsReports.place(x=23,y=563)

btnManagerSection = ctk.CTkButton(appPCC,
                               text="GERÊNCIA",
                               width=294,
                               height=60,
                               font=("Syne", 20),
                               fg_color="#484848",
                               bg_color="#303030",
                               corner_radius=5,
                               hover_color="#373737",
                               command=managerPageEvent,
                               )

btnManagerSection.place(x=23,y=649)

btnEmergencyChannel = ctk.CTkButton(appPCC,
                               text="CANAL DE EMERGÊNCIA",
                               width=280,
                               height=50,
                               font=("Syne", 20),
                               fg_color="#484848",
                               bg_color="#1F1F1F",
                               corner_radius=0,
                               hover_color="#666666",
                               command=emergencyChannelEvent
                               )

btnEmergencyChannel.place(x=1007,y=765)

btnLeaveAll = ctk.CTkButton(appPCC,
                               text="SAIR",
                               width=100,
                               height=50,
                               font=("Syne", 20),
                               fg_color="#484848",
                               bg_color="#1F1F1F",
                               corner_radius=0,
                               hover_color="#666666",
                               command=leaveButtonEvent,
                               )

btnLeaveAll.place(x=1320,y=765)

# Top Labels

agentNameLabel = ctk.CTkLabel(appPCC,
                              text= agentName,
                              font=("Syne", 25),
                              text_color="#FFFFFF",
                              bg_color="#303030",
                              )

agentNameLabel.place(x=95,y=150)

agentIDLabel = ctk.CTkLabel(appPCC,
                              text="MATRÍCULA: " + agentID,
                              font=("Syne", 15),
                              text_color="#FFFFFF",
                              bg_color="#303030",
                              )

agentIDLabel.place(x=95,y=180)

agentShiftLabel = ctk.CTkLabel(appPCC,
                              text="TURNO: " + agentShift,
                              font=("Syne", 20),
                              text_color="#FFFFFF",
                              bg_color="#242424",
                              )

agentShiftLabel.place(x=1134,y=20)

currentPageLabel = ctk.CTkLabel(appPCC,
                              text=currentPageName,
                              font=("Syne", 20),
                              text_color="#FFFFFF",
                              bg_color="#404040",
                              )

currentPageLabel.place(x=366,y=81)

selectedFunctionLabel = ctk.CTkLabel(appPCC,
                              text="FUNÇÃO: ",
                              font=("Syne", 0),
                              text_color="#FFFFFF",
                              bg_color="#1F1F1F",
                              )

selectedFunctionLabel.place(x=23,y=753)

timeOnFuncLabel = ctk.CTkLabel(appPCC,
                              text="TEMPO NA FUNÇÃO: " + timeOnFunc,
                              font=("Syne", 10),
                              text_color="#FFFFFF",
                              bg_color="#1F1F1F",
                              )

timeOnFuncLabel.place(x=23,y=774)

agentManagerNameLabel = ctk.CTkLabel(appPCC,
                              text="GERENTE: " + agentManagerName,
                              font=("Syne", 15),
                              text_color="#FFFFFF",
                              bg_color="#1F1F1F",
                              )

agentManagerNameLabel.place(x=23,y=798)

regionIDLabel = ctk.CTkLabel(appPCC,
                              text="REGIÃO: " + regionID,
                              font=("Syne", 25),
                              text_color="#FFFFFF",
                              bg_color="#1F1F1F",
                              )

regionIDLabel.place(x=340,y=755)

regionENDLabel = ctk.CTkLabel(appPCC,
                              text="ENDEREÇO: " + regionEND,
                              font=("Syne", 20),
                              text_color="#FFFFFF",
                              bg_color="#1F1F1F",
                              )
regionENDLabel.place(x=340,y=795)

appPCC.mainloop()