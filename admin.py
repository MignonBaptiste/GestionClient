from subprocess import  call
from  tkinter import  ttk, Tk
from tkinter import *
import mysql.connector as MC

from tkinter import messagebox

class Admin:
    def __init__(self):
        # Créer la fenêtre
        self.window = Tk()
        self.window.title("PAGE ADMINISTRATION")
        self.window.geometry("1350x750+0+0")
        self.window.resizable(False, False)
        self.window.config(bg="#A91821")

        # Ajouter un titre
        h2 = Label(self.window, borderwidth=3, relief=SUNKEN, text="GESTION DES CLIENTS ", font=("sans serif", 25), bg="#DF4F4F", fg="#FFFAFA")
        h2.place(x=0, y=0, width=1350, height=100)

        # Ajouter un titre pour le formulaire
        h1 = Label(self.window, text="formulaire d'inscription des clients", font=("helvetica", 18), bg="#A91821", fg="#FFFAFA")
        h1.place(x=50, y=150, width=450)

        # Ajouter un champ pour le nom
        lbnom = Label(self.window, text="NOM :", font=("Arial", 18), bg="#A91821", fg="white")
        lbnom.place(x=70, y=250, width=150)
        self.Champnom = Entry(self.window, bd=4, font=("Arial", 14))
        self.Champnom.place(x=250, y=250, width=300)

        # Ajouter un champ pour le prénom
        lbp = Label(self.window, text="PRENOM :", font=("Arial", 18), bg="#A91821", fg="white")
        lbp.place(x=70, y=300, width=150)
        self.ChampP = Entry(self.window, bd=4, font=("Arial", 14))
        self.ChampP.place(x=250, y=300, width=300)

        #ajouter un champ pour le mail 
        email = Label(self.window, text="E-MAIL :", font=("Arial", 18), bg="#A91821", fg="white")
        email.place(x=70, y=350, width=150)
        self.champmail = Entry(self.window, bd=4, font=("Arial", 14))
        self.champmail.place(x=250, y=350, width=300)

        # Ajouter une liste déroulante pour le programme
        lbMatiere = Label(self.window, text="Programme :", font=("Arial", 18), bg="#A91821", fg="white")
        lbMatiere.place(x=70, y=400, width=130)
        self.matiere1 = ttk.Combobox(self.window, font=("Arial", 16))
        self.matiere1['value'] = ['Perte de poids', 'Total perfection']
        self.matiere1.place(x=250, y=400, width=210)

        # Ajouter un champ pour l'abonnement
        lbNote = Label(self.window, text="Abonnement :", font=("Arial", 18), bg="#A91821", fg="white")
        lbNote.place(x=70, y=450, width=150)
        self.ChampNote = ttk.Combobox(self.window, font=("Arial", 16))
        self.ChampNote['value'] = ['Premium','Normal']
        self.ChampNote.place(x=250, y=450, width=130)

        # Ajouter un champ pour la date d'inscription
        types = Label(self.window, text="DATE:", font=("Arial", 18), bg="#A91821", fg="white")
        types.place(x=50, y=500, width=200)
        self.type_user = Entry(self.window, bd=4, font=("Arial", 14))
        self.type_user.place(x=250, y=500, width=130)


        #Enregistrer
        btnE = Button(self.window, text="Enregistrer", font=("Arial", 16), bg="#C1231E", fg="white", command=self.ajouter)
        btnE.place(x=250, y=600, width=200)


        #voir list
        btnS = Button(self.window, text="Modifier", font=("Arial", 16), bg="#C1231E", fg="white", command=self.modifier)
        btnS.place(x=250, y=650, width=200)

        #Enregistrer
        btnE = Button(self.window, text="Supprimer", font=("Arial", 16), bg="#C1231E", fg="white", command=self.supprimer)
        btnE.place(x=250, y=700, width=200)

        


        #le taleau 
        self.tree = ttk.Treeview(self.window, columns=(1, 2, 3, 4, 5, 6,7), height=5, show="headings")
        self.tree.heading(1, text="ID")
        self.tree.heading(2, text=" NOM")
        self.tree.heading(3, text="PRENOM")
        self.tree.heading(4, text="MAIL")
        self.tree.heading(5, text="PROGRAMME")
        self.tree.heading(6, text="ABONNEMENT")
        self.tree.heading(7, text="DATE")

        # Définir les dimensions des colonnes:
        self.tree.column(1, width=30)
        self.tree.column(2, width=100)
        self.tree.column(3, width=100)
        self.tree.column(4, width=100)
        self.tree.column(5, width=50)
        self.tree.column(6, width=50)
        self.tree.column(7, width=50)


        #entete
        

        self.tree.place(x=560,y=150, height=450, width=790)

        # Afficher les informations dans le tableau:
        con = MC.connect(host="localhost", user="root", password="", database="gestionclient")
        cur = con.cursor()
        cur.execute("SELECT * FROM inscription")
        for row in cur:
            self.tree.insert('', END, value=row)
            

        #afficher la fenetre
        self.window.mainloop()

    def vider(self):
        self.Champnom.delete("0", "end")
        self.ChampP.delete("0", "end")
        self.champmail.delete("0", "end")
        self.matiere1.delete("0", "end")
        self.ChampNote.delete("0", "end")
        self.type_user.delete("0", "end")
        
        
    

    
    def ajouter(self):
        # Vérifier si les champs obligatoires sont vides
        if self.Champnom.get() == "" or self.ChampP.get() == "" or self.champmail.get() == "" or self.matiere1.get() == "" or self.ChampNote.get() == "" or self.type_user.get() == "":
            messagebox.showerror("", "Merci de remplir tous les champs du formulaire.")
        else:
            con = MC.connect(host="localhost", user="root", password="", database="gestionclient")
            cur = con.cursor()
            
            # Vérifier si les valeurs existent déjà dans la base de données
            cur.execute("SELECT * FROM inscription WHERE nom = %s AND prenom = %s AND email = %s", (self.Champnom.get(), self.ChampP.get(), self.champmail.get()))
            row = cur.fetchone()
            if row:
                messagebox.showerror("", "Ce client existe déjà dans la base de données.")
                self.vider()
            else:
                # Insérer les valeurs dans la base de données
                sql = "INSERT INTO inscription (nom, prenom, email, programme, abonnement, date) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (self.Champnom.get(), self.ChampP.get(), self.champmail.get(), self.matiere1.get(), self.ChampNote.get(), self.type_user.get())
                cur.execute(sql, val)
                con.commit()
                messagebox.showinfo("Information", "Client enregistré.")
                self.vider()
                self.window.destroy()
                call(["python", "admin.py"])

    
    # Ajouter un bouton pour la suppression

    # Définir la méthode de suppression
    def supprimer(self):
        # Récupérer l'ID de l'étudiant sélectionné dans le tableau
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Aucun enregistrement sélectionné.")
            return
        item = self.tree.item(selected_item)
        id_etudiant = item['values'][0]

        # Supprimer l'enregistrement de la base de données
        con = MC.connect(host="localhost", user="root", password="", database="gestionclient")
        cur = con.cursor()
        cur.execute("DELETE FROM inscription WHERE id = %s", (id_etudiant,))
        con.commit()
        cur.close()
        con.close()

        # Mettre à jour le tableau
        self.tree.delete(selected_item)
        messagebox.showinfo("Succès", "Enregistrement supprimé avec succès.")

    def modifier(self):
        # Récupérer les valeurs des champs
        id = self.tree.item(self.tree.selection())['values'][0]
        nom = self.Champnom.get()
        prenom = self.ChampP.get()
        maile =self.champmail.get()
        formation = self.matiere1.get()
        option = self.ChampNote.get()
        date = self.type_user.get()

        # Vérifier si toutes les valeurs sont remplies
        if not nom or not prenom or not formation or not option or not  maile  or not date:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs avant de modifier")
            return

        # Mettre à jour les données dans la base de données
        con = MC.connect(host="localhost", user="root", password="", database="gestionclient")
        cur = con.cursor()
        cur.execute("UPDATE inscription SET nom=%s, prenom=%s,email=%s ,programme=%s, abonnement=%s ,date=%s  WHERE id=%s",
                    (nom, prenom, maile,formation,option ,date, id))
        con.commit()
        con.close()

        # Mettre à jour les données dans le tableau
        self.tree.item(self.tree.selection(), values=(id,nom, prenom, maile,formation,option ,date))

        # Afficher un message de succès
        messagebox.showinfo("Succès", "Les informations ont été modifiées avec succès")
        self.window.destroy()
        call(["python","admin.py"])

   
    
    




if __name__ == "__main__":
    Admin()


       
