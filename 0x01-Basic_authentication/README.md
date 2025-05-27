# 0x01-Basic_authentication

## Description

This project implements basic authentication for a RESTful API using Flask. It covers error handling, route protection, and basic auth implementation including Base64 encoding/decoding and user credential validation.

## Requirements

| Category          | Details                                                                 |
|-------------------|-------------------------------------------------------------------------|
| Python            | Python 3.7 on Ubuntu 18.04 LTS                                         |
| Packages          | Flask, pycodestyle                                                     |
| File Format       | All Python files must start with `#!/usr/bin/env python3`              |
| Style Guide       | pycodestyle (version 2.5)                                              |
| Documentation     | All modules, classes, and functions must be documented                 |
| README            | A README.md file at the root of the project folder is mandatory        |
| File Length       | File length will be tested using wc                                    |
| Type Annotations  | All functions must have type annotations                               |

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0    | Simple API setup | api/v1/app.py, api/v1/views/index.py |
| 1    | Unauthorized error handler (401) | api/v1/app.py, api/v1/views/index.py |
| 2    | Forbidden error handler (403) | api/v1/app.py, api/v1/views/index.py |
| 3    | Auth class template | api/v1/auth/auth.py |
| 4    | Define excluded routes | api/v1/auth/auth.py |
| 5    | Request validation | api/v1/app.py |
| 6    | Basic auth class | api/v1/auth/basic_auth.py |
| 7    | Base64 extraction | api/v1/auth/basic_auth.py |
| 8    | Base64 decoding | api/v1/auth/basic_auth.py |
| 9    | User credentials extraction | api/v1/auth/basic_auth.py |
| 10   | User object retrieval | api/v1/auth/basic_auth.py |
| 11   | Complete basic auth | api/v1/auth/basic_auth.py |
| 12   | Allow passwords with ":" | api/v1/auth/basic_auth.py |
| 13   | Wildcard route exclusion | api/v1/auth/auth.py |

## Learning Objectives

- Implementing HTTP error handlers in Flask
- Creating authentication middleware
- Working with Base64 encoding/decoding
- Validating user credentials
- Protecting API routes
- Handling authorization headers
- Managing excluded routes
- Implementing wildcard route matching
- Following REST API security best practices

## Additional Notes

- Use environment variables for configuration (API_HOST, API_PORT, AUTH_TYPE)
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

