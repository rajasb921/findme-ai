from flask import request, jsonify
from config import app, db
from models import Image

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to findme.ai', 200

@app.route('/images', methods=['GET']) 
def get_images():
    images = Image.query.all()
    return jsonify([image.to_json() for image in images])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)