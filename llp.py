import numpy as np
from utils import LLP
import tkinter as tk

class MainWindow:

    def __init__(self) -> None:
        self.win = tk.Tk()
        self.win.title("LLP")
        self.win.geometry("500x600")

        self.rows_amount = 0
        self.columns_amount = 0

        self.K_size = None
        self.K_inputs = []
        self.P_inputs = []

    def handle_k_size(self):
        new_size = (int(self.rows_amount.get()), int(self.columns_amount.get()))
        self.draw_core(new_size=new_size)

    def get_values(self):
        k = []
        for i in range(self.K_size[0]):
            row = []
            for j in range(self.K_size[1]):
                row.append(int(self.K_inputs[i][j].get()))
            k.append(row)

        p = []
        for i in range(self.K_size[1]):
            p.append(int(self.P_inputs[i].get()))

        q = []
        for i in range(self.K_size[0]):
            q.append(0)

        return np.array(k), np.array(p), np.array(q)
            

    def calculate(self):
        k, p, q = self.get_values()
        llp = LLP()

        p = p.reshape(len(p), 1)
        q = q.reshape(len(q), 1)   

        print(k)
        print(p)
        print(q)

        llp.linear_logical_transform(k, p, q)

        print("===================================")
        for i in range (len(llp.Qh)):
            print(f"\t\tStep #{i + 1}")
            print("P: ")
            print(f"{llp.Ph[i]}")
            print("Q: ")
            print(f"{llp.Qh[i]}")
            print("===================================")


    def draw_core(self, new_size: tuple):
        ##TODO make reset
        # global K_inputs
        # if len(K_inputs) != 0:
        #     for i in range(K_size[0]):
        #         for j in range(K_size[1]):
        #             K_inputs[i][j].destroy()
        #     K_inputs = []

        self.K_size = new_size

        tk.Label(self.win, text="Ядро").grid(row=3, column=0, sticky="W")
        for i in range(new_size[0]):
            row = []
            for j in range(new_size[1]):
                entry = tk.Entry(self.win, width=10)
                row.append(entry)
                entry.grid(row=i + 4, column=j, padx=(0, 5), pady=(0, 5))
            self.K_inputs.append(row)
        
        tk.Label(self.win, text="P").grid(row=4 + self.K_size[0] + 1, column=0, sticky="W")
        for i in range(new_size[1]):
            entry = tk.Entry(self.win, width=10)
            self.P_inputs.append(entry)
            entry.grid(row=i + 5 + self.K_size[0] + 1, column=0, padx=(0, 5), pady=(0, 5))

        tk.Button(self.win, text="Розрахувати", command=self.calculate).grid(row=6 + self.K_size[0] + len(self.P_inputs) + 1, column=0)

    def run(self):
        tk.Label(self.win, text="Кількість строк:").grid(row=0, column=0, sticky="W")
        self.rows_amount = tk.Entry(self.win)
        self.rows_amount.grid(row=0, column=1)
        tk.Label(self.win, text="Кількість стовпців:").grid(row=1, column=0, sticky="W")
        self.columns_amount = tk.Entry(self.win)
        self.columns_amount.grid(row=1, column=1)
        tk.Button(self.win, text="Прийняти", command=self.handle_k_size).grid(
            row=2, column=0, columnspan=2, sticky="WE", pady=(10, 30))
        self.win.mainloop()


if __name__ == "__main__":
    main_win = MainWindow()
    main_win.run()


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
