from app import db

class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(64))
    visited = db.Column(db.Boolean, default=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    def __repr__(self):
        return f"<City: ID Number: {self.id}, Name: {self.city_name}, Visited {self.visited}>"