import secrets
import string

def generate_password(length=int):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.?"
    password = "".join(
        secrets.choice(characters) for _ in range(length)
    )
    return password

print(generate_password(12))