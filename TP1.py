import sys
import tkinter as tk
from montred import Montgomery
from datetime import datetime

import tkinter as tk
from datetime import datetime

def getRemainder(num, divisor):
    return (num - divisor * (num // divisor))
 
def calculateN():
    baseN = int(base_entryN.get())
    puissanceN = int(puissance_entryN.get())
    divisorN = int(divisor_entryN.get())
    start=datetime.now()
    numN = pow(baseN, puissanceN)
    resultN = getRemainder(numN, divisorN)
    resultN_label.config(text=f"le résultat de l'opération: ({baseN}^{puissanceN}) (mod {divisorN}) en utilisant la méthode naive est: {resultN}\n le temps d'éxécution est {datetime.now()-start} s")
    #time = datetime.now()-start
    #time_label.config(text=f"le temps pris pour faire ce calcul avec la méthode naive est : {time} s")

# Create the main window
root = tk.Tk()

# Add labels for input instructions
text1=tk.Label(root,text="La méthode Naive ",font=("Arial",15)).grid(row=0,column=0,columnspan=2)
base_label = tk.Label(root, text="Donnez la numero a la base:")
puissance_label = tk.Label(root, text="Donnez la puissance:")
divisor_label = tk.Label(root, text="Donnez le diviseur:")

# Place the input labels in the window
base_label.grid(row=1, column=0, sticky="W")
puissance_label.grid(row=2, column=0, sticky="W")
divisor_label.grid(row=3, column=0, sticky="W")

# Add entry boxes for user input
base_entryN = tk.Entry(root)
puissance_entryN = tk.Entry(root)
divisor_entryN = tk.Entry(root)

# Place the entry boxes in the window
base_entryN.grid(row=1, column=1)
puissance_entryN.grid(row=2, column=1)
divisor_entryN.grid(row=3, column=1)

# Add button to initiate calculation
calculateN_button = tk.Button(root, text="Calculer", command=calculateN)
calculateN_button.grid(row=4, column=0, columnspan=2, pady=10)

# Add labels to display resultNs
resultN_label = tk.Label(root, text="")
resultN_label.grid(row=5, column=0, columnspan=2)

time_label = tk.Label(root, text="")
time_label.grid(row=6, column=0, columnspan=2)

start=datetime.now()

# Run the main loop
#root.mainloop()


# Path: montred.py
def calculate():
    a = int(base_entry.get())
    b = int(power_entry.get())

    while True:
        try:
            c = int(modulus_entry.get())
            if c < 3 or c % 2 == 0:
                raise ValueError("Le modulus doit etre impaire et plus grand que trois")
            break
        except ValueError as ve:
            result_label.config(text=ve)
            return

    print (f"x={a}, y={b}, c={c}")
    start=datetime.now()

    mr = Montgomery(c)
    aval=mr.convert_in(a)
    bval=mr.convert_in(b)
    res=mr.convert_out(mr.pow(aval,b))

    #print (f" le résultat est: \n({a}^{b}) (mod {c})={res}")
    #print ("le temps pris pour faire ce calcul avec la méthode de Montgomery : ",datetime.now()-start, "s")
    result_label.config(text=f"le résultat de l'opération: ({a}^{b}) (mod {c}) en utilisant la méthode de montgomery est: {res}\n le temps d'éxécution est {datetime.now()-start} s")

#root = tk.Tk()
root.title("TP1: Les reductions modulaires")
text1=tk.Label(root,text="La méthode de montgomery",font=("Arial",15)).grid(row=7,column=0,columnspan=2)
base_label = tk.Label(root, text="Donnez la numero a la base : ")
base_entry = tk.Entry(root)
power_label = tk.Label(root, text="donnez la puissance : ")
power_entry = tk.Entry(root)
modulus_label = tk.Label(root, text="donnez le diviseur : ")
modulus_entry = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculer", command=calculate)
result_label = tk.Label(root, text="")


base_label.grid(row=8, column=0, sticky="W")
base_entry.grid(row=8, column=1)
power_label.grid(row=9, column=0, sticky="W")
power_entry.grid(row=9, column=1)
modulus_label.grid(row=10, column=0, sticky="W")
modulus_entry.grid(row=10, column=1)
calculate_button.grid(row=11, column=0, columnspan=2, pady=10)
result_label.grid(row=12, column=0, columnspan=2)

root.mainloop()
