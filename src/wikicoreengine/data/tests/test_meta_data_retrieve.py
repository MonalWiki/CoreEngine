from io import BytesIO
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID



storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
# storage backend 
storage_routing(NAMESPACES, storage_base_dir)

revid = "c76aefcb2df44727b3a84d238a021af9"

meta =  {'itemtype': 'default',
         'contenttype': 'text/x-markdown;charset=utf-8',
         'namespace': NAMESPACE_DEFAULT,
         'summary': 'summary 9',
         'name': ['Home2'],
         'tags': ['sfsd sfsfh tha3'],
         'comment': 'mycomment9',
         'rev_number': 1}

data =  b"this si same string text;convereted to bytes and then to BytesIO"

revid = storage_routing.namespace_storage_map[''].store(meta, data)
#print ("revid = ", revid)
#revid = "fe0ece342daa4c39a854dd57081b4deb"
meta, data = storage_routing.namespace_storage_map[''].retrieve(revid)
print ("meta = ", meta)
print ("data = ", data)

