import tkinter as tk

def converter_temperatura():
    celsius1 = float(campo_celsios.get())
    fahrenheit1 = float(campo_fahrenheit.get())

    fahrenheit2 = (celsius1 * 1.8) + 32
    celsius2 = (fahrenheit1 - 32) / 1.8

    resultado_f.config(text=f"Resultado: {celsius1}ºC = {fahrenheit2:.2f}ºF")
    resultado_c.config(text=f"Resultado: {fahrenheit1}ºF = {celsius2:.2f}ºC")

root = tk.Tk()
root.title("conversor de temperatura")
root.geometry("800x650")

texto_celsios = tk.Label(root, text="digite uma temperatura em grau celsios: ")
texto_celsios.pack(pady=10)

campo_celsios = tk.Entry(root)
campo_celsios.pack()



resultado_f = tk.Label(root)
resultado_f.pack(pady=5)



texto_fahrenheit = tk.Label(root, text="digite uma temperatura em fahrenheit: ")
texto_fahrenheit.pack(pady=10)

campo_fahrenheit = tk.Entry(root)
campo_fahrenheit.pack()

botao_fahrenheit = tk.Button(root, text="confirmar", command= converter_temperatura)
botao_fahrenheit.pack(pady=15)

resultado_c = tk.Label(root)
resultado_c.pack(pady=5)

root.mainloop()