# 🛒 Phimart — E-commerce REST API (Django + DRF)

Phimart is a fully functional **E-commerce REST API** built using **Django Rest Framework (DRF)**.  
It provides endpoints for managing **products**, **categories**, **carts**, **orders**, and **authentication** using **JWT (Djoser)**.  
The project also includes **Swagger API documentation** powered by `drf_yasg`.

---

## 🚀 Features

- 🔐 **JWT Authentication** (via [Djoser](https://djoser.readthedocs.io/en/latest/))
- 🧺 **Cart & Orders Management**
- 🛍️ **Product & Category CRUD APIs**
- 👤 **User Registration & Login**
- 📘 **Interactive API Docs** (Swagger / ReDoc)
- ⚙️ **Modular and Scalable Code Structure**

---

## 🧰 Tech Stack

| Component        | Technology Used         |
|------------------|--------------------------|
| Backend Framework | Django 5 / Django REST Framework |
| Authentication    | Djoser + JWT (SimpleJWT) |
| Database          | SQLite / PostgreSQL (configurable) |
| API Docs          | drf_yasg (Swagger & ReDoc) |
| Language          | Python 3.11+ |

---

## 📁 Project Structure
phimart/
│
├── manage.py
├── phimart/ # Main project config
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── products/ # Product & Category app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── orders/ # Orders & Cart management
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── users/ # User management with JWT (Djoser)
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
└── requirements.txt

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/phimart.git
cd phimart
```
### 2️⃣ Create Virtual env
```bash
Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux
```
### 3️⃣Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Apply migrations
```bash
python manage.py migrate
```
### 5️⃣ Create superuser
```bash
python manage.py createsuperuser
```
### 6️⃣ Run the development server
```bash
python manage.py runserver
```
### Now open your browser at : 
```bash
http://127.0.0.1:8000/
```
---

### 🧾 API Documentation

**Phimart includes interactive API documentation generated via drf_yasg.**




| Tool | URL |
| ----------- | ----------- |
| Swagger | http://127.0.0.1:8000/swagger/ |
| ReDoc | http://127.0.0.1:8000/redoc/ |

---

### 🔑 Authentication (JWT + Djoser)
| Action | End-Poind | Method |
| ----------- | ----------- |---------|
| Register User | /auth/users/ | POST |
| Login | /auth/jwt/create/ | POST |
| Refresh Token | /auth/jwt/refresh/ | POST |
| Get User Info | /auth/users/me/ | GET |
---
### Example Login Request:
```
json:
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```
### Example Response:
```
json:
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```
### 🧪 Example Environment Variables

**Create a .env file in the root directory:**
```
ini

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST = your_email_host
```

### 📄 License
---

This project is licensed under the MIT License — feel free to use and modify it.

---

### Author

**Fardin Khan**

*Django Backend Developer*

📧 fardinazim7@gmail.com

🌐 https://fardin-05.github.io


⭐ If you like this project, consider giving it a star on GitHub!
