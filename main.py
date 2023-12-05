import customtkinter as ctk
from PIL import Image

app = ctk.CTk()

# Atributos da Janela

app.title("Negão Builds Technologies")
app.after(0, 
          lambda: app.wm_state('zoomed'))
app.geometry("1440x870")
app._set_appearance_mode("dark")

# Carregando a logo no canto superior esquerdo

logoNegaoCorpIMG = ctk.CTkImage(dark_image=Image.open(r"assets\mainIcon.png"), size=(176,155))
ctk.CTkLabel(app, text=None, image=logoNegaoCorpIMG).place(x=52 ,y=21)

# Chupando os champs

champList = [
    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
    "Aurelion Sol", "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia",
    "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal",
    "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen",
    "Hecarim", "Heimerdinger", "Hecarim", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce",
    "Jhin", "Jinx", "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kennen", "Kha'Zix",
    "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux",
    "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
    "Neeko", "Nidalee", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana",
    "Quinn", "Rakan", "Rammus", "Rek'Sai", "Renekton", "Renata Glasc", "Rengar", "Riven", "Ryze", "Samira", "Senna",
    "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra",
    "Tahm Kench", "Talon", "Taliyah", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate",
    "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick",
    "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean",
    "Zoe", "Zyra"
]

# Chupando os Itens



# Func Role

selected_role = ""

def roleSelected(selected_role_value):
    # Atualize a variável global
    global selected_role
    selected_role = selected_role_value
    
    # Atualize o rótulo com a rota selecionada
    infoSelectedRoleLabel.configure(text=f"{selected_role}", text_color="#D6D94C")

    # Atualize o ícone com base na rota selecionada
    updateRoleIcon()

# Função para atualizar o ícone com base na rota selecionada
def updateRoleIcon():
    if selected_role == "Topo":
        selectedRoleIconIMG = ctk.CTkImage(dark_image=Image.open(r"assets\topIcon.png"), size=(30,30))
    elif selected_role == "Caçador":
        selectedRoleIconIMG = ctk.CTkImage(dark_image=Image.open(r"assets\jgIcon.png"), size=(30,30))
    elif selected_role == "Meio":
        selectedRoleIconIMG = ctk.CTkImage(dark_image=Image.open(r"assets\midIcon.png"), size=(30,30))
    elif selected_role == "Atirador":
        selectedRoleIconIMG = ctk.CTkImage(dark_image=Image.open(r"assets\adcIcon.png"), size=(30,30))
    else:
        selectedRoleIconIMG = ctk.CTkImage(dark_image=Image.open(r"assets\supIcon.png"), size=(30,30))

    # Exiba o ícone no rótulo
    print(selected_role)
    ctk.CTkLabel(app, text=None, image=selectedRoleIconIMG).place(x=1284, y=99)

# Func Champ

def champSelected(selected_champ):
    infoSelectedChampLabel.configure(text=f"{selected_champ}", 
                                     text_color="#68D94C")

# Func Item

def itemSelected(selected_item):
    itemNameLabel.configure(text=f"{selected_item}")

# Menus

dropdownChampMenu = ctk.CTkOptionMenu(app, 
                                    width=355, 
                                    height=45, 
                                    corner_radius=35, 
                                    fg_color="#38393F",
                                    values= champList, 
                                    command=champSelected,
                                    button_color="#595D6B",
                                    button_hover_color="#8A91AB",
                                    dropdown_fg_color="#4B4D50",
                                    bg_color="#242424")

dropdownChampMenu.place(x=244, y=44)
dropdownChampMenu.set("Selecionar um campeão:")

dropdownRoleMenu = ctk.CTkOptionMenu(app, 
                                     width=355, 
                                     height=45, 
                                     corner_radius=35, 
                                     fg_color="#38393F",
                                     values=["Topo", "Caçador", "Meio", "Atirador", "Suporte"],
                                     command=roleSelected,
                                     button_color="#595D6B",
                                     button_hover_color="#8A91AB",
                                     dropdown_fg_color="#4B4D50",
                                     bg_color="#242424")

dropdownRoleMenu.place(x=608, y=44)
dropdownRoleMenu.set("Selecionar uma rota:")

dropdownItemMenu = ctk.CTkOptionMenu(app, width=719, height=40, corner_radius=45, fg_color="#38393F",
                                     values= [""],
                                     command=itemSelected,
                                     button_color="#595D6B",
                                     button_hover_color="#8A91AB",
                                     dropdown_fg_color="#4B4D50",
                                     bg_color="#242424")

