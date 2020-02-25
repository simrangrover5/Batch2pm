
##Movie api

def showimg(data,poster):
    image = requests.get(poster)
    if image.status_code == 200:
        title = data['Title']
        with open(f"{title}.jpeg","wb") as f:
            f.write(image.content)
        img = plt.imread(f"{title}.jpeg")
        plt.imshow(img)
        plt.xticks([])
        plt.yticks([])
        plt.show()
    else:
        return "Incorrect url"



def checkmovie(movie):
    url = f"http://www.omdbapi.com/?t={movie}&apikey=e22bdd41"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        title = data['Title']
        date = data['Released']
        runtime = data['Runtime']
        genre = data['Genre']
        ratings = data['Ratings'][0]['Value']
        plot = data['Plot']
        poster = data['Poster']
        if poster:
            showimg(data,poster)
        else:
            print("No poster for this movie....")
        print(title,date,runtime,genre,ratings,plot,sep="\n")
    else:
        print("The url is not correct......")
        
        
        
if __name__ == "__main__":
    import requests,json
    import matplotlib.pyplot as plt
    movie = input("Enter the name of movie : ")
    checkmovie(movie)
