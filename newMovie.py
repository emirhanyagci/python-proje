import tkinter as tk
from tkinter import ttk,messagebox




def open_form(root,saveFn,fetchFn):
    form_window = tk.Toplevel(root)
    form_window.title("Film Bilgileri")
    window_width = 300
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    form_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    tk.Label(form_window, text="Film İsmi:").pack(pady=5)
    film_name_entry = tk.Entry(form_window)
    film_name_entry.pack(pady=5)

    tk.Label(form_window, text="Film Türü:").pack(pady=5)
    film_type_combobox = ttk.Combobox(form_window, values=["Aksiyon", "Komedi", "Dram", "Romantik", "Bilim Kurgu"])
    film_type_combobox.pack(pady=5)

    tk.Label(form_window, text="Film Puani (1-10):").pack(pady=5)
    film_rating_entry = tk.Entry(form_window)
    film_rating_entry.pack(pady=5)
    tk.Label(form_window, text="Film Notu").pack(pady=5)
    film_note_entry = tk.Entry(form_window)
    film_note_entry.pack(pady=5)

    def save_form():
        film_name = film_name_entry.get()
        film_type = film_type_combobox.get()
        film_rate = film_rating_entry.get()
        film_note = film_note_entry.get()
        try:
            film_rating = float(film_rating_entry.get())
            if film_rating < 1 or film_rating > 10:
                raise ValueError("Not 1 ile 10 arasında olmalı.")
        except ValueError as e:
            messagebox.showerror("Hata", f"Geçersiz giriş: {e}")
            return

        messagebox.showinfo("Başarılı", f"Film Adı: {film_name}\nTür: {film_type}\nNot: {film_rating}")
        saveFn(film_name,film_type,film_rate,film_note)
        fetchFn()
        form_window.destroy()

    save_button = tk.Button(form_window, text="Kaydet", command=save_form)
    save_button.pack(pady=10)