dropdownItemMenu.place(x=244, y=136)

# Frames

frameCenter = ctk.CTkFrame(app, 
                           width=937, 
                           height=477, 
                           corner_radius=0, 
                           fg_color="#8A91AB")

frameCenter.place(x=52, y=198)

frameTopRight = ctk.CTkFrame(app, 
                             width=379, 
                             height=155, 
                             corner_radius=0, 
                             fg_color="#333333")

frameTopRight.place(x=1009, y=21)

frameRight = ctk.CTkFrame(app, 
                          width=379, 
                          height=173, 
                          corner_radius=0, 
                          fg_color="#8A91AB")

frameRight.place(x=1009, y=198)

frameSummonerInfo = ctk.CTkFrame(app, 
                              width=339, 
                              height=65, 
                              corner_radius=50, 
                              fg_color="#6A6C81", 
                              bg_color="#8A91AB")

frameSummonerInfo.place(x=1029,y=218)

frameSummonerIcon = ctk.CTkFrame(app, 
                              width=151, 
                              height=65, 
                              corner_radius=0, 
                              fg_color="#353638", 
                              bg_color="#6A6C81")

frameSummonerIcon.place(x=1029,y=218)

frameLevel = ctk.CTkFrame(app, 
                                       width=151, 
                                       height=60, 
                                       corner_radius=25, 
                                       fg_color="#6A6C81", 
                                       bg_color="#8A91AB")

frameLevel.place(x=1029,y=293)

frameRank = ctk.CTkFrame(app, 
                                       width=151, 
                                       height=60, 
                                       corner_radius=25, 
                                       fg_color="#6A6C81", 
                                       bg_color="#8A91AB")

frameRank.place(x=1217,y=293)

frameBottom = ctk.CTkFrame(app, 
                           width=1336, 
                           height=155, 
                           corner_radius=0, 
                           fg_color="#8A91AB")

frameBottom.place(x=52, y=694)

frameItemIcon = ctk.CTkFrame(app, 
                             width=155, 
                             height=135, 
                             corner_radius=0, 
                             fg_color="#353638")

frameItemIcon.place(x=73, y=218)

frameItemNameBox1 = ctk.CTkFrame(app,
                                width=722, 
                                height=65, 
                                corner_radius=0, 
                                fg_color="#545561", 
                                bg_color="#8A91AB")

frameItemNameBox1.place(x=241, y=218)

frameItemTierBox = ctk.CTkFrame(app, 
                                width=220, 
                                height=60, 
                                corner_radius=0, 
                                fg_color="#545561")

frameItemTierBox.place(x=244, y=293)

frameItemAttributesLabelBox = ctk.CTkFrame(app, 
                                           width=890, 
                                           height=35, 
                                           corner_radius=10, 
                                           fg_color="#545561", 
                                           bg_color="#969BAA")

frameItemAttributesLabelBox.place(x=73, y=371)

frameItemPassiveLabelBox = ctk.CTkFrame(app, 
                                        width=890, 
                                        height=35, 
                                        corner_radius=10, 
                                        fg_color="#545561", 
                                        bg_color="#969BAA")

frameItemPassiveLabelBox.place(x=73, y=526)

frameSelectedChampIconBox = ctk.CTkFrame(app, 
                                         width=160, 
                                         height=110, 
                                         corner_radius=0, 
                                         fg_color="#242424")

frameSelectedChampIconBox.place(x=1029, y=44)

frameSelectedChampInfoBox = ctk.CTkFrame(app, 
                                         width=160, 
                                         height=110, 
                                         corner_radius=40, 
                                         fg_color="#242424")

frameSelectedChampInfoBox.place(x=1208, y=44)

frameItemSlot1 = ctk.CTkFrame(app, 
                              width=140, 
                              height=32, 
                              corner_radius=0, 
                              fg_color="#4B4D50")

frameItemSlot1.place(x=310, y=723)

frameItemSlot2 = ctk.CTkFrame(app, 
                              width=140, 
                              height=34, 
                              corner_radius=0, 
                              fg_color="#4B4D50")

frameItemSlot2.place(x=310, y=755)

frameItemSlot3 = ctk.CTkFrame(app,
                              width=140, 
                              height=32, 
                              corner_radius=0, 
                              fg_color="#4B4D50")

