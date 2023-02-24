import os
import tkinter as tk
from tkinter import messagebox
#LA FONCTION QUI CALCULE LE PGCD DE DEUX NOMBRES
def pgcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

#LA FONCTION DE L'ALGORITHME D'EUCLIDE ETENDU 
def euce(a,b):

    q = [-1,-1]
    r = [a,b]
    u = [1,0]
    v = [0,1]

    while r[-1] > 0:
        q.append(r[-2]//r[-1])
        r.append(r[-2]%r[-1])
        u.append(u[-2]-q[-1]*u[-1])
        v.append(v[-2]-q[-1]*v[-1])
    return r[-2],u[-2],v[-2]

#Tkinter GUI
root = tk.Tk()
root.title("TP2: Euclide Etendu")
root.geometry("650x450")

a_label = tk.Label(root, text="Donner un premier nombre 'a': ")
a_label.pack()

a_entry = tk.Entry(root)
a_entry.pack()

b_label = tk.Label(root, text="Donner un deuxième nombre 'b': ")
b_label.pack()

b_entry = tk.Entry(root)
b_entry.pack()



def submit1():
    a = int(a_entry.get())
    b = int(b_entry.get())

    pgcd_result = pgcd(a, b)
    output_text1.insert("insert", f"Le PGCD de {a} et {b} en utilisant l'algortihme d'euclide est: {pgcd_result}\n")
    output_text1.insert("insert", "-+-+-+-+-+-+-+-+-+-+-+\n")

    pgcde, u, v = euce(a, b)
   

    if (pgcd_result == 1):

        pgcde, u, v = euce(a, b)
        output_text1.insert("insert", f"Calcule des conficient de bezout en utilisant l'algorithme d'euclide etendu :\n {pgcde} = {u} * {a} + {v} * {b}\n")
        output_text1.insert("insert", f'Les coeficient de bezout sont: u = {u} et v = {v}\n')
        output_text1.insert("insert", "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

    else:
        messagebox.showerror("Erreur", "Vous ne pouvez pas calculer les coefficients de Bézout car \nLe pgcd entre ces deux nombres n'est pas 1 !\nVeuillez introduire deux nouveaux nombres premiers entre eux !")

    



submit_button1 = tk.Button(root, text="Calculer", command=submit1)
submit_button1.pack()

output_text1 = tk.Text(root, height=5, width=90)
output_text1.pack()





n_label = tk.Label(root, text="Donner le nombre 'N' pour le quelle on veut calculer l'inverse: ")
n_label.pack()

n_entry = tk.Entry(root)
n_entry.pack()

p_label = tk.Label(root, text="Donner le modulo 'p': ")
p_label.pack()

p_entry = tk.Entry(root)
p_entry.pack()


output_text = tk.Text(root, height=5, width=80)
output_text.pack()

def submit():
   
    
    n = int(n_entry.get())
    p = int(p_entry.get())

    pgcde, v, u = euce(n,p)

    if pgcde == 1:
        output_text.insert("insert", f"L'inverse de {n} modulo {p} est: {v}\n")
        output_text.insert("insert", "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    else:
        output_text.insert("insert", f"L'inverse de {n} modulo {p} n'existe pas\n")
        output_text.insert("insert", "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")




submit_button = tk.Button(root, text="Calculer", command=submit)
submit_button.pack()

root.mainloop()



    

