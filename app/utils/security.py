from passlib.context import CryptContext

Pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str)-> str:
    return Pwd_context.hash(password)

def verify_password(plain_password: str , hashed_password: str)-> bool:
    return Pwd_context.verify(plain_password , hashed_password)