import tkinter as tk
from tkinter import ttk, messagebox, Scrollbar
from tkcalendar import DateEntry

class ViewVoyage:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Système de Gestion de Voyages")
        self.root.geometry("800x600")
        style = ttk.Style()
        style.theme_use('default')

        
        # Variables pour les champs
        self.destination_var = tk.StringVar()
        self.date_depart_var = tk.StringVar()
        self.date_retour_var = tk.StringVar()
        self.prix_var = tk.DoubleVar()
        self.description_var = tk.StringVar()
        self.places_dispo_var = tk.IntVar()

        # Interface utilisateur
        self.UI()

    def reinitialiser_formulaire_ajout_voyage(self):
        self.destination_var.set("")
        self.date_depart_var.set("")
        self.date_retour_var.set("")
        self.prix_var.set("")
        self.description_var.set("")
        self.places_dispo_var.set("")
    
    def setup_notebook_style(self):
        style = ttk.Style()
        style.configure("TNotebook", background="#f0f0f0", borderwidth=0)
        style.configure("TNotebook.Tab", background="#e1e1e1", foreground="#000000", font=("Arial", 10))
        style.map("TNotebook.Tab", background=[("selected", "#2e8b57")], foreground=[("selected", "white")], expand=[("selected",[1,1,1,0])])


    def UI(self):

        #Initialise l'interface utilisateur avec Notebook qui contient deux onglets:
        #- "Ajouter Voyage" pour ajouter un nouveau voyage.
        #- "Recherche Voyage" pour rechercher des voyages existants.
        self.notebook = ttk.Notebook(self.root)
        self.aj_fen = ttk.Frame(self.notebook)
        self.rech_fen = ttk.Frame(self.notebook)

        self.aj_fen = tk.Frame(self.notebook, bg='#faf9f6')
        self.rech_fen =tk.Frame(self.notebook, bg='#faf9f6')

        self.notebook.add(self.aj_fen, text="Ajouter Voyage")
        self.notebook.add(self.rech_fen, text="Recherche Voyage")
        self.notebook.pack(expand=True, fill="both")

        self.ajout_fenetre()
        self.fenetre_recherche()
    

    def ajout_fenetre(self):

        # Labels et champs de saisie
        labels = ["Destination", "Date Départ", "Date Retour",
                  "Prix", "Places Disponibles", "Description"]
       
        tk.Label(self.aj_fen, text="Destination", bg='#faf9f6').grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        tk.Label(self.aj_fen, text="*", bg='#faf9f6',fg='red').grid(row=0, column=2, padx=10, pady=5, sticky="nsew")
        tk.Entry(self.aj_fen, textvariable=self.destination_var, bg='white', fg='#000000').grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.aj_fen, text="Date Départ", bg='#faf9f6').grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        tk.Label(self.aj_fen, text="*", bg='#faf9f6',fg='red').grid(row=1, column=2, padx=10, pady=5, sticky="nsew")
        DateEntry(self.aj_fen, textvariable=self.date_depart_var, date_pattern='y-mm-d', bg='white', fg='#000000').grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.aj_fen, text="Date Retour", bg='#faf9f6').grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        tk.Label(self.aj_fen, text="*", bg='#faf9f6',fg='red').grid(row=2, column=2, padx=10, pady=5, sticky="nsew")
        DateEntry(self.aj_fen, textvariable=self.date_retour_var, date_pattern='y-mm-d', bg='white', fg='#000000').grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.aj_fen, text="Prix", bg='#faf9f6').grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        tk.Label(self.aj_fen, text="*", bg='#faf9f6',fg='red').grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
        tk.Entry(self.aj_fen, textvariable=self.prix_var, bg='white', fg='#000000').grid(row=3, column=1, padx=10, pady=5) 

        tk.Label(self.aj_fen, text="Places Disponibles", bg='#faf9f6').grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
        tk.Label(self.aj_fen, text="*", bg='#faf9f6',fg='red').grid(row=4, column=2, padx=10, pady=5, sticky="nsew")
        tk.Entry(self.aj_fen, textvariable=self.places_dispo_var, bg='white', fg='#000000').grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.aj_fen, text="Description", bg='#faf9f6').grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
        tk.Label(self.aj_fen, text="*", bg='#faf9f6',fg='red').grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
        tk.Entry(self.aj_fen, textvariable=self.description_var, bg='white', fg='#000000').grid(row=5, column=1, padx=10, pady=5)
        
        # Boutons
        self.ajouter_button = tk.Button(self.aj_fen, text="Ajouter Voyage", command=self.ajouter_voyage, bg="#2e8b57")
        self.ajouter_button.grid(row=len(labels), column=0, columnspan=2, pady=10)
        self.reinit_button = tk.Button(self.aj_fen, text="Reinitialiser", command=self.reinitialiser_formulaire_ajout_voyage, bg="#dc6868")
        self.reinit_button.grid(row=6, column=2, columnspan=2, pady=10)
        self.root.bind('<Return>', self.entree_aj)
        self.root.bind('<Escape>', self.echap_reinit)

        #pour utiliser les touches clavier 
    def entree_aj(self, event): #click sur entrer pour ajouter voyage
        self.ajouter_button.invoke() 
    def echap_reinit(self, event): #click sur echap pour reinitialiser le formulaire
        self.reinit_button.invoke()

    def verifier_date(self):
        date_depart = self.date_depart_var.get()
        date_retour = self.date_retour_var.get()

        if date_depart > date_retour:
            messagebox.showerror("Erreur de date", "La date de départ doit être antérieure à la date de retour.")
            return False
        return True
    
    def ajouter_voyage(self): #fonction pour ajouter un voyage
        data = (
            self.destination_var.get(),
            self.date_depart_var.get(),
            self.date_retour_var.get(),
            self.prix_var.get(),
            self.places_dispo_var.get(),
            self.description_var.get()
        )
        if all(data):
            self.controller.ajouter_voyage()
        else:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires !")

    def fenetre_recherche(self):
        # Barre de recherche
        tk.Label(self.rech_fen, text="Rechercher Destination", bg='#faf9f6').grid(column=0, padx=10, pady=5, sticky="w")
        self.recherche_entry = tk.Entry(self.rech_fen, width=40)
        self.recherche_entry.grid(row=0, column=1, padx=10, pady=5)
        self.recherche_button = tk.Button(self.rech_fen, text="Rechercher", command=self.rechercher_voyage, bg="lightblue")
        self.recherche_button.grid(row=0, column=2, padx=10, pady=5)
        self.recherche_entry.bind('<Return>', self.entree_rech)

        # Table des resultat de recherche
        self.tree = ttk.Treeview(self.rech_fen, columns=("ID", "Destination", "Date Départ", "Date Retour", "Prix",
                                   "Places", "Description"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.v_scrollbar = Scrollbar(self.tree, orient="vertical", bg="grey")
        self.h_scrollbar = Scrollbar(self.tree, orient="horizontal")
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        #pour bloquer(desactiver) le bouton supprimer
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)
        self.tree.bind('<FocusOut>', self.on_tree_focus_out)

        self.supprimer_button = tk.Button(self.rech_fen, text="Supprimer", command=self.supprimer_voyage, bg="#dc6868", state=tk.DISABLED)
        self.supprimer_button.grid(row=2, column=0, columnspan=3, pady=10)
        self.root.bind('<Delete>', self.del_supprimer)

    def del_supprimer(self, event): #click sur Suppr pour supprimer un voyage
        self.supprimer_button.invoke()

        self.charger_tt_reservations()

    def entree_rech(self, event): #click sur entrer pour rechercher un voyage
        self.recherche_button.invoke()

    def on_tree_select(self, event): #activer bouton supprimer quand un voyage est selectionné
        self.supprimer_button.config(state=tk.NORMAL)

    def on_tree_focus_out(self, event): #desactiver bouton supprimer quand un voyage n'est selectionné
        self.supprimer_button.config(state=tk.DISABLED)

    def rechercher_voyage(self): #fonction pour rechercher un voyage
        destination = self.recherche_entry.get()
        results = self.controller.rechercher_voyage(destination)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for result in results:
            self.tree.insert("", "end", values=result)
    
    def charger_tt_reservations(self): #fonction permet d'afficher tout les voyages ajoutés
        results = self.controller.tt_reservations()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for result in results:
            self.tree.insert("", "end", values=result)

    def supprimer_voyage(self): #fonction pour supprimer un voyage
        voyage_selec = self.tree.selection()[0]
        voyage_id= self.tree.item(voyage_selec)['values'][0]
        self.controller.supprimer_voyage(voyage_id)
        self.charger_tt_reservations()
        self.supprimer_button.config(state=tk.DISABLED) #desactiver le bouton supprimer apres exec
        self.root.focus_set() #ou quand il perd le focus

    def run(self): 
        self.root.mainloop()