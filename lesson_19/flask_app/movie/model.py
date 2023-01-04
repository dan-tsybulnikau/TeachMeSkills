from database.database import db


class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    
    
    def to_dict(self):
        return {'id': self.movie_id,
                'title': self.title}