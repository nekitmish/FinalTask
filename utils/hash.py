import bcrypt


def generate_hash(pwd: str) -> bytes:
    return bcrypt.hashpw(
        password=pwd.encode(),
        salt=bcrypt.gensalt(),
    )


def check_hash(pwd: str, hashed: bytes) -> None:
    result = bcrypt.checkpw(
        password=pwd.encode(),
        hashed_password=hashed,
    )
    return result

