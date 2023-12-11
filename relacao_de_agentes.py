import customtkinter as ctk

relAgent = ctk.CTk()

relAgent.title('The Frank Spreadsheets | Relação de Agentes')
relAgent._set_appearance_mode("dark")
relAgent.state('normal')
relAgent.geometry("400x200")
relAgent.resizable(False, False)

btnRegistrarAgente = ctk.CTkButton(relAgent, font=("Impact Bold", 12),fg_color="#303030", bg_color="#242424", hover_color="#5B5B5B",width=250, height=30, text_color="#FFFFFF",text="REGISTRAR AGENTE", corner_radius=25)
btnRegistrarAgente.place(x=75,y=35)

btnListarAgentes = ctk.CTkButton(relAgent, font=("Impact Bold", 12),fg_color="#303030", bg_color="#242424", hover_color="#5B5B5B",width=250, height=30, text_color="#FFFFFF",text="LISTAR AGENTES", corner_radius=25)
btnListarAgentes.place(x=75,y=85)

btnRegistrarAgente = ctk.CTkButton(relAgent, font=("Impact Bold", 12),fg_color="#303030", bg_color="#242424", hover_color="#5B5B5B",width=250, height=30, text_color="#FFFFFF",text="ALTERAR DADOS DE CLIENTES", corner_radius=25)
btnRegistrarAgente.place(x=75,y=135)

relAgent.mainloop()