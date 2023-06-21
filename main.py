from tkinter import *


# Okno
window = Tk()
window.title("TO-DO List")
window.minsize(550, 500)
window.iconbitmap("icon.ico")
window.resizable(False, False)

# Fonty a barvy
my_font = ("Verdana", 12)
bg_color = "#73e0fa"
button_color = "#07a7cd"
window.config(bg=bg_color)

# Funkce
def add_item():
    # přidání úkolu
    text_area.insert(END, user_input.get())
    user_input.delete(0, END)

def remove_item():
    # odstraní jednu položku seznamu
    text_area.delete(ANCHOR)

def remove_list():
    # odstraní celý seznam úkolů
    text_area.delete(0, END)

def save_file():
    # uloží úkoly do textového souboru
    with open("tasks.txt", "w") as file:
        my_tasks = text_area.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(one_task)
            else:
                file.write(f"{one_task}\n")

def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for one_line in file:
                text_area.insert(END, one_line)
    except:
        print("Chyba ve funkci na otevírání souboru tasks.txt")

# Frames - založení
input_frame = Frame(window, bg=bg_color)
text_frame = Frame(window, bg=bg_color)
button_frame = Frame(window, bg=bg_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Input frame - content
user_input = Entry(input_frame, width=35, borderwidth=3, font=my_font)
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button = Button(input_frame, text="Add", borderwidth=2, font=my_font, bg=button_color, command=add_item)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=29)

# Scrollbar
scrollbar_text = Scrollbar(text_frame)
scrollbar_text.grid(row=0, column=1, sticky=N+S)

# Text frame - content
text_area = Listbox(text_frame, width=45, height=20, borderwidth=3, font=my_font, yscrollcommand=scrollbar_text.set)
text_area.grid(row=0, column=0)

# Propojení Scrollbar s text_are
scrollbar_text.config(command=text_area.yview)

# Button frame - content
remove_button = Button(button_frame, text="Remove item", borderwidth=2, font=my_font, bg=button_color, command=remove_item)
clear_button = Button(button_frame, text="Remove all", borderwidth=2, font=my_font, bg=button_color, command=remove_list)
save_button = Button(button_frame, text="Save", borderwidth=2, font=my_font, bg=button_color, command=save_file)
quit_button = Button(button_frame, text="Close", borderwidth=2, font=my_font, bg=button_color, command=window.destroy)

remove_button.grid(row=0, column=0, padx=2, pady=10, ipadx=7)
clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=7)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=22)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=22)


# Načteme seznam úkolů do text_area
open_tasks()


# Hlavní cyklus
window.mainloop()