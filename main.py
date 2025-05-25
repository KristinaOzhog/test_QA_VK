from typing import List, Dict, Optional, Iterator

class Movie:
    def __init__(self, title: str, genre: str, year: int, rating: float) -> None:
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def __str__(self) -> str:
        return f"{self.title} ({self.year}г.) жанр: {self.genre} рейтинг: {self.rating}"

class MovieIterator(Iterator[Movie]):
    def __init__(self, movies: List[Movie]):
        self._movies = movies
        self._index = 0

    def __next__(self) -> Movie:
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        raise StopIteration()

class MovieCollection:
    def __init__(self) -> None:
        self.movies: Dict[str, Movie] = {}

    def add_movie(self, movie: Movie) -> None:
        self.movies[movie.title] = movie

    def remove_movie(self, title: str) -> None:
        if title in self.movies:
            del self.movies[title]
        else:
            raise ValueError(f'Фильм с названием {title} не найден.')



    def search_by_title(self, title: str) -> Optional[Movie]:
        return self.movies.get(title)

    def search_by_genre(self, genre: str) -> List[Movie]:
        return [movie for movie in self.movies.values() if movie.genre.lower() == genre.lower()]

    def search_by_year(self, year: int) -> List[Movie]:
        return [movie for movie in self.movies.values() if movie.year == year]

    def __iter__(self) -> MovieIterator:
        return MovieIterator(list(self.movies.values()))


collection = MovieCollection()

collection.add_movie(Movie('Гарри Поттер и Узник Азкабана', 'приключения', 2004, 8.2))
collection.add_movie(Movie('Алиса в стране чудес', 'фентези', 2010, 7.1))
collection.add_movie(Movie('Мой любимый враг', 'мелодрама', 2021, 8.2))

for movie in collection.search_by_year(2004):
    print(movie)

for movie in collection.search_by_genre('Мелодрама'):
    print(movie)

for movie in collection:
    print(movie)

collection.remove_movie('Гарри Поттер и Узник Азкабана')

for movie in collection:
    print(movie)

collection.remove_movie('Один дома')
