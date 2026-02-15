from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    decode_access_token,
)


hashed = get_password_hash("testpassword")
print(f"Hashed: {hashed}")
print(f"Verify correct: {verify_password('testpassword', hashed)}")
print(f"Verify wrong: {verify_password('wrongpass', hashed)}")

# Test JWT
token = create_access_token({"sub": "123"})
print(f"Token: {token}")
decoded = decode_access_token(token)
print(f"Decoded: {decoded}")
