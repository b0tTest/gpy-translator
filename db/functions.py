from .db import db, dbc


async def add_chat(chat_id, chat_type):
    if chat_type == "private":
        dbc.execute("INSERT INTO users (user_id) values (?)", (chat_id,))
        db.commit()


async def chat_exists(chat_id, chat_type):
    if chat_type == "private":
        dbc.execute("SELECT user_id FROM users where user_id = ?", (chat_id,))
        return bool(dbc.fetchone())
    raise TypeError("Unknown chat type '%s'." % chat_type)


async def get_lang(chat_id: int, chat_type: str) -> str:
    if chat_type == "private":
        dbc.execute("SELECT chat_lang FROM users WHERE user_id = ?", (chat_id,))
        ul = dbc.fetchone()
    return ul[0] if ul else None


async def set_lang(chat_id: int, chat_type: str, lang_code: str):
    if chat_type == "private":
        dbc.execute(
            "UPDATE users SET chat_lang = ? WHERE user_id = ?", (lang_code, chat_id))
        db.commit()


async def get_users_count():
    a = dbc.execute("""select count(*) from users""")
    b = a.fetchone()[0]
    return b
