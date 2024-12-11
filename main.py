import movie
import tkinter as tk


film = movie.Movie("Dune 2", "Kurgu", "Izlenecek", 4, "kesin izle").getMovie()
root = tk.Tk()
root.title('Favori Film Uygulaman')

window_width = 1200
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.iconbitmap('./images/movie .ico')

root.mainloop()
movie.saveMovie(film)
