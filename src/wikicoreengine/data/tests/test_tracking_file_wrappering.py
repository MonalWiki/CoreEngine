from addict import Dict
from io import BytesIO
import os


import os
import base64
import zlib

import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing

from sqlite3 import connect, Row
#from .crypto import make_uuid
from wikicoreengine.constant_keys import REVID, DATAID, SIZE, HASH_ALGORITHM
from wikicoreengine.data.utils import serialize, TrackingFileWrapper
from wikicoreengine.data.crypto import make_uuid
#from wikicoreengine.wikicfg import STORAGETYPE, STORAGEARGS
#from wikicoreengine.system_params import StorageType

storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
# storage backend 
storage_routing(NAMESPACES, storage_base_dir)

data = b"this si same string text;convereted to bytes and then to BytesIO"
#tfw = TrackingFileWrapper(data, hash_method=HASH_ALGORITHM)
#godknows  = tfw.read()
datatbl_manager = storage_routing.namespace_storage_map[''].datatbl_manager

dataid = make_uuid()
datatbl_manager.set_item(dataid,  data)

answer = datatbl_manager.get_item(dataid)
print(answer)