frameItemSlot3.place(x=310, y=788)

frameItemSlot4 = ctk.CTkFrame(app, 
                              width=140, 
                              height=32, 
                              corner_radius=0, 
                              fg_color="#4B4D50")

frameItemSlot4.place(x=991, y=723)

frameItemSlot5 = ctk.CTkFrame(app, 
                              width=140, 
                              height=34, 
                              corner_radius=0, 
                              fg_color="#4B4D50")

frameItemSlot5.place(x=991, y=754)

frameItemSlot6 = ctk.CTkFrame(app, 
                              width=140, 
                              height=32, 
                              corner_radius=0, 
                              fg_color="#4B4D50")

frameItemSlot6.place(x=991, y=788)

# Labels dos slots de itens

itemSlot1Label = ctk.CTkLabel(app, 
                              text="vazio",
                              font=("arial bold", 25),
                              text_color="#FFFFFF",
                              bg_color="#4B4D50")

itemSlot1Label.place(x=355 ,y=732)

itemSlot2Label = ctk.CTkLabel(app, 
                              text="vazio",
                              font=("arial bold", 25),
                              text_color="#FFFFFF",
                              bg_color="#4B4D50")

itemSlot2Label.place(x=355 ,y=760)

itemSlot3Label = ctk.CTkLabel(app, 
                              text="vazio",
                              font=("arial bold", 25),
                              text_color="#FFFFFF",
                              bg_color="#4B4D50")

itemSlot3Label.place(x=355 ,y=788)

itemSlot4Label = ctk.CTkLabel(app, 
                              text="vazio",
                              font=("arial bold", 25),
                              text_color="#FFFFFF",
                              bg_color="#4B4D50")

itemSlot4Label.place(x=1033 ,y=732)

itemSlot5Label = ctk.CTkLabel(app, 
                              text="vazio",
                              font=("arial bold", 25),
                              text_color="#FFFFFF",
                              bg_color="#4B4D50")

itemSlot5Label.place(x=1033 ,y=760)

itemSlot6Label = ctk.CTkLabel(app, 
                              text="vazio",
                              font=("arial bold", 25),
                              text_color="#FFFFFF",
                              bg_color="#4B4D50")

itemSlot6Label.place(x=1033 ,y=788)

# Item - Atributo e Passiva. Labels e Frames

frameItemAttributes = ctk.CTkFrame(app, 
                                   width=890, 
                                   height=87, 
                                   fg_color="#A6AABA", 
                                   corner_radius=0, 
                                   bg_color="#8A91AB")

frameItemAttributes.place(x=76 ,y=421)

frameItemAttributesLabelDyn = ctk.CTkLabel(app, 
                                           width=890, 
                                           height=87, 
                                           fg_color="#A6AABA", 
                                           text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent porttitor augue in neque suscipit posuere.",
                                           bg_color="#8A91AB",
                                           text_color="#545561")

frameItemAttributesLabelDyn.place(x=76 ,y=421)

frameItemPassive = ctk.CTkLabel(app, 
                                width=890, 
                                height=87, 
                                fg_color="#A6AABA", 
                                text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent porttitor augue in neque suscipit posuere.",
                                bg_color="#8A91AB",
                                text_color="#545561")

frameItemPassive.place(x=76 ,y=577)

# Labels

summonerLevelLabel = ctk.CTkLabel(app,
                              text="Nível: ",
                              font=("arial bold", 25),
                              text_color="#FFFFFF",
                              bg_color="#6A6C81")

summonerLevelLabel.place(x=1068,y=307)

summonerRankLabel = ctk.CTkLabel(app,
                              text="Rank: ",
                              font=("arial bold", 25),
                              text_color="#FFFFFF",
                              bg_color="#6A6C81")

summonerRankLabel.place(x=1260,y=307)

summonerNameLabel = ctk.CTkLabel(app,
                              text="Nome do invocador:",
                              font=("arial bold", 15),
                              text_color="#FFFFFF",
                              bg_color="#6A6C81")

summonerNameLabel.place(x=1190,y=235)

itemPriceLabel = ctk.CTkLabel(app,
                              text="3200",
                              font=("arial bold", 35),
                              text_color="#FFFFFF",
                              bg_color="#8A91AB")

itemPriceLabel.place(x=878,y=307)

