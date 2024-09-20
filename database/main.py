import sqlite3, uuid

sqlite3.register_adapter(uuid.UUID, lambda u: u.bytes_le)
sqlite3.register_converter("GUID", lambda b: uuid.UUID(bytes_le=b))

def get_db():
    connection = sqlite3.connect(
        'schedule.db', 
        isolation_level=None, 
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    db = connection.cursor()

    return db