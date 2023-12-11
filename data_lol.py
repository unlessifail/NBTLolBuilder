import sqlite3

nome_do_item = ""
id_do_item = 0
tier_do_item = ""
preco_do_item = 0
atributos_do_item = ""
passiva_do_item = ""

banco = sqlite3.connect('itemDb.db')

cursor = banco.cursor()

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

# CRIAR TABELA

# cursor.execute("CREATE TABLE items (nome_do_item text,id_do_item integer,tier_do_item text,preco_do_item integer, atributos_do_item text, passiva_do_item text)")

# INSERIR DADOS

# cursor.execute("CREATE TABLE items (nome_do_item text,id_do_item integer,tier_do_item text,preco_do_item integer, atributos_do_item text, passiva_do_item text)")

# ATUALIZAR DADOS

# cursor.execute("UPDATE items SET nome_do_item = 'Gume dos Infernos' WHERE nome_do_item = "Quebra-Tijolos")

# EXCLUIR DADOS

# cursor.execute("DELETE FROM items WHERE nome_do_item = 'Gume dos Infernos' WHERE nome_do_item = "Quebra-Tijolos")

# ENVIAR AO BANCO

# banco.commit()

# LER DADOS

# cursor.execute("SELECT * FROM items")

# print(cursor.fetchall())