import tkinter as tk
from PIL import ImageTk, Image

from src.MovieListVisualator import MovieListVisualator
from src.movie_recommender import MovieRecommender

HEIGHT = 500
WIDTH = 600


def getMovies(movie,root,m_rec):
    if len(movie)<1:
        return
    mainf = tk.Frame(root, bg='LIGHTBLUE', bd=1)
    mainf.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')
    movies = m_rec.movieRecommender(movie)
    MovieListVisualator(mainf,movies).pack(side="top", fill="both", expand=True)

m_rec = MovieRecommender()
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('movies.jpg'))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='LIGHTBLUE', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.65, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Movies", font=40, command=lambda: getMovies(entry.get(),root,m_rec))
button.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()