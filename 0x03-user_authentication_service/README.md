# 0x03-User_authentication_service

## Description
This project implements a complete user authentication service using Flask and SQLAlchemy. It provides user registration, login/logout functionality, session management, and password reset capabilities with secure password hashing using bcrypt. The service follows RESTful API principles and includes comprehensive end-to-end testing.

## Requirements
| Category          | Details                                                                 |
|-------------------|-------------------------------------------------------------------------|
| Python            | Python 3.7 on Ubuntu 18.04 LTS                                         |
| Packages          | Flask, SQLAlchemy 1.3.x, bcrypt, uuid, requests                       |
| File Format       | All Python files must start with `#!/usr/bin/env python3`              |
| Style Guide       | pycodestyle (version 2.5)                                              |
| Documentation     | All modules, classes, and functions must be documented                 |
| README            | A README.md file at the root of the project folder is mandatory        |
| File Length       | File length will be tested using wc                                    |
| Type Annotations  | All functions must have type annotations                               |
| Database          | SQLite with SQLAlchemy ORM                                             |
| Security          | bcrypt for password hashing, UUID for session/token generation         |

## Project Structure
| Task | Description | File |
|------|-------------|------|
| 0    | SQLAlchemy User model | user.py |
| 1    | Add user method | db.py |
| 2    | Find user method | db.py |
| 3    | Update user method | db.py |
| 4    | Hash password function | auth.py |
| 5    | Register user method | auth.py |
| 6    | Basic Flask app | app.py |
| 7    | Register user endpoint | app.py |
| 8    | Credentials validation | auth.py |
| 9    | Generate UUIDs | auth.py |
| 10   | Get session ID | auth.py |
| 11   | Log in endpoint | app.py |
| 12   | Find user by session ID | auth.py |
| 13   | Destroy session | auth.py |
| 14   | Log out endpoint | app.py |
| 15   | User profile endpoint | app.py |
| 16   | Generate reset password token | auth.py |
| 17   | Get reset password token endpoint | app.py |
| 18   | Update password method | auth.py |
| 19   | Update password endpoint | app.py |
| 20   | End-to-end integration test | main.py |

## Learning Objectives
- Implementing user authentication with Flask and SQLAlchemy
- Secure password hashing with bcrypt and salt
- Session management using UUIDs and cookies
- Database operations with SQLAlchemy ORM
- RESTful API design and implementation
- Password reset functionality with secure tokens
- Exception handling and error responses
- End-to-end testing with requests library
- Following separation of concerns (Auth never directly uses DB)
- Type annotations and comprehensive documentation

## API Endpoints
| Method | Endpoint | Description | Form Data | Response |
|--------|----------|-------------|-----------|----------|
| GET    | /        | Welcome message | None | `{"message": "Bienvenue"}` |
| POST   | /users   | Register user | email, password | `{"email": "<email>", "message": "user created"}` |
| POST   | /sessions | User login | email, password | `{"email": "<email>", "message": "logged in"}` + cookie |
| DELETE | /sessions | User logout | session_id (cookie) | Redirect to / |
| GET    | /profile | Get user profile | session_id (cookie) | `{"email": "<email>"}` |
| POST   | /reset_password | Generate reset token | email | `{"email": "<email>", "reset_token": "<token>"}` |
| PUT    | /reset_password | Update password | email, reset_token, new_password | `{"email": "<email>", "message": "Password updated"}` |

## Database Schema
The User model contains the following fields:
- `id` - Integer primary key (auto-increment)
- `email` - Non-nullable string (VARCHAR 250)
- `hashed_password` - Non-nullable string (VARCHAR 250)
- `session_id` - Nullable string (VARCHAR 250)
- `reset_token` - Nullable string (VARCHAR 250)

## Setup
1. Install requirements:
```bash
pip3 install bcrypt flask sqlalchemy requests
```

2. Make files executable:
```bash
chmod +x *.py
```

3. Run the Flask application:
```bash
python3 app.py
```

4. Run integration tests (in another terminal):
```bash
python3 main.py
```

## Security Features
- **Password Security**: bcrypt hashing with automatic salt generation
- **Session Management**: UUID-based session IDs stored as HTTP-only cookies
- **Token Security**: UUID-based reset tokens with single-use validation
- **SQL Injection Protection**: SQLAlchemy ORM with parameterized queries
- **Error Handling**: Proper HTTP status codes without information leakage
- **Authentication Flow**: Secure login/logout with session validation

## Additional Notes
- Flask app runs on `http://0.0.0.0:5000` by default
- Database file `a.db` is created automatically in the project directory
- All endpoints return JSON responses with appropriate HTTP status codes
- The Auth class serves as the main interface - Flask never directly accesses DB
- Integration tests verify complete user lifecycle from registration to password reset
- All functions include comprehensive docstrings and type annotations
- Follows PEP 8 style guidelines and pycodestyle compliance
- 
## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
