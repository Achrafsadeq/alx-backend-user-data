# 0x02-Session_authentication

## Description

This project implements session-based authentication for a RESTful API using Flask. It builds upon the basic authentication from 0x06-Basic_authentication by adding session management, cookie handling, and user session persistence.

## Requirements

| Category          | Details                                                                 |
|-------------------|-------------------------------------------------------------------------|
| Python            | Python 3.7 on Ubuntu 18.04 LTS                                         |
| Packages          | Flask, pycodestyle, uuid, datetime                                     |
| File Format       | All Python files must start with `#!/usr/bin/env python3`              |
| Style Guide       | pycodestyle (version 2.5)                                              |
| Documentation     | All modules, classes, and functions must be documented                 |
| README            | A README.md file at the root of the project folder is mandatory        |
| File Length       | File length will be tested using wc                                    |
| Type Annotations  | All functions must have type annotations                               |

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0    | Copy basic auth and add /users/me endpoint | api/v1/app.py, api/v1/views/users.py |
| 1    | Empty SessionAuth class | api/v1/auth/session_auth.py, api/v1/app.py |
| 2    | Create session method | api/v1/auth/session_auth.py |
| 3    | User ID for Session ID | api/v1/auth/session_auth.py |
| 4    | Session cookie method | api/v1/auth/auth.py |
| 5    | Before request update | api/v1/app.py |
| 6    | Current user method | api/v1/auth/session_auth.py |
| 7    | Login view | api/v1/views/session_auth.py, api/v1/views/__init__.py |
| 8    | Logout functionality | api/v1/auth/session_auth.py, api/v1/views/session_auth.py |
| 9    | Session expiration | api/v1/auth/session_exp_auth.py, api/v1/app.py |
| 10   | Database sessions | models/user_session.py, api/v1/auth/session_db_auth.py, api/v1/app.py |

## Learning Objectives

- Implementing session-based authentication
- Managing cookies in Flask
- Creating and destroying sessions
- Handling session expiration
- Storing sessions in a database
- Building login/logout functionality
- Protecting API endpoints with session auth
- Working with environment variables for configuration
- Following REST API security best practices

## Additional Notes

- Use environment variables for configuration (API_HOST, API_PORT, AUTH_TYPE, SESSION_NAME, SESSION_DURATION)
- All endpoints must return JSON responses
- Follow PEP 8 style guidelines for all Python code
- All functions must include type annotations
- Test all endpoints thoroughly with curl or Postman
- The User model is provided in the archive

## Setup

1. Install requirements:
```bash
pip3 install -r requirements.txt
```
## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.


