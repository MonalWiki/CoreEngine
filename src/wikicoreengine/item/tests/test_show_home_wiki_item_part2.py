from io import BytesIO
import os
from wikicoreengine.wikicfg import NAMESPACES, WIKINAME, BACKEND_DATADIR_BASE
from wikicoreengine.data.storage_routing import storage_routing
from wikicoreengine.data.indexes import indexes, get_storage_revision

from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.Name import CompositeName, url_to_compositeName
from wikicoreengine.item import WikiItem

storage_base_dir = f"{BACKEND_DATADIR_BASE}/{WIKINAME}"
# storage backend 
storage_routing(NAMESPACES, storage_base_dir)
# init indexes 
indexes(storage_base_dir)



{'itemtype': 'default', 'contenttype': 'text/csv;charset=utf-8', 'template': ' HTTP/1.1'}

item_name = "Home"
fqcn = url_to_compositeName(item_name)
itemtype = 'default'
contenttype = 'text/csv;charset=utf-8'
rev_id=CURRENT
rev = get_storage_revision(fqcn, itemtype, contenttype, rev_id)

print (rev)

