from app import db

# class Crystal: 
#     def __init__(self, id, name, color, powers):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.powers = powers


class Crystal (db.Model):
    # id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    id = db.Column(db.Integer, primary_key=True, autoincrement = True) 
    name = db.Column(db.String)
    color = db.Column(db.String)
    powers = db.Column(db.String)