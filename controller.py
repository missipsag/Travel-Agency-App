from tkinter import messagebox
from model import ModeleVoyage
from view import ViewVoyage

class ControllerVoyage:
    def __init__(self):
        self.modele = ModeleVoyage()
        self.view = ViewVoyage(self)
        self.view.run()

    def ajouter_voyage(self):
         if self.view.verifier_date():
            data = (
                self.view.destination_var.get(),
                self.view.date_depart_var.get(),
                self.view.date_retour_var.get(),
                self.view.prix_var.get(),
                self.view.places_dispo_var.get(),
                self.view.description_var.get()
                     )
            try:
                 self.modele.ajouter_voyage(data)
                 self.view.reinitialiser_formulaire_ajout_voyage()
                 messagebox.showinfo("Succès", "Voyage ajouté avec succès!")
                 self.view.charger_tt_reservations() #refresher la pagep
            except Exception as e:
                 messagebox.showerror("Erreur", str(e))

    def rechercher_voyage(self, destination):
        try:
            resultats = self.modele.rechercher_voyage(destination)
            return resultats
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
            return []

    def tt_reservations(self):
        try:
            resultats = self.modele.get_voyage()
            return resultats
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
            return []    
    
    def supprimer_voyage(self, id):
        try:
            self.modele.supprimer_voyage(id)
            messagebox.showinfo("Succès", "Voyage supprimé avec succès!")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def run(self): 
        self.view.root.mainloop()

if __name__ == "__main__" : 
    controller = ControllerVoyage()
    controller.run()
