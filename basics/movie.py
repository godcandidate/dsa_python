class Movie:
    def __init__(self, title, genre, release_year):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        
    def display(self):
        print(f"Title: {self.title}, Genre: {self.genre}, Release Year: {self.release_year}")

    # TODO: Add a function here that takes a new title
    def set_title(self, title):
        self.title = title


if __name__ == "__main__":
    movie = Movie("Inception", "Sci-Fi", 2010)
    movie.display()

    # TODO: Call the method on movie with the value "Interstellar"
    movie.set_title("Interstellar")
    # TODO: Display the movie details
    movie.display()