itemSearchLabel = ctk.CTkLabel(app, 
                               text= "Pesquise seus itens abaixo:", 
                               font=("arial bold", 25), 
                               text_color="#FFFFFF", 
                               bg_color="#242424")

itemSearchLabel.place(x=244, y=101)

itemNameLabel = ctk.CTkLabel(app, 
                             text= "Nome do item", 
                             font=("arial bold", 45), 
                             text_color="#FFFFFF", 
                             bg_color="#545561")

itemNameLabel.place(x=255, y=227)

itemTierLabel = ctk.CTkLabel(app, 
                             text= "Tier do item", 
                             font=("arial bold", 35), 
                             text_color="#FFFFFF", 
                             bg_color="#545561")

itemTierLabel.place(x=255, y=307)

itemAttributesLabel = ctk.CTkLabel(app, 
                                   text= "Atributos", 
                                   font=("arial bold", 25), 
                                   text_color="#FFFFFF", 
                                   bg_color="#545561")

itemAttributesLabel.place(x=461, y=373)

itemPassiveLabel = ctk.CTkLabel(app, 
                                text= "Passiva", 
                                font=("arial bold", 25), 
                                text_color="#FFFFFF", 
                                bg_color="#545561")

itemPassiveLabel.place(x=465, y=528)

infoSelectedChampLabel = ctk.CTkLabel(app, 
                                      text= "Nome do campeão: ", 
                                      font=("arial bold", 15), 
                                      text_color="#FFFFFF", 
                                      bg_color="#242424")

infoSelectedChampLabel.place(x=1226, y=59)

infoSelectedRoleLabel = ctk.CTkLabel(app, 
                                     text= "Rota: ", 
                                     font=("arial bold", 15), 
                                     text_color="#FFFFFF", 
                                     bg_color="#242424")

infoSelectedRoleLabel.place(x=1226, y=99)

# Botoes Func

def calcular():
    calculou = "calculado"
    print(calculou)

def adicionar():
    adicionou = "adicionado"
    print(adicionou)

def remover():
    removeu = "removido"
    print(removeu)

def favoritar():
    favoritou = "favoritado"
    print(favoritou)

def comparar():
    comparou = "comparado"
    print(comparou)

# Botoes GUI

btnCalcular = ctk.CTkButton(app, text="Calcular", 
                            font=("arial bold", 40), 
                            command=calcular, 
                            width=380, 
                            height=110, 
                            fg_color="#595D6B", 
                            corner_radius=0, 
                            bg_color="#8A91AB", 
                            hover_color="#424449")

btnCalcular.place(x=530, y=694)

btnAdicionar = ctk.CTkButton(app, text="Adicionar", 
                             font=("arial bold", 15), 
                             command=adicionar, width=200, 
                             height=35, fg_color="#68708C", 
                             corner_radius=0, 
                             bg_color="#8A91AB", 
                             hover_color="#424449")

btnAdicionar.place(x=1168, y=723)

btnRemover = ctk.CTkButton(app, text="Remover", 
                           font=("arial bold", 15), 
                           command=remover, 
                           width=200, 
                           height=35, 
                           fg_color="#68708C", 
                           corner_radius=0, 
                           bg_color="#8A91AB", 
                           hover_color="#424449")

btnRemover.place(x=1168, y=785)

btnComparar = ctk.CTkButton(app, 
                            text="Comparar", 
                            font=("arial bold", 15), 
                            command=comparar, 
                            width=200, 
                            height=35, 
                            fg_color="#68708C", 
                            corner_radius=0, 
                            bg_color="#8A91AB", 
                            hover_color="#424449")

btnComparar.place(x=73, y=723)

btnFavoritar = ctk.CTkButton(app, text="Favoritar", 
                             font=("arial bold", 15), 
                             command=favoritar, 
                             width=200, 
                             height=35, 
                             fg_color="#68708C", 
                             corner_radius=0, 
                             bg_color="#8A91AB", 
                             hover_color="#424449")

btnFavoritar.place(x=73, y=785)

# Carregar Save Func

def loadSave1():
    print("carregado o save 1")

def loadSave2():
    print("carregado o save 2")

def loadSave3():
    print("carregado o save 3")

def loadSave4():
    print("carregado o save 4")

def loadSave5():
    print("carregado o save 5")

def loadSave6():
    print("carregado o save 6")

# Botao Carregar Save GUI

