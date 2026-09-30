import re
import string
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#tela principal
#========================================================
root = tk.Tk()
root.title("Gerador de Senhas Seguras")
root.geometry("450x250")
titulo = tk.Label(
    root,
    text="Gerador de Senhas Seguras",
    font=("Segoe UI", 18, "bold"),
    fg="#003366"
)
titulo.pack(pady=15)

label = tk.Label(root, text="Selecione abaixo quantos caracteres você deseja em sua senha: ")
label.pack()

horizontal_scale = tk.Scale(root, from_=12, to=30, orient="horizontal")
horizontal_scale.pack()

text_widget = tk.Text(root, height=1, width=34)
text_widget.pack()
text_widget.tag_configure("centralizado", justify="center")
#========================================================

#Exceção
#========================================================
class LengthError(Exception):
    pass
#========================================================

#Pegar o valor selecionado no Slider
#========================================================
def get_scale_value():
    return horizontal_scale.get()
#========================================================

#Geração da senha
#========================================================
def generate_random():
    
    COMMON_SPECIALS = "!@#$%&*?"

    possible_characters = list(
        string.ascii_letters +
        string.digits +
        COMMON_SPECIALS
    )
    password_characters = [random.choice(possible_characters) for _ in range(get_scale_value())]
    return "".join(password_characters)
#========================================================

#Validação de caracteres da senha
#========================================================
def is_valid(password):
    pattern = (
        r"^(?=.*[a-z])"      # pelo menos uma minúscula
        r"(?=.*[A-Z])"       # pelo menos uma maiúscula
        r"(?=.*\d)"          # pelo menos um número
        r"(?=(?:.*[!@#$%&*?]){4,})"  # pelo menos quatro caracteres especiais permitidos
        r"[A-Za-z\d!@#$%&*?]+$"
    )

    return re.match(pattern, password) is not None
#========================================================

#Validação final e recall da geração até uma senha válida ser gerada
#========================================================
def validate_password():
    try:
        if int(get_scale_value()) < 12:
            raise LengthError
    except LengthError:
        messagebox.showerror("Erro", "The minimun length is 12, please enter a 12 or greater length")
    else:
        password = None        
        while True:
            password = generate_random()
            if is_valid(password):
                break
        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", password)
        text_widget.tag_add("centralizado", "1.0", "end")
#========================================================

#Botão de submit
#========================================================
submit_button = tk.Button(
    root,
    text="Gerar Senha",
    command=validate_password,
    bg="#003366",
    fg="white",
    font=("Segoe UI",11,"bold"),
    padx=20,
    pady=8,
    cursor="hand2"
)
submit_button.pack(pady=10)
#========================================================

root.mainloop()