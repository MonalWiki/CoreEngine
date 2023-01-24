from io import BytesIO
import os

from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.constant_keys import NAME, NAMESPACE

storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"

storage_routing(NAMESPACES, storage_base_dir)
revid_or_metaid = storage_routing.namespace_storage_map[''].store({NAME: 'test'}, b'this is test string')
storage_routing.commit()
print("revid_or_metaid = ", revid_or_metaid)
