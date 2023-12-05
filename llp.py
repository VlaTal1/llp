import numpy as np
from utils import LLP
import tkinter as tk


win = tk.Tk()
win.title("LLP")
win.geometry("500x600")

K_size = (3, 5)
K_inputs = []
P_inputs = []


def handle_k_size():
    new_size = (int(rows_amount.get()), int(columns_amount.get()))
    draw_core(new_size=new_size)

def get_values():
    global K_size
    global K_inputs
    global P_inputs

    k = []
    for i in range(K_size[0]):
        row = []
        for j in range(K_size[1]):
            row.append(int(K_inputs[i][j].get()))
        k.append(row)

    p = []
    for i in range(K_size[1]):
        p.append(int(P_inputs[i].get()))

    q = []
    for i in range(K_size[0]):
        q.append(0)

    return np.array(k), np.array(p), np.array(q)
        

def calculate():
    k, p, q = get_values()
    llp = LLP()

    p = p.reshape(len(p), 1)
    q = q.reshape(len(q), 1)   

    print(k)
    print(p)
    print(q)

    llp.linear_logical_transform(k, p, q)

    for i in range (len(llp.Qh)):
        print(f"\t\tStep #{i + 1}")
        print("P: ")
        print(f"{llp.Ph[i]}")
        print("Q: ")
        print(f"{llp.Qh[i]}")
        print("===================================")


def draw_core(new_size: tuple):
    global K_size
    global K_inputs
    global P_inputs

    ##TODO make reset
    # global K_inputs
    # if len(K_inputs) != 0:
    #     for i in range(K_size[0]):
    #         for j in range(K_size[1]):
    #             K_inputs[i][j].destroy()
    #     K_inputs = []

    tk.Label(win, text="Ядро").grid(row=3, column=0, sticky="W")
    for i in range(new_size[0]):
        row = []
        for j in range(new_size[1]):
            entry = tk.Entry(win, width=10)
            row.append(entry)
            entry.grid(row=i + 4, column=j, padx=(0, 5), pady=(0, 5))
        K_inputs.append(row)
    
    tk.Label(win, text="P").grid(row=4 + K_size[0] + 1, column=0, sticky="W")
    for i in range(new_size[1]):
        entry = tk.Entry(win, width=10)
        P_inputs.append(entry)
        entry.grid(row=i + 5 + K_size[0] + 1, column=0, padx=(0, 5), pady=(0, 5))

    tk.Button(win, text="Розрахувати", command=calculate).grid(row=6 + K_size[0] + len(P_inputs) + 1, column=0)


tk.Label(win, text="Кількість строк:").grid(row=0, column=0, sticky="W")
rows_amount = tk.Entry(win)
rows_amount.grid(row=0, column=1)
tk.Label(win, text="Кількість стовпців:").grid(row=1, column=0, sticky="W")
columns_amount = tk.Entry(win)
columns_amount.grid(row=1, column=1)
tk.Button(win, text="Прийняти", command=handle_k_size).grid(
    row=2, column=0, columnspan=2, sticky="WE", pady=(10, 30))


win.mainloop()


# P = np.array([1, 1, 0, 0, 1])
# Q = np.array([0, 0, 0])

# K = np.array([[1, 1, 0, 0, 0],
#               [0, 0, 0, 1, 0],
#               [0, 0, 0, 1, 1]])


# P = P.reshape(len(P), 1)
# Q = Q.reshape(len(Q), 1)

# llp = LLP()

# llp.linear_logical_transform(K, P, Q)

# for i in range (len(llp.Qh)):
#     print(f"\t\tStep #{i + 1}")
#     print("P: ")
#     print(f"{llp.Ph[i]}")
#     print("Q: ")
#     print(f"{llp.Qh[i]}")
#     print("===================================")
