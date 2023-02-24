import time
import tkinter as tk
from datetime import datetime
def square_and_multiply_always(base, exp, mod):
    
    R0=1
    R1 = base
    c = '{0:b}'.format(exp)
    
    i=len(c)-1
    t=0
    c=c[::-1]
    while(i>=0):
        if(t==0):
            Rt=R0
        elif(t==1):
            Rt=R1
        else:
            print("t != 0 or 1")
        R0=(R0*Rt)%mod
        d=int(c[i])
        t=(t^d)
        i=i-1+t
    return R0

def run_calculation():
    a = int(base_entry.get())
    b = int(exp_entry.get())
    c = int(mod_entry.get())
    start  = datetime.now()

    result = square_and_multiply_always(a, b, c)
    result_label.config(text=f"Le résultat de l'opération est : {result} \nLe temps d'éxécution est {datetime.now()- start} s")




def proche_en_proche_exp (base , exp , mod):
    
    i = 1 
    res = 1
    temp = 1
    if exp == 1 :
        return base % mod
    elif exp == 0 :
        return 1 % mod 
    else :
        while i <= exp :
            if i == 1 :
                temp = base
            else:
                temp = res * base 

            res = temp % mod
            i+=1
    return res 


def run_calculation1():
    

    a = int(base_entry1.get())
    b = int(exp_entry1.get())
    c = int(mod_entry1.get())
    start = datetime.now()
    result = proche_en_proche_exp(a, b, c)
    

    result_label1.config(text=f"Le résultat de l'opération est : {result} \nLe temps d'éxécution est {datetime.now() - start} s")
    
root = tk.Tk()
root.title("TP 3 : Exponentiation modulaire")
text2=tk.Label(root,text="La méthode naive",font=("Arial",15)).grid(row=0,column=0,columnspan=2)

base_label1 = tk.Label(root, text="Base:")
base_label1.grid(row=1, column=0, padx=10, pady=10)

base_entry1 = tk.Entry(root)
base_entry1.grid(row=1, column=1, padx=10, pady=10)

exp_label1 = tk.Label(root, text="Puissance:")
exp_label1.grid(row=2, column=0, padx=10, pady=10)

exp_entry1 = tk.Entry(root)
exp_entry1.grid(row=2, column=1, padx=10, pady=10)

mod_label1 = tk.Label(root, text="Modulo:")
mod_label1.grid(row=3, column=0, padx=10, pady=10)

mod_entry1 = tk.Entry(root)
mod_entry1.grid(row=3, column=1, padx=10, pady=10)

calculate_button1 = tk.Button(root, text="Calculer", command=run_calculation1)
calculate_button1.grid(row=4, column=0, columnspan=2, pady=10)

result_label1 = tk.Label(root, text="")
result_label1.grid(row=5, column=0, columnspan=2)


text1=tk.Label(root,text="Square and multiply ",font=("Arial",15)).grid(row=6,column=0,columnspan=2)

base_label = tk.Label(root, text="Base:")
base_label.grid(row=7, column=0 , padx=10, pady=10)

base_entry = tk.Entry(root)
base_entry.grid(row=7, column=1, padx=10, pady=10)

exp_label = tk.Label(root, text="Puissance:")
exp_label.grid(row=8, column=0 , padx=10, pady=10)

exp_entry = tk.Entry(root)
exp_entry.grid(row=8, column=1 , padx=10, pady=10)

mod_label = tk.Label(root, text="Modulo:")
mod_label.grid(row=9, column=0 , padx=10, pady=10)

mod_entry = tk.Entry(root)
mod_entry.grid(row=9, column=1 , padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculer", command=run_calculation)
calculate_button.grid(row=10, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=2)

root.mainloop()
