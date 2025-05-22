 # 0x00-personal_data

## Description

This project focuses on handling personal data securely, covering log filtering, data encryption, and secure database connections. It includes Python scripts to obfuscate sensitive information in logs, securely hash passwords, and interact with MySQL databases while protecting personally identifiable information (PII).

## Requirements

| Category          | Details                                                                 |
|-------------------|-------------------------------------------------------------------------|
| Python            | Python 3.7 on Ubuntu 18.04 LTS                                         |
| MySQL             | MySQL 5.7+ with mysql-connector-python                                  |
| Packages          | bcrypt, mysql-connector-python                                         |
| File Format       | All Python files must start with `#!/usr/bin/env python3`              |
| Style Guide       | pycodestyle (version 2.5)                                              |
| Documentation     | All modules, classes, and functions must be documented                 |
| README            | A README.md file at the root of the project folder is mandatory        |
| File Length       | File length will be tested using wc                                    |
| Type Annotations  | All functions must have type annotations                               |

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0    | Obfuscate log fields with regex | filtered_logger.py |
| 1    | Implement RedactingFormatter class | filtered_logger.py |
| 2    | Create logger with PII filtering | filtered_logger.py |
| 3    | Connect to secure MySQL database | filtered_logger.py |
| 4    | Read and filter database data | filtered_logger.py |
| 5    | Password hashing with bcrypt | encrypt_password.py |
| 6    | Password validation | encrypt_password.py |

## Learning Objectives

- Understanding PII and personal data protection
- Implementing log obfuscation with regular expressions
- Creating custom logging formatters in Python
- Securely handling database credentials with environment variables
- Working with MySQL databases in Python
- Implementing password hashing with bcrypt
- Validating hashed passwords
- Following security best practices for data handling

## Additional Notes

- All database credentials must be stored as environment variables
- Never store passwords in plain text
- Follow PEP 8 style guidelines for all Python code
- All functions must include type annotations
- Test all scripts thoroughly before submission
- Use the provided user_data.csv for testing log filtering

## Setup and Execution

1. Set up environment variables for database access:
```bash
export PERSONAL_DATA_DB_USERNAME=your_username
export PERSONAL_DATA_DB_PASSWORD=your_password
export PERSONAL_DATA_DB_HOST=localhost
export PERSONAL_DATA_DB_NAME=your_database
```

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
