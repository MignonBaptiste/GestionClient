from subprocess import  call
from  tkinter import  ttk, Tk
from tkinter import messagebox
import  mysql.connector as MC
from tkinter import *



def login():
    user = champu.get()
    mdp = champ.get()
    

    if(user=="" and mdp==""):
        messagebox.showerror("","Merci de bien remplir tous les champs de ce formulaire.")
        champu.delete("0", "end")
        champ.delete("0", "end")
    
    else:
        con = MC.connect(host="localhost", user="root", password="", database="gestionclient")
        cur = con.cursor()
        sql = "SELECT * FROM Admin WHERE email = %s AND  motdepasse = %s "
        cur.execute(sql, (user, mdp))
        resultat = cur.fetchone()
        if resultat:
            messagebox.showinfo(user, "Bienvenue"+" "+user)
            window.destroy()
            call(["python","admin.py"])
           
        else:
            messagebox.showwarning("Message Erreur", "Nom de l'utilisateur ou mot de passe incorecte ")
            champu.delete("0", "end")
            champ.delete("0", "end")
            window.destroy()



window = Tk()
window.title('FENETRE DE CONNEXION')
window.geometry("400x350+450+200")
window.resizable(False,  False)
window.config(bg = "#A91821")


#ajouter un titre:
h1 = Label(window,borderwidth=3,relief=SUNKEN ,text="Formulaire de connexion", font = ("sans serif",25),bg="#091821", fg="white" )
h1.place(x=0, y=0, width=400)


#ajouter un mot:utilisateur et son champ:
u = Label(window,text="Utilisateur:", font = ("Arial",14),bg="#A91821", fg="white" )
u.place(x=5, y=100, width=150)
champu = Entry(window, bd=3, font=("Arial",13))
champu.place(x=150, y=100,width=200, height=30)

#ajouter un mot:password et son champ
um = Label(window,text="Mot de passe:", font = ("Arial",14),bg="#A91821", fg="white" )
um.place(x=5, y=150, width=150)
champ = Entry(window,show="*", bd=4, font=("Arial",13))
champ.place(x=150, y=155,width=200, height=30)




#creaction du boutton
btn1 = Button(window, text="connexion",font=("Arial",16),bg="#FF4500", fg="white", command=login )
btn1.place(x=150, y=230, width=200)




#afficher la fenetre :
window.mainloop()
