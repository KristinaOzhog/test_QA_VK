from typing import List, Dict, Optional, Iterator

class Movie:
    def __init__(self, title: str, genre: str, year: int, rating: float) -> None:
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def __str__(self) -> str:
        return f"{self.title} ({self.year}г.) жанр: {self.genre} рейтинг: {self.rating}"