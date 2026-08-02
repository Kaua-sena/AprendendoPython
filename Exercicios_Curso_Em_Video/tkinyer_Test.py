import tkinter as tk


janela = tk.Tk()

contents = tk.StringVar(value="Essa e um variavel")

entry = tk.Entry(janela, text="entrada", background="gainsboro", value=str)
entry.pack()
saida = tk.Button(janela, text="saida", command=entry)
saida.pack()
nome = entry.pack()
janela.mainloop()
print(nome)
