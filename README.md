# PRODIGY_BD_03
Persistent Storage with Database Integration 

## 🚀 Overview

The goal of this task is to demonstrate how to connect a **Django REST API** with a **NoSQL database (MongoDB)** for persistent storage.  
It showcases environment-based configuration, connection pooling, and CRUD functionality.

---

## ✨ Features

-  **Django + MongoDB Integration** using MongoEngine (ODM)
- 🧩 **Persistent Storage** of user data in MongoDB
- ⚙️ **Environment Variables (.env)** for secure DB credentials
- 🧱 **Connection Pooling** for better database performance
- 🌍 **REST API Endpoints** for full CRUD operations:
  - Create User
  - Read All Users
  - Read Single User
  - Update User
  - Delete User
- 🧪 **Postman Tested** endpoints
- 🔐 **Environment-Specific Configuration** (Development / Production)


## 🧠 Technology Stack

| Component | Technology Used |
|------------|----------------|
| **Backend Framework** | Django  |
| **Database** | MongoDB (NoSQL) |
| **ODM** | MongoEngine |
| **Language** | Python  |
| **API Tool** | Django REST Framework |
| **Environment Management** | python-dotenv |
| **Testing** | Postman |

---

## ⚙️ Project Setup & Installation

1 Create Virtual Environment
python -m venv venv
venv\Scripts\activate 

2 Install Required Packages
pip install -r requirements.txt

3 Create .env File

Create a .env file in your project root:

DB_NAME=harishdb
DB_HOST=localhost
DB_PORT=27017
SECRET_KEY=harishsecret
DEBUG=True

4 Run MongoDB

Make sure MongoDB is running locally:

mongod

5 Run Django Server
python manage.py runserver

## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for educational and professional purposes.

## 🎥 Output
<img width="1920" height="1080" alt="Screenshot 2025-10-19 194551" src="https://github.com/user-attachments/assets/ced6d336-8ab3-4e97-ab40-0bf5ef2683eb" />

