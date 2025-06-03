import customtkinter as ctk
from tkinter import messagebox 
registro = {}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.title("Registro Elettronico")
app.geometry("700x550")


# PARTE HOME
frame_home=ctk.CTkFrame(app)
frame_home.pack(fill="both", expand=True)


label_home=ctk.CTkLabel(frame_home, text="Benvenuto nella home")
label_home.pack(pady=20)


btn_aggiungi=ctk.CTkButton(frame_home, text="Aggingi Studenti", command=lambda: switch_frame(frame_aggiungi))
btn_aggiungi.pack(pady=10)


btn_voto=ctk.CTkButton(frame_home, text="Inserisci Voti", command=lambda: switch_frame(frame_inserisci_voti))
btn_voto.pack(pady=10)  

btn_stampa=ctk.CTkButton(frame_home, text="Stampa Voti", command=lambda: switch_frame(frame_stampa_voti))
btn_stampa.pack(pady=10)




#DEF AGGIUNGI STUDENTE
def aggiungiStudente():
    nome_studente= entry_nome_aggiungi.get().strip().lower()
    if nome_studente == "":
        messagebox.showerror("Errore", "Inserisci un nome valido!")
    elif nome_studente in registro:
        messagebox.showerror("Errore", "Studente già presente!")
    else:
        registro[nome_studente]={"pratico": list(), "teorico": list(), "orale": list()}
    
    entry_nome_aggiungi.delete(0, ctk.END) 





# PARTE AGGIUNGI STUDENTI
frame_aggiungi=ctk.CTkFrame(app)


label_aggiungi=ctk.CTkLabel(frame_aggiungi, text="Aggingi Nome dello Sturdente")
label_aggiungi.pack(pady=20)


entry_nome_aggiungi = ctk.CTkEntry(frame_aggiungi, placeholder_text="Nome Studente")
entry_nome_aggiungi.pack(pady=20)

btn_aggingi_studente=ctk.CTkButton(frame_aggiungi, text="Aggiungi Studente", command=aggiungiStudente)
btn_aggingi_studente.pack(pady=10)



btn_home_aggiungi=ctk.CTkButton(frame_aggiungi, text="INDIETRO", command=lambda: switch_frame(frame_home))
btn_home_aggiungi.pack(pady=10)



#DEF PRATICO, TEORICO, ORALE
def VotoPratico():
    nome_studente=entry_nome_voti.get().strip().lower()
    voto_Pratico=entry_pratico.get().strip()
    if nome_studente == "" or voto_Pratico == "":
        messagebox.showerror("Errore", "Inserisci nome e voto valido!")
    elif nome_studente not in registro:
        messagebox.showerror("Errore","Studente non trovato!")
    else:
        registro[nome_studente]["pratico"].append(voto_Pratico)
    entry_pratico.delete(0, ctk.END)  
    entry_nome_voti.delete(0, ctk.END)  


def VotoTeorico():
    nome_studente=entry_nome_voti.get().strip().lower()
    voto_Teorico=entry_teorico.get().strip()
    if nome_studente == "" or voto_Teorico == "":
        messagebox.showerror("Errore", "Inserisci nome e voto valido!")
    elif nome_studente not in registro:
        messagebox.showerror("Errore","Studente non trovato!")
    else:
        registro[nome_studente]["teorico"].append(voto_Teorico)
    entry_teorico.delete(0, ctk.END)
    entry_nome_voti.delete(0, ctk.END)

def VotoOrale():
    nome_studente=entry_nome_voti.get().strip().lower()
    voto_Orale=entry_orale.get().strip()
    if nome_studente == "" or voto_Orale == "":
        messagebox.showerror("Errore", "Inserisci nome e voto valido!")
    elif nome_studente not in registro:
        messagebox.showerror("Errore","Studente non trovato!")
    else:
        registro[nome_studente]["orale"].append(voto_Orale)
    entry_orale.delete(0, ctk.END)  
    entry_nome_voti.delete(0, ctk.END)



# PARTE INSERISCI VOTI
frame_inserisci_voti=ctk.CTkFrame(app)



label_nome_studente=ctk.CTkLabel(frame_inserisci_voti, text="NOME STUDENTE", font=("Arial", 20))
label_nome_studente.pack(pady=20)

entry_nome_voti = ctk.CTkEntry(frame_inserisci_voti, placeholder_text="Nome Studente")
entry_nome_voti.pack(pady=20)



label_voti=ctk.CTkLabel(frame_inserisci_voti, text="INSERISCI IL VOTO", font=("Arial", 20))
label_voti.pack(pady=20)



entry_pratico=ctk.CTkEntry(frame_inserisci_voti, placeholder_text="PRATICO")
entry_pratico.pack(pady=10)



btn_pratico=ctk.CTkButton(frame_inserisci_voti, text="Aggiungi Voto Pratico", command=VotoPratico)
btn_pratico.pack(pady=10)

entry_teorico=ctk.CTkEntry(frame_inserisci_voti, placeholder_text="TEORICO")
entry_teorico.pack(pady=10)



btn_teorico=ctk.CTkButton(frame_inserisci_voti, text="Aggiungi Voto Teorico", command=VotoTeorico)
btn_teorico.pack(pady=10)

entry_orale=ctk.CTkEntry(frame_inserisci_voti, placeholder_text="ORALE")
entry_orale.pack(pady=10)



btn_orale=ctk.CTkButton(frame_inserisci_voti, text="Aggiungi Voto Orale", command=VotoOrale)
btn_orale.pack(pady=10)



btn_home_voto=ctk.CTkButton(frame_inserisci_voti, text="INDIETRO", command=lambda: switch_frame(frame_home))
btn_home_voto.pack(pady=10)


def StampaVoti():
    nome_stampa=entry_nome_stampa.get().strip().lower()
    if nome_stampa == "":
        messagebox.showerror("Errore", "inserisci un nome valido!")
    elif nome_stampa in registro:
        stampa.configure(text=f"I voti di {str.capitalize(nome_stampa)} sono:\n"
                            f"Pratico: {registro[nome_stampa]['pratico']}\n"
                            f"Teorico: {registro[nome_stampa]['teorico']}\n"
                            f"Orale: {registro[nome_stampa]['orale']}")
    else:
        messagebox.showerror("Errore","Studente non trovato!")
    entry_nome_stampa.delete(0, ctk.END)  


#FRAME STAMPA VOTI
frame_stampa_voti = ctk.CTkFrame(app)

entry_nome_stampa=ctk.CTkEntry(frame_stampa_voti, placeholder_text="Nome Studente")
entry_nome_stampa.pack(pady=20) 

btn_stampa_voti = ctk.CTkButton(frame_stampa_voti, text="STAMPA I VOTI", command=StampaVoti)
btn_stampa_voti.pack(pady=10)

stampa=ctk.CTkLabel(frame_stampa_voti, text="")
stampa.pack(pady=20)

btn_indietro_stampa = ctk.CTkButton(frame_stampa_voti, text="INDIETRO", command=lambda: switch_frame(frame_home))
btn_indietro_stampa.pack(pady=10)


def switch_frame(new_frame):
    for widget in app.winfo_children():
        widget.pack_forget()  
    new_frame.pack(fill="both", expand=True)  

switch_frame(frame_home)

app.mainloop()