import customtkinter as ctk
from data_lol import banco
from PIL import Image, ImageTk
import sqlite3


cursor = banco.cursor()
cadItem1 = ctk.CTk()
cadItem1.title('Cadastro de Itens')
cadItem1.geometry('400x500')
cadItem1.resizable(False, False)
cadItem1.attributes('-topmost', True)

# Func

def novoItem():
    try:
        # Verifica se todos os campos foram preenchidos
        if not nome_do_item.get() or not id_do_item.get() or not tier_do_item.get() or not preco_do_item.get() or not atributos_do_item.get() or not passiva_do_item.get():
            raise ValueError("Todos os campos devem ser preenchidos.")

        # Constrói o comando SQL
        comando_sql = f"INSERT INTO items VALUES ('{nome_do_item.get()}', {id_do_item.get()}, '{tier_do_item.get()}', {preco_do_item.get()}, '{atributos_do_item.get()}', '{passiva_do_item.get()}')"

        # Executa o comando SQL
        cursor.execute(comando_sql)
        
        # Comita as alterações no banco de dados
        banco.commit()
        labelCadItem.configure(text='Ultimo Cadastrado:\n'+str(id_do_item)+'')

        print("Item cadastrado com sucesso!")
    except ValueError as ve:
        print(f"Erro ao cadastrar item: {ve}")
    except Exception as e:
        print(f"Erro ao cadastrar item: {e}")


# Frames

frameTopo = ctk.CTkFrame(cadItem1, width=400, height=110, fg_color="#EB8D98", corner_radius=0)
frameTopo.place(x=0,y=0)

logoNegaoCorpIMG = ctk.CTkImage(dark_image=Image.open(r"assets\mainIcon.png"), size=(124,124))
ctk.CTkLabel(cadItem1, text=None, image=logoNegaoCorpIMG, bg_color="#EB8D98").place(x=232 ,y=-7)

frameEsquerda = ctk.CTkFrame(cadItem1, width=212, height=390, fg_color="#C97575", corner_radius=0)
frameEsquerda.place(x=188,y=110)

frameDireita = ctk.CTkFrame(cadItem1, width=188, height=390, fg_color="#E7B8B8", corner_radius=0)
frameDireita.place(x=0,y=110)

frameEsquerdaBaixo = ctk.CTkFrame(cadItem1, width=160, height=95, fg_color="#5F3D55", corner_radius=0)
frameEsquerdaBaixo.place(x=17,y=400)

# Labels

labelCadItem = ctk.CTkLabel(cadItem1, text="Ultimo Cadastrado:\n", text_color="#580828", font=("arial bold", 25), bg_color="#EB8D98")
labelCadItem.place(x=9,y=11)

labelID = ctk.CTkLabel(cadItem1, text="ID:", font=("arial bold", 20), text_color="#414247", fg_color="#E7B8B8")
labelID.place(x=31,y=118)

labelNome = ctk.CTkLabel(cadItem1, text="NOME:", font=("arial bold", 20), text_color="#414247", fg_color="#E7B8B8")
labelNome.place(x=31,y=164)

labelTier = ctk.CTkLabel(cadItem1, text="TIER:", font=("arial bold", 20), text_color="#414247", fg_color="#E7B8B8")
labelTier.place(x=31,y=210)

labelPreco = ctk.CTkLabel(cadItem1, text="PREÇO:", font=("arial bold", 20), text_color="#414247", fg_color="#E7B8B8")
labelPreco.place(x=31,y=256)

labelAtributos = ctk.CTkLabel(cadItem1, text="ATRIBUTOS:", font=("arial bold", 20), text_color="#414247", fg_color="#E7B8B8")
labelAtributos.place(x=31,y=302)

labelPassiva = ctk.CTkLabel(cadItem1, text="PASSIVA:", font=("arial bold", 20), text_color="#414247", fg_color="#E7B8B8")
labelPassiva.place(x=31,y=348)

# Buttons

btnCarregarIcone = ctk.CTkButton(cadItem1, fg_color="#DA69BB", hover_color="#786E55", width=120, height=24, text="Carregar Ícone:", text_color="#414247", bg_color="#E7B8B8", corner_radius=15)
btnCarregarIcone.place(x=37,y=376)

btnSalvarItem = ctk.CTkButton(cadItem1, fg_color="#581044", hover_color="#9D1C79", font=("arial bold", 25),width=170, height=45, text="SALVAR", text_color="#BB708E", bg_color="#C97575", corner_radius=15, command=novoItem)
btnSalvarItem.place(x=209,y=425)

# Entrys

id_do_item = ctk.CTkEntry(cadItem1,
                       placeholder_text="Entre com o ID do item.",
                       placeholder_text_color="#414247",
                       width=200,
                       height=33,
                       font=("arial bold", 10),
                       text_color="#414247",
                       fg_color="#DEA0A0",
                       bg_color="#C97575",
                       corner_radius=0,
                       border_width=0
                       )
id_do_item.place(x=194,y=118)

nome_do_item = ctk.CTkEntry(cadItem1,
                       placeholder_text="Entre com o NOME do item.",
                       placeholder_text_color="#414247",
                       width=200,
                       height=33,
                       font=("arial bold", 10),
                       text_color="#414247",
                       fg_color="#DEA0A0",
                       bg_color="#C97575",
                       corner_radius=0,
                       border_width=0
                       )
nome_do_item.place(x=194,y=165)

tier_do_item = ctk.CTkEntry(cadItem1,
                       placeholder_text="Entre com o TIER do item.",
                       placeholder_text_color="#414247",
                       width=200,
                       height=33,
                       font=("arial bold", 10),
                       text_color="#414247",
                       fg_color="#DEA0A0",
                       bg_color="#C97575",
                       corner_radius=0,
                       border_width=0
                       )
tier_do_item.place(x=194,y=211)

preco_do_item = ctk.CTkEntry(cadItem1,
                       placeholder_text="Entre com o PREÇO do item.",
                       placeholder_text_color="#414247",
                       width=200,
                       height=33,
                       font=("arial bold", 10),
                       text_color="#414247",
                       fg_color="#DEA0A0",
                       bg_color="#C97575",
                       corner_radius=0,
                       border_width=0
                       )
preco_do_item.place(x=194,y=257)

atributos_do_item = ctk.CTkEntry(cadItem1,
                       placeholder_text="Entre com os ATRIBUTOS do item.",
                       placeholder_text_color="#414247",
                       width=200,
                       height=33,
                       font=("arial bold", 10),
                       text_color="#414247",
                       fg_color="#DEA0A0",
                       bg_color="#C97575",
                       corner_radius=0,
                       border_width=0
                       )
atributos_do_item.place(x=194,y=302)

passiva_do_item = ctk.CTkEntry(cadItem1,
                       placeholder_text="Entre com a PASSIVA do item.",
                       placeholder_text_color="#414247",
                       width=200,
                       height=33,
                       font=("arial bold", 10),
                       text_color="#414247",
                       fg_color="#DEA0A0",
                       bg_color="#C97575",
                       corner_radius=0,
                       border_width=0
                       )
passiva_do_item.place(x=194,y=348)


cadItem1.protocol("WM_DELETE_WINDOW", lambda: (banco.close(), cadItem1.destroy()))
cadItem1.mainloop()