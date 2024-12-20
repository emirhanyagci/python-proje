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
        if(5 == 5) :
            pass
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
   
def update_status():
    movies = getMovies()
    name = input("Güncellenecek dizi veya filmi girin:")
    for item in movies:
        if item["name"] == name:
            status = input("Yeni durumu girin (İzlendi, İzlenecek, İzleniyor):")
            if status in ["İzlendi", "İzlenecek", "İzleniyor"]:
                item["status"] = status
                with open('movies.json', "w") as moviesJson:
                    json.dump({"movies": movies}, moviesJson)
                print("Durum güncellendi.")
                return
            else:
                print("Geçersiz durum")
                return
    print("Dizi veya film bulunamadı")

def deleteMovies():
    movies=getMovies()
    name = input("Silinecek dizi veya filmi girin:")
    for item in movies:
        if item["name"]==name:
            confirm = input("Bu ögeyi silmek istediğinizden emin misiniz ?")
            if confirm== 'Evet' or confirm== 'evet':
                movies.remove(item)
                with open('movies.json', 'w') as moviesJson:
                    json.dump({"movies": movies}, moviesJson)
                print(f"'{name}' başarıyla silindi.")
                return
            else:
                print("Silme işlemi iptal edildi.")
                return
    print("Dizi veya film bulunamadı.")

def add_movie(name,type,status,note):
    addedmovie=Movie(name,type,status,rate=0,note=note).getMovie()
    saveMovie(addedmovie)

