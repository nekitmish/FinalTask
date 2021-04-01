import re

from utils.db_api.db_commands import select_user


async def check_valid_ref(ref: str):
    if re.match(r"\d+$", ref):
        try:
            user = await select_user(int(ref))
        except Exception:
            return False
        return True
