from . import model




def create_movie(db, movie_dict):
    db_movie = model.Movie(**movie_dict)