import tkinter as tk
import os

def run_tp1():
    os.system('python TP1.py')
    
def run_tp2():
    os.system('python TP2.py')
    
def run_tp3():
    os.system('python TP3.py')
    
def run_tp4():
    os.system('python TP4.py')
    

root = tk.Tk()
root.title("Le menu des implementations")

frame0 = tk.Frame(root)
frame0.pack()

label = tk.Label(frame0, text="Bienvenue dans le menu des implementations", font=("Helvetica", 16))
label.pack()

frame01 = tk.Frame(root)
frame01.pack()

tp1_label = tk.Label(frame01, text="TP1:Reductions modulaire ", font=("Helvetica", 14))
tp1_label.pack()

frame1 = tk.Frame(root)
frame1.pack()

tp1_button = tk.Button(frame1, text="Réduction modulaire en utilisant la méthode de Montgomery", command=run_tp1)
tp1_button.pack()


frame02 = tk.Frame(root)
frame02.pack()

tp2_label = tk.Label(frame02, text="TP2: Euclide etendu ", font=("Helvetica", 14))
tp2_label.pack()

frame2 = tk.Frame(root)
frame2.pack()

tp2_button = tk.Button(frame2, text="Euclide etendu", command=run_tp2)
tp2_button.pack()

frame4 = tk.Frame(root)
frame4.pack()

tp3_label = tk.Label(frame4, text="TP3: Exponentiation modulaire", font=("Helvetica", 14))
tp3_label.pack()

frame5 = tk.Frame(root)
frame5.pack()

tp3_button = tk.Button(frame5, text="Les méthodes d'exponentiation modulaire", command=run_tp3)
tp3_button.pack(side="right")

frame6 = tk.Frame(root)
frame6.pack()

tp4_label = tk.Label(frame6, text="TP4: Différents test de primalité", font=("Helvetica", 14))
tp4_label.pack()


frame7 = tk.Frame(root)
frame7.pack()

tp4_button = tk.Button(frame7, text="Les test de primalité", command=run_tp4)
tp4_button.pack(side="left")

frame7 = tk.Frame(root)
frame7.pack()

root.mainloop()
