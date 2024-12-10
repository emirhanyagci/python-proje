import json
import os.path


class Movie:
    def __init__(self, name, type, status, rate, note):
        self.name = name
        self.type = type
        self.status = status
        self.rate = rate
        self.note = note

    def getMovie(self):
        return {
            "name": self.name,
            "type": self.type,
            "status": self.status,
            "rate": self.rate,
            "note": self.note
        }


def saveMovie(movie):
    if (not os.path.exists("movies.json")):
        with open("movies.json", "x") as dosya:
            json.dump({
                "movies": []
            }, dosya)

    with open("movies.json") as moviesJson:

        data = list(json.load(moviesJson)["movies"])
        data.append(movie)
        with open('movies.json', 'w') as moviesJson:
            json.dump({
                "movies": data
            }, moviesJson)


def getMovies():
    try:
        with open("movies.json") as moviesJson:
            data = list(json.load(moviesJson)["movies"])
            return data
    except FileNotFoundError:
        print("Kaydedilmis film yok")


film1 = Movie("Dune 2", "Kurgu", "Izlenecek", 4, "kesin izle").getMovie()

m = getMovies()

saveMovie(film1)
