class Marca(db.Model):
    id = db.column(db.Integer, primary_key=True)
    nombre = db.column(db.String(30, nullable=False)
    
    def