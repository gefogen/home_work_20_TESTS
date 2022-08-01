from unittest.mock import MagicMock
import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    jonh = Movie(id=1, title='Что-нибудь', description='Как-нибудь', trailer='Тут', year=2005, rating=5.2, genre_id=1, director_id=1)
    kate = Movie(id=1, title='Вот это', description='Здесь', trailer='Произошло', year=2007, rating=6.4, genre_id=2, director_id=2)
    max = Movie(id=3, title='Как здесь', description='Это', trailer='Оказалось?', year=2013, rating=7.3, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=jonh)
    movie_dao.get_all = MagicMock(return_value=[jonh, kate, max])
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "name": "Ivan"
        }
        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "name": "Ivan"
        }
        self.movie_service.update(movie_d)