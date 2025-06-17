from flask import Flask, jsonify,request
from flask_migrate import Migrate
from .models import db
from .config import Config
from .models.user import User
from .models.role import Role 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app=Flask(__name__)

app.config.from_object(Config)


CORS(app)

db.init_app(app)
migrate = Migrate(app, db)

# Register all routes
@app.route('/users', methods=['GET'])
def get_users():
    users=User.query.all()
    results=[{
        'id':u.id,
        'name':u.name,
        'email':u.email,
        'role':u.role.name
    }for u in users
    ]
    return jsonify(results),200

if __name__ == '__main__':
    app.run(debug=True)
    
# Register user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role_name = data.get('role')

    if not all([name, email, password, role_name]):
        return jsonify({'error': 'All fields are required'}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    role = Role.query.filter_by(name=role_name).first()
    if not role:
        return jsonify({'error': 'Invalid role'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password, role=role)
    new_user.set_password(password)
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Login user
@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({'error': 'Email and password required'}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return jsonify({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role.name
            }
        }), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)

