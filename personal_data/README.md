# Personal Data

This directory contains Python modules focused on handling personal and sensitive data securely, with an emphasis on password encryption and protecting Personally Identifiable Information (PII) in logs.

## Files

- **filtered_logger.py**
	- Provides tools for filtering and obfuscating log messages that contain PII fields such as name, email, phone, SSN, and password.
	- Includes a custom logging formatter (`RedactingFormatter`) that automatically redacts sensitive fields in log output.
	- Connects to a MySQL database using credentials from environment variables and demonstrates secure logging of user data.

- **encrypt_password.py**
	- Contains functions for securely hashing passwords using bcrypt (`hash_password`) and for verifying passwords (`is_valid`).

## Usage

- Use `filtered_logger.py` to safely log user data from a database, ensuring that sensitive fields are never exposed in logs.
- Use `encrypt_password.py` to hash and verify passwords securely in your applications.

## Security Practices

- All sensitive fields are redacted in logs to prevent accidental data leaks.
- Passwords are never stored or transmitted in plain text; bcrypt is used for secure password hashing.
- Database credentials are loaded from environment variables for better security.

## Example

```python
from encrypt_password import hash_password, is_valid

hashed = hash_password('mysecretpassword')
print(is_valid(hashed, 'mysecretpassword'))  # True
```

## Environment Variables for Database Connection
- `PERSONAL_DATA_DB_USERNAME` (default: `root`)
- `PERSONAL_DATA_DB_PASSWORD` (default: empty)
- `PERSONAL_DATA_DB_HOST` (default: `localhost`)
- `PERSONAL_DATA_DB_NAME` (required)

## Disclaimer
This code is for educational purposes and demonstrates best practices for handling personal data in Python applications.