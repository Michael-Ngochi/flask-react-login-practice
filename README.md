
# Full Stack User Authentication App

This project is a simple full-stack user authentication system using:

- **Backend:** Flask (Python)
- **Frontend:** React (JavaScript)
- **Database:** SQLite (via SQLAlchemy)

---

## 🗂 Project Structure

```
project-root/
│
├── server/      # Flask backend (API)
│   ├── app.py
│   ├── models/
│   │     ├── user.py
│   │     ├── role.py
│   │     └── __init__.py
│   ├── config.py
│   └── __init__.py
│
└── client/      # React frontend
    └── login.jsx
```

---

## ⚙ Backend Setup (Flask API)

### 1 Navigate to backend folder

```bash
cd server
```

### 2️ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️ Install dependencies

```bash
pip install -r requirements.txt
```


### 4️ Initialize database

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 5️ Run the server

```bash
export FLASK_APP=app.py
export FLASK_ENV=development  # optional, for debug mode

flask run
```

The server will start at:

```
http://localhost:5000
```

---

## ⚙ Frontend Setup (React)

### 1️ Navigate to frontend folder

```bash
cd client
```

### 2️ Install dependencies

```bash
npm install
```

### 3️ Run frontend

```bash
npm start
```

The frontend will run at:

```
http://localhost:3000
```

---

## 🖥 API Routes

| Method | Route      | Description           |
|--------|------------|-----------------------|
| POST   | /register  | Register new user     |
| POST   | /login     | User login            |
| GET    | /users     | Get all users (admin) |

---

## 🔐 Registration Behavior
- Passwords are hashed using Werkzeug.
- Role-based assignment supported (`Admin`, `Staff`, etc.)

---

## 🛑 Notes

- Database file is `users.db` (SQLite by default).
- Make sure CORS is enabled for frontend-backend communication (already included).
- You can easily extend this project to use JWT authentication.

---

## 🔗 Repository

[GitHub Repository](https://github.com/Michael-Ngochi/flask-react-login-practice.git)