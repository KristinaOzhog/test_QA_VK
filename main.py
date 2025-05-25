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
        self.collections: Dict[str, List[Movie]] = {}

    def add_movie(self, movie: Movie) -> None:
        self.movies[movie.title] = movie

    def remove_movie(self, title: str) -> None:
        if title in self.movies:
            del self.movies[title]
        else:
            raise ValueError(f'Фильм с названием {title} не найден.')

    def create_collection(self, name: str) -> None:
        if name in self.collections:
            raise ValueError(f"Коллекция '{name}' уже существует")
        self.collections[name] = []

    def add_to_collection(self, collection_name: str, movie_title: str) -> None:
        if collection_name not in self.collections:
            raise ValueError(f"Коллекция '{collection_name}' не найдена")
        if movie_title not in self.movies:
            raise ValueError(f"Фильм '{movie_title}' не найден")

        movie = self.movies[movie_title]
        if movie in self.collections[collection_name]:
            raise ValueError(f"Фильм уже есть в коллекции '{collection_name}'")

        self.collections[collection_name].append(movie)

    def remove_movie_from_collection(self, collection_name: str, movie_title: str) -> None:
        if collection_name not in self.collections:
            raise ValueError(f"Коллекция '{collection_name}' не найдена")
        if movie_title not in self.movies:
            raise ValueError(f"Фильм '{movie_title}' не найден")

        movie = self.movies[movie_title]
        if movie not in self.collections[collection_name]:
            raise ValueError(f"Фильм не найден в коллекции '{collection_name}'")

        self.collections[collection_name].remove(movie)

    def get_collection(self, name: str) -> List[Movie]:
        return self.collections.get(name, [])

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
collection.add_movie(Movie('Зеленая миля', 'драма', 1999, 9.1))
collection.add_movie(Movie('Побег из Шоушенка', 'драма', 1994, 9.0))
collection.add_movie(Movie('Форрест Гамп', 'драма', 1994, 8.9))
collection.add_movie(Movie('Интерстеллар', 'фантастика', 2014, 8.6))

collection.create_collection('Драмы 90-х')
collection.create_collection('Лучшие фильмы')

collection.add_to_collection('Драмы 90-х', 'Зеленая миля')
collection.add_to_collection('Драмы 90-х', 'Побег из Шоушенка')
collection.add_to_collection('Драмы 90-х', 'Форрест Гамп')
collection.add_to_collection('Лучшие фильмы', 'Побег из Шоушенка')
collection.add_to_collection('Лучшие фильмы', 'Интерстеллар')
collection.add_to_collection('Лучшие фильмы', 'Мой любимый враг')
collection.add_to_collection('Лучшие фильмы', 'Алиса в стране чудес')

print('Фильмы 1994 года')
for movie in collection.search_by_year(1994):
    print(movie)

print('Все драмы в кинотеатре')
for movie in collection.search_by_genre('драма'):
    print(movie)

print('Все фильмы кинотеатра')
for movie in collection:
    print(movie)

collection.remove_movie('Гарри Поттер и Узник Азкабана')

print('Все фильмы кинотеатра')
for movie in collection:
    print(movie)

collection.remove_movie("Форрест Гамп")

print("Фильмы в коллекции 'Драмы 90-х':")
for movie in collection.get_collection("Драмы 90-х"):
    print(movie)

