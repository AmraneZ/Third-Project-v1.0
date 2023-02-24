from math import sqrt
from datetime import datetime
import random
import tkinter as tk
from tkinter import StringVar
import AKS_primality as aks
import miller_primality as MR
import millerR_primalityGen as MRG

root = tk.Tk()
root.title("TP4: Différents test de primalité")
root.geometry("1000x400")


def Naive():
    n = int(input1.get())
    start = datetime.now()
    if n < 2:
        result_label1.config(text=f"{n} n'est pas un nombre premier et \n temps d'éxécution est {datetime.now()-start} s")
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                result_label1.config(text=f"{n} n'est pas un nombre premier \n le temps d'éxécution est {datetime.now()-start} s")
                return
                
        result_label1.config(text=f"{n} est un nombre premier \n temps d'éxécution est {datetime.now()-start} s")

def Wilson():
    fac = 1
    n = int(input2.get())
    start = datetime.now()
    for i in range(1, n):   # from 1 to n-1
        fac = (fac * i) % n

    if fac == n-1:
        result_label2.config(text=f"{n}\n est un nombre premier \n temps d'éxécution est {datetime.now()-start} s")
    else:
        result_label2.config(text=f"{n} n\'est pas un nombre premier \n temps d'éxécution est {datetime.now()-start} s")
    
def Fermat():
    n = int(input3_1.get())
    k = int(input3_2.get())
    start = datetime.now()
    for i in range(k):
        a = random.randrange(2, n)  # 2 <= a <= n
        if pow(a, n-1, n) != 1:     # compute a^(n-1) mod n
            result_label3.config(text=f" le nombre n\'est pas premier \n temps d'éxécution est {datetime.now()-start} s")            # definitely composite
            return
    else:
        return result_label3.config(text=f"le nombre est un nombre premier \n temps d'éxécution est {datetime.now()-start} s")                # probably prime

def AKS():
    n = int(input4.get())
    start = datetime.now()
    if aks.aks(n) == True:
        result_label4.config(text=f"{n} est un nombre premier \n temps d'éxécution est {datetime.now()-start} s")
        return
    else:
        result_label4.config(text=f"{n} n\'est pas un nombre premier \n temps d'éxécution est {datetime.now()-start} s")

def RabinMiller():
    n = int(input5_1.get())
    k = int(input5_2.get())
    start = datetime.now()
    if MR.millerRabin(n, k) == True:
        result_label5.config(text=f"le nombre est premier \n temps d'éxécution est {datetime.now()-start} s")
        return
    else:
        result_label5.config(text=f"le nombre n\'est pas premier \n temps d'éxécution est {datetime.now()-start} s")

def MillerGeneration():
    lenght = int(input6.get())
    start = datetime.now()
    MRG.generate_prime_number(lenght)
    result_label6.insert("insert", f"Le nombre premier est \n{MRG.generate_prime_number(lenght)} \n temps d'éxécution est {datetime.now()-start} s")



entry = StringVar()
entry.set("Entrer le nombre de fois a tester 'précision'")

#La méthode naïve
text1 = tk.Label(root, text="La méthode naïve: ")
text1.grid(row=0, column=0, sticky="W")

input1 = tk.Entry(root, width=30)
input1.grid(row=0, column=1)

check_button = tk.Button(root, text="Vérifier", command=Naive)
check_button.grid(row=0, column=2, pady=10)

result_label1 = tk.Label(root, text="", padx=15)
result_label1.grid(row=0, column=3, columnspan=2)


#la méthode de Wilson

text2=tk.Label(root,text="La méthode de Wilson: ")
text2.grid(row=1,column=0,sticky="W")

input2 = tk.Entry(root,width=30 )
input2.grid(row=1, column=1)

button2 = tk.Button(root, text="Verifier", command=Wilson)
button2.grid(row=1, column=2, pady=10, )

result_label2 = tk.Label(root, text="", padx=15)
result_label2.grid(row=1, column=3, columnspan=2)

#fermat test

text3=tk.Label(root,text="La méthode de Fermat: ")
text3.grid(row=2,column=0,sticky="W")

input3_1 = tk.Entry(root,width=30)
input3_1.grid(row=2, column=1)


input3_2 = tk.Entry(root,width=30, textvariable=entry)
input3_2.grid(row=2, column=2)

button3 = tk.Button(root, text="Verifier",command=Fermat)
button3.grid(row=2, column=3, pady=10, )

result_label3 = tk.Label(root, text="", padx=15)
result_label3.grid(row=2, column=4, columnspan=2)

#AKS test
text4=tk.Label(root,text="La méthode de AKS: ")
text4.grid(row=3,column=0,sticky="W")

input4 = tk.Entry(root, width=30)
input4.grid(row=3, column=1)

button4 = tk.Button(root, text="Verifier",command=AKS)
button4.grid(row=3, column=2, pady=10 )

result_label4 = tk.Label(root, text="", padx=15)
result_label4.grid(row=3, column=3, columnspan=2)


def clear (event):
    entry.set("")

input3_2.bind("<FocusIn>", clear)

#Rabin-Miller test
text5=tk.Label(root,text="La méthode de Rabin-Miller: ")
text5.grid(row=4,column=0,sticky="W")

input5_1 = tk.Entry(root, width=30)
input5_1.grid(row=4, column=1)

input5_2 = tk.Entry(root, width=30)
input5_2.grid(row=4, column=2)

button5 = tk.Button(root, text="Verifier", command=RabinMiller)
button5.grid(row=4, column=3, pady=10 )

result_label5 = tk.Label(root, text="", padx=15)
result_label5.grid(row=4, column=4, columnspan=2)

#millerrabin generation
text6=tk.Label(root,text="Miller-Rabin generation: ")
text6.grid(row=5,column=0,sticky="W")

input6 = tk.Entry(root, width=30)
input6.grid(row=5, column=1)

button6 = tk.Button(root, text="Générer", command=MillerGeneration)
button6.grid(row=5, column=2, pady=10 )

result_label6 = tk.Text(root, height=7, width=70)
result_label6.grid(row=6, column=1, columnspan=2)



root.mainloop()