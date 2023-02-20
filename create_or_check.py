import tkinter as tk
import password_generator
import re

root = tk.Tk()
root.geometry("800x600")

root.title("Password creator")


# set up the window
empty = tk.Label(text="")
empty.grid(row=0, column=0, rowspan=2)

main_label = tk.Label(text="Test a password, or create a new one!", font=20)
main_label.grid(row=0, column=1)

enter_password_label = tk.Label(text="Enter your password: ")
enter_password_label.grid(row=1, column=0)

enter_password_entry = tk.Entry()
enter_password_entry.grid(row=1, column=1)

test_password_button = tk.Button(
    text="test your password!", command=lambda: password_generator.test_strength(enter_password_entry.get()))
test_password_button.grid(row=2, column=1)

create_password = tk.Button(text="create a strong password!",
                            command=lambda: password_generator.generate_password())
create_password.grid(row=2, column=3)


root.mainloop()
