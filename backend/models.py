from config import db

# Store and load sample images
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_name = db.Column(db.String(100), nullable=False)
    filepath = db.Column(db.String(100), nullable=False)
    
    def to_json(self):
        return {
            'id': self.id,
            'img_name': self.img_name,
            'filepath': self.filepath
        }