btnLoadSavedBuild01 = ctk.CTkButton(app, text="Carregar Slot I", 
                                    font=("arial bold", 15),  
                                    command=loadSave1, 
                                    width=176, 
                                    height=42, 
                                    fg_color="#757784", 
                                    hover_color="#424449")

btnLoadSavedBuild01.place(x=1212, y=389)

btnLoadSavedBuild02 = ctk.CTkButton(app, text="Carregar Slot II", 
                                    font=("arial bold", 15), 
                                    command=loadSave2, width=176, 
                                    height=42, 
                                    fg_color="#757784", 
                                    hover_color="#424449")

btnLoadSavedBuild02.place(x=1212, y=438)

btnLoadSavedBuild03 = ctk.CTkButton(app, text="Carregar Slot III", 
                                    font=("arial bold", 15), 
                                    command=loadSave3, 
                                    width=176, 
                                    height=42, 
                                    fg_color="#757784", 
                                    hover_color="#424449")

btnLoadSavedBuild03.place(x=1212, y=487)

btnLoadSavedBuild04 = ctk.CTkButton(app, text="Carregar Slot IV", 
                                    font=("arial bold", 15), 
                                    command=loadSave4, 
                                    width=176, height=42, 
                                    fg_color="#757784", 
                                    hover_color="#424449")

btnLoadSavedBuild04.place(x=1212, y=535)

btnLoadSavedBuild05 = ctk.CTkButton(app, text="Carregar Slot V", 
                                    font=("arial bold", 15), 
                                    command=loadSave5, 
                                    width=176, 
                                    height=42, 
                                    fg_color="#757784", 
                                    hover_color="#424449")

btnLoadSavedBuild05.place(x=1212, y=584)

btnLoadSavedBuild06 = ctk.CTkButton(app, text="Carregar Slot VI", 
                                    font=("arial bold", 15),
                                    command=loadSave6, 
                                    width=176, 
                                    height=42, 
                                    fg_color="#757784", 
                                    hover_color="#424449")

btnLoadSavedBuild06.place(x=1212, y=633)

# Salvar Build Func

def saveSlot1():
    print("build salva no slot 1")

def saveSlot2():
    print("build salva no slot 2")

def saveSlot3():
    print("build salva no slot 3")

def saveSlot4():
    print("build salva no slot 4")

def saveSlot5():
    print("build salva no slot 5")

def saveSlot6():
    print("build salva no slot 6")

# Botao Salvar Build GUI

btnSaveBuild01 = ctk.CTkButton(app, text="Salvar no Slot I", 
                               font=("arial bold", 15), 
                               command=saveSlot1, 
                               width=176, 
                               height=42, 
                               fg_color="#757784",
                               hover_color="#424449")

btnSaveBuild01.place(x=1009, y=389)

btnSaveBuild02 = ctk.CTkButton(app, text="Salvar no Slot II", 
                               font=("arial bold", 15), 
                               command=saveSlot2, 
                               width=176, 
                               height=42, 
                               fg_color="#757784",
                               hover_color="#424449")
btnSaveBuild02.place(x=1009, y=438)

btnSaveBuild03 = ctk.CTkButton(app, text="Salvar no Slot III", 
                               font=("arial bold", 15), 
                               command=saveSlot3, 
                               width=176, 
                               height=42, 
                               fg_color="#757784",
                               hover_color="#424449")
btnSaveBuild03.place(x=1009, y=487)

btnSaveBuild04 = ctk.CTkButton(app, text="Salvar no Slot IV", 
                               font=("arial bold", 15), 
                               command=saveSlot4, 
                               width=176, 
                               height=42, 
                               fg_color="#757784",
                               hover_color="#424449")
btnSaveBuild04.place(x=1009, y=535)

btnSaveBuild05 = ctk.CTkButton(app, text="Salvar no Slot V", 
                               font=("arial bold", 15), 
                               command=saveSlot5, 
                               width=176, 
                               height=42, 
                               fg_color="#757784",
                               hover_color="#424449")
btnSaveBuild05.place(x=1009, y=584)

btnSaveBuild06 = ctk.CTkButton(app, text="Salvar no Slot VI", 
                               font=("arial bold", 15), 
                               command=saveSlot6, 
                               width=176, 
                               height=42, 
                               fg_color="#757784",
                               hover_color="#424449")
btnSaveBuild06.place(x=1009, y=633)

app.mainloop()
