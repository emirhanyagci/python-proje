from movie import getMovies,add_movie
import newMovie
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Favori Film Uygulaman')

window_width = 1200
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.iconbitmap('./images/movie.ico')

header = tk.Frame(root, bg="white", height=50)
header.pack(fill=tk.X, side=tk.TOP)
header_label = tk.Label(header, text="Kaydettiklerim", bg="white", font=("Arial", 14, "bold"))
header_label.pack(side=tk.LEFT, padx=20, pady=10)


add_button = tk.Button(header, text="+", bg="green", fg="white",padx=10, font=("Arial", 12, "bold"),command=lambda : newMovie.open_form(root,saveFn=add_movie,fetchFn=fetchMovies))
add_button.pack(side=tk.RIGHT, padx=20, pady=10)

table_frame = tk.Frame(root, bg="gray")
table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)


columns = ("Isim", "Tur", "Durum", "Puan", "Not") 
tree = ttk.Treeview(table_frame, columns=columns, show='headings')
tree.heading("Isim", text="Isim", anchor="w")  
tree.heading("Tur", text="Tur", anchor="w")   
tree.heading("Durum", text="Durum", anchor="w") 
tree.heading("Puan", text="Puan", anchor="w") 
tree.heading("Not", text="Not", anchor="w") 

tree.column("Isim", width=150, anchor="w") 
tree.column("Tur", width=100, anchor="w")  
tree.column("Durum", width=100, anchor="w") 
tree.column("Puan", width=100, anchor="w")  
tree.column("Not", width=100, anchor="w")


def fetchMovies():
    tree.delete(*tree.get_children())

    movies = getMovies()
    for movie in movies:
        print(movie)
        tree.insert("", tk.END, values=(movie["name"],movie["type"],movie["status"],movie["rate"],movie["note"]))
    
selectedMovie = ""
fetchMovies()
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = list(item['values'])
        record = [str(i) for i in record]

        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)
tree.pack(fill="both", expand=True)

root.mainloop()
