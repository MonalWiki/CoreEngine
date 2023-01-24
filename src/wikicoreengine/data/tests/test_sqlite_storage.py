from sqlite3 import connect, Row
from io import BytesIO
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.Name import CompositeName


storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"

db_filepath = f"{storage_base_dir}//.meta.db"

conn = connect(db_filepath)
conn.row_factory = Row
tblname = "store"
rows = list(conn.execute(f"select value from {tblname}"))
print(rows)
key = "kuchi"
value = "bhalo"
#conn.execute(f"""insert into  {tblname} values ("{key}", "{value}")""")

rows = conn.execute(f"select value from {tblname}").fetchall()
for row in rows:
    print (row)

conn.commit